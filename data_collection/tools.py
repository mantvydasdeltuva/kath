"""Module providing a functionality to collect data from various sources."""

import os
import requests
from requests.exceptions import RequestException
import pandas as pd
from pandas import DataFrame
from constants import LOVD_VARIABLES_DATA_TYPES



# EXCEPTIONS
class BadResponseException(Exception):
    """Custom exception for bad responses."""


class DownloadError(Exception):
    """Custom exception for download errors."""



def get_file_from_url(url, save_to, override=False):
    """
    Gets file from url and saves it into provided path. Overrides, if override is True.

    :param str url: link with file
    :param str save_to: path to save
    :param bool override: needs override
    """

    # check if directory exists, if not - create
    save_to_dir = os.path.dirname(save_to)
    if not os.path.exists(save_to_dir):
        os.makedirs(save_to_dir)

    # check if file exist and needs to override
    if os.path.exists(save_to) and not override:
        print(f"The file at {save_to} already exists.")
        return

    try:
        response = requests.get(url, timeout=10)
    except RequestException as e:
        raise DownloadError(f"Error while downloading file from {url}") from e

    if response.status_code != 200:
        raise BadResponseException(f"Bad response from {url}."
                                   f" Status code: {response.status_code}")

    with open(save_to, "wb") as f:
        f.write(response.content)


def convert_lovd_to_datatype(df_dict):
    """
    Convert data from LOVD format table to desired data format based on specified data types.

    :param dict[str, tuple[DataFrame, list[str]] df_dict: Dictionary of tables where each table is represented by its name
     and contains a tuple with a DataFrame and a list of notes.
    """

    for constant_table_name, attributes in LOVD_DATA_TYPES.items():
        frame, notes = df_dict[constant_table_name]
        for column, data_type in attributes.items():
            if column not in frame.columns:
                continue

            match data_type:
                case "Date":
                    frame[column] = pd.to_datetime(frame[column], errors='coerce')
                case "Boolean":
                    frame[column] = (frame[column] != 0).astype('bool')
                case "String":
                    frame[column] = frame[column].astype('string')
                case "Integer":
                    frame[column] = pd.to_numeric(frame[column], errors='coerce').astype('Int64')
                case "Double":
                    frame[column] = pd.to_numeric(frame[column], errors='coerce').astype('float')
                case _:
                    continue


def from_lovd_to_pandas(path):
    """
    Converts data from text file with LOVD format to dictionary of tables. \
    Key is name of table, value is tuple, where first element is data saved as \
    pandas DataFrame and second element is list of notes.

    :param str path: path to text file
    :returns: dictionary of tables
    :rtype: dict[str, tuple[DataFrame, list[str]]]
    """

    # Check if the file exists
    if not os.path.exists(path):
        raise FileNotFoundError(f"The file at {path} does not exist.")

    d = {}

    with open(path, encoding="UTF-8") as f:
        # skip header
        [f.readline() for _ in range(4)]  # pylint: disable=expression-not-assigned

        while True:
            line = f.readline()

            if line == '':
                break

            table_name = line.split("##")[1].strip()

            notes = []
            line = f.readline()
            while line.startswith("##"):
                notes.append(line[2:-1])
                line = f.readline()

            table_header = [column[3:-3] for column in line[:-1].split('\t')]
            frame = DataFrame([], columns=table_header)
            line = f.readline()
            while line != '\n':
                variables = [variable[1:-1] for variable in line[:-1].split('\t')]
                observation = DataFrame([variables], columns=table_header)
                frame = pd.concat([frame, observation], ignore_index=True)
                line = f.readline()

                while line != '\n':
                    variables = [variable[1:-1] for variable in line[:-1].split('\t')]
                    observation = DataFrame([variables], columns=table_header)
                    frame = pd.concat([frame, observation], ignore_index=True)
                    line = f.readline()

                d[table_name] = (frame, notes)
                # skip inter tables lines
                [f.readline() for _ in range(1)]


            d[table_name] = (frame, notes)
            # skip inter tables lines
            [f.readline() for _ in range(1)]  # pylint: disable=expression-not-assigned

    return d


def from_clinvar_name_to_dna(name):
    """
    Custom cleaner to extract DNA from Clinvar name variable.

    :param str name:
    :returns: extracted DNA
    :rtype: str
    """

    start = name.find(":") + 1
    ends = {'del', 'delins', 'dup', 'ins', 'inv', 'subst'}

    if "p." in name:
        name = name[:name.index("p.") - 1].strip()

    end = len(name)

    for i in ends:
        if i in name:
            end = name.index(i) + len(i)
            break

    return name[start:end]
  
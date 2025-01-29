---
title: Back-End Setup
description: A guide to setting up the back-end environment for kath project development.
tags: 
    - Development
    - Back-End
    - Setup
    - Guide
draft: false
date: 2025-01-23
---

This guide offers step-by-step instructions for setting up and running a **Flask-based** development server on a Windows system using **Windows Subsystem for Linux (WSL)**.

---

## Step 1 - Install WSL

1. **Open PowerShell**
   
    Search for _PowerShell_ in the Start menu, right-click, and select Open.

2. **Install WSL**

    Run the following command to install WSL with default _Ubuntu_ distribution.

    ```bash
    wsl --install
    ```

    Follow the on-screen instructions to create a new user and password.

> [!warning]
> A system restart may be required.

---

## Step 2 - Launch WSL

1. **Open PowerShell**

    Search for _PowerShell_ in the Start menu, right-click, and select Open.

2. **Run WSL**

    Run the following command to launch WSL with  _Ubuntu_ distribution.

    ```bash
    wsl -d ubuntu
    ```

---

## Step 3 - Install Required Tools in WSL

1. **Navigate to the Home Directory**

    ```bash
    cd ~
    ```

2. **Update Package List**

    Run the following command to update _Ubuntu_ default packages.

    ```bash
    sudo apt update
    ```

    Wait for it to complete.

3. **Install Required Packages**
   
    Run the following command to install packages required for environment.

    ```bash
    sudo apt install python3 python3-pip python3-venv redis unzip
    ```

> [!info]
> Respond with `y` to confirm when a confirmation prompt appears.

---

## Step 4 - Set Up Visual Studio Code

1. **Open VS Code**

    If you haven't already installed Visual Studio Code, you can download it from [Visual Studio Code official website](https://code.visualstudio.com/).

2. **Install the WSL Extension**

    Go to the Extensions view by clicking the Extensions icon in the Activity Bar on the side of the window. Search for `WSL` and install it.

3. **Connect to WSL**

    In the VS Code window, open the _Command Palette_ `Ctrl+Shift+P`. Type `>WSL: Connect to WSL using Distro...` and select it to connect to WSL using VS Code.

> [!info]
> If there are multiple distributions in your system, select `Ubuntu`.

4. **Open Project Folder**

    In the WSL-connected VS Code window, open the _Command Palette_ `Ctrl+Shift+P`, type `>WSL: Open Folder in WSL...` and navigate to your project folder located on Windows. 
    
> [!example]
> WSL can access your Windows files under `/mnt/{drive_name}/`, so your project might be located at something like `/mnt/c/Users/YourUsername/Path/To/Project`. To start navigation through files, type `/mnt/c/`.


5. **Install Essential Extensions**

    With the WSL window open in VS Code, go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window.
    
    <br>
    Search and install the following extensions in WSL:

    - **Python** - provides rich support for the Python language, including features for linting, debugging, and code navigation.
    - **Black Formatter** - integrates the Black code formatter into VS Code, ensuring your Python code is formatted consistently.
    - **Rainbow CSV** - highlights CSV and TSV files with color coding, making it easier to view and edit tabular data.
  
> [!note]
> This step is optional but highly recommended.

---

## Step 5 - Set Up the Python Environment

1. **Navigate to Application**

    Open the _New Terminal_ `` Ctrl+Shift+` `` and navigate Back-End application directory.

    ```bash
    cd app/back_end
    ```

> [!example]
> In terminal you should see something like this: `ubuntu_user@windows_user:/mnt/c/Users/YourUsername/Path/To/Project/app/back-end$`.

2. **Create a Python Virtual Environment**

    Run the following command to create _Python Virtual Environment_.

    ```bash
    python3 -m venv .venv
    ```

    Wait for virtual environment to be created.

3. **Activate Virtual Environment**

    Run the following command to activate _Python Virtual Environment_.

    ```bash
    source .venv/bin/activate
    ```

> [!tip]
> To deactivate the Python Virtual Environment, run `deactivate`.

4. **Install Python Dependencies**

    Run the following command to install _Python dependencies_.

    ```bash
    pip install -r requirements.txt
    ```

    Wait for the dependencies to be installed into virtual environment. To install additional development dependencies use the following command.

    ```bash
    pip install -r requirements_dev.txt
    ```

5. **Configure Python Interpreter**

    Open the _Command Palette_ `Ctrl+Shift+P`, type `>Python: Select Interpreter` and select the Python interpreter from your WSL virtual environment:
    - Select `Enter interpreter path...`.
    - Select `Find...`.
    - Open `/mnt/c/Users/YourUsername/Path/To/Project/app/back_end/.venv/bin/python3.12`.

---

## Step 6 - Test Redis

1. **Test Redis Connectivity**

    Run the following command.

    ```bash
    redis-cli
    ```

    Test the connectivity with the `ping` command.
    ```bash
    127.0.0.1:6379> ping
    PONG
    ```

> [!failure]
> If you get the response `Could not connect to Redis at 127.0.0.1:6379: Connection refused`, exit out of the connection and start the Redis server.
> ```bash
> sudo systemctl start redis
> ```
> Now test it again.

> [!tip]
> The following command will stop the Redis server.
> ```bash
> sudo systemctl stop redis
> ```

---

## Step 7 - Prepare Additional Data Sources

1. **Download FASTA File**

    Execute the following command into terminal.

    ```bash
    mkdir -p src/workspace/fasta && cd src/workspace/fasta && curl -O https://hgdownload.cse.ucsc.edu/goldenPath/hg38/bigZips/hg38.fa.gz && gunzip hg38.fa.gz && cd ../../..
    ```

    This will download the FASTA file "hg38.fa," which is required for _SpliceAI_ to function correctly.

2. **Download REVEL file**

    Execute the following command into terminal.

    ```bash
    mkdir -p src/workspace/revel && cd src/workspace/revel && curl -O https://rothsj06.dmz.hpc.mssm.edu/revel-v1.3_all_chromosomes.zip && unzip revel-v1.3_all_chromosomes.zip && cd ../.. && python3 scripts/revel.py workspace/revel/revel_with_transcript_ids workspace/revel/revel_with_transcript_ids.db && cd ..
    ```
    This will download "revel_with_transcript_ids" file that is required for correct work of REVEL. Python script will create database file for indexing REVEL values.

---

## Step 8 - Run the Flask Application

Start the development server with the following command.

```bash
gunicorn -c gunicorn_config.py run:app
```

> [!info]
> This will launch the Flask application on http://localhost:8080/. To stop the development server, simply press `Ctrl+C` in the VS Code terminal.

> [!success]
> Congratulations on starting the Back-End development server! This is a great step towards contributing to the Kath project. Happy coding and development! Remember to keep your code organized, break down tasks into manageable parts, and continuously test your code.

> [!question]
> If you encounter any issues or need guidance, feel free to reach out to your team lead!
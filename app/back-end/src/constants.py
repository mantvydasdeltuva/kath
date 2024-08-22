"""
This module defines key project paths and routes used across the application.

It sets up:
- The base directory of the project.
- Source directory path.
- Workspace directory paths, including a template directory.
- Base API route and specific routes for various functionalities.

These constants are typically used for file handling, directory management, and routing in the
Flask application.

Dependencies:
- os: Used for interacting with the operating system to manage file and directory paths.
"""

# pylint: disable=import-error

import os


# Project paths
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
SRC_DIR = os.path.join(BASE_DIR, "src")
WORKSPACE_DIR = os.path.join(SRC_DIR, "workspace")
WORKSPACE_TEMPLATE_DIR = os.path.join(WORKSPACE_DIR, "template")

# Routes
BASE_ROUTE = "/api/v1"
WORKSPACE_ROUTE = "/workspace"

# Events
CONSOLE_FEEDBACK_EVENT = "console_feedback"

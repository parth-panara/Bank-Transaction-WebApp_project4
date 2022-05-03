"""This test checks the Database, logs, and Uploads folder"""

import logging
import os
from pathlib import Path
from click.testing import CliRunner

from app import create_database
import logs
from app.db import config
runner = CliRunner()

# this test checks if the uploads folder is created for csv file#15
def test_create_uploads_folder():
    root = config.Config.BASE_DIR
    # set the name of the apps uploads folder for csv file
    uploadfolder = os.path.join(root, '..', config.Config.UPLOAD_FOLDER)
    # make a directory if it doesn't exist
    assert os.path.exists(uploadfolder) == True

# this test checks if the database directory is created#16
def test_create_database():
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../database')
    # make a directory if it doesn't exist
    assert os.path.exists(dbdir) == True

# this test checks if the database directory is created#18
def test_auto_creat_database():

    root = config.Config.BASE_DIR
    # set the name of the apps database directory
    dbdir = os.path.join(root,'..',config.Config.DB_DIR)
    # make a directory if it doesn't exist
    # make a directory if it doesn't exist
    assert os.path.exists(dbdir) == True


# Test to check if Logs folder is created#19
def test_create_log_folder():
    logdir = config.Config.LOG_DIR
    path = Path(logdir)

    if path.is_file():
        print(f'The file {logs} exists')
    else:
        print(f'The file {logs} does not exist')
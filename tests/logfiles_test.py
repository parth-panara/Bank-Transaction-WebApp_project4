"""This test the homepage"""

"""This test the all logfiles"""
import logging
import os


import app.config


#test to check if handler.log file exists#20
def test_logfile_handler():
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../logs/handler.log')
    assert os.path.exists(logfile) == True

#second way to check if handler.log file exists#20
def test_handler_logfile():
    log_dir = app.config.Config.LOG_DIR
    filepath = os.path.join(log_dir, "handler.log")
    assert os.path.isfile(filepath)


#test to check if myapp.log file exists#21

def test_logfile_myapp():
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../logs/myapp.log')
    assert os.path.exists(logfile) == True

#second way to check if myapp.log file exists#21
def test_myapp_logfile():
    log_dir = app.config.Config.LOG_DIR
    filepath = os.path.join(log_dir, "myapp.log")
    assert os.path.isfile(filepath)

#test to check if request.log file exists#22
def test_logfile_request():
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../logs/request.log')
    assert os.path.exists(logfile) == True



#second way to check if request.log file exists#22
def test_request_logfile():
    log_dir = app.config.Config.LOG_DIR
    filepath = os.path.join(log_dir, "request.log")
    assert os.path.isfile(filepath)








# test to check if the functions of logfiles are from 'init_py' is readable#20

def test_add_path_to_logfile():

    path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(path, '../app/logging_config/__init__.py')
    with open(filepath, encoding="utf-8") as file:
        data = {
            'file': filepath
            }
    assert os.path.isfile(filepath)
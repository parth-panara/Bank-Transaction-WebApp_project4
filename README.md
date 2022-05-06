# IS601 Project-4

[![Production Workflow 1](https://github.com/parth-panara/IS601_project-4_parth/actions/workflows/prod.yml/badge.svg)](https://github.com/parth-panara/IS601_project-4_parth/actions/workflows/prod.yml)


* [Production Deployment](https://parth-prod-project4.herokuapp.com/)


[![Development Workflow 3.8](https://github.com/parth-panara/IS601_project-4_parth/actions/workflows/dev.yml/badge.svg)](https://github.com/parth-panara/IS601_project-4_parth/actions/workflows/dev.yml)

* [Developmental Deployment](https://parth-dev-project4.herokuapp.com/)

## Project Description

This is Final Project 4 of IS 601. We need to make a website that allows a user to register, login, and upload the CSV file included with the project repository. The user transaction managment dashboard must display a table of transactions and it must display the current balance of the account based on the transactions.  The starting balance of the account is 0 and is determined by adding and subtracting debits and credits to the account that are identified as such in the CSV file.

Requirements:

1. A project must have a log file with an entry for each time a user uploads a CSV account transaction file.  
2. There must be a test to verify that the CSV file is uploaded and processed.
3. We must create a database record that is related to the user record for each transaction.
4. We must calculate a balance and have a test for this.
5. We must have a test for login, a test for registration, a test for accessing the dashboard as a logged-in user, and a test for denying access to the dashboard, and denying access to uploading the CSV file.
6. We will need to have our app work with a dev, prod, and testing configuration file to control the behavior of the program in different environments.

We must

A.  We need at least 25 unit tests, each unit test is worth 4 points.  There must be at least one test for each thing that the user does in the app.\
B.  We will need at least 25 commits (commit tests with their functional code in one commit)\
C.  Have the correct badge on our readme for the development and production workflows respectively\
D.  We must link to your project on Heroku for dev and production respectively\
E.  We must submit a link to your project on GitHub


## Key component of this projects:
* [Dockerfile](https://github.com/Milan-36/PythonFlaskWebsite/blob/master/app/Dockerfile), and [docker-compose](https://github.com/Milan-36/PythonFlaskWebsite/blob/master/docker-compose.yml)
* [app.py](https://github.com/Milan-36/PythonFlaskWebsite/blob/master/app/app.py)
* [Github](https://github.com/Milan-36/PythonFlaskWebsite)
* [PyCharm](https://www.jetbrains.com/pycharm/)
* [MySql](https://www.mysql.com/)
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [pytest](https://docs.pytest.org/en/7.1.x/)
* [WTForms](https://wtforms.readthedocs.io/en/3.0.x/)
* [Bootstrap](https://getbootstrap.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/)

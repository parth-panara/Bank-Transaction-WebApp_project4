"""This test the csv file procedure"""

from flask import Flask, current_app
from app import db
import os
from app.db.models import Transaction
from app.transactions import transactions_upload
from tests.transactions_test import test_user
import logging
from app import config
from app.db.models import User

import io
from sqlalchemy import func


#this test shows that user is logged in and able to read csv file in app#30

def test_file_uploads(application, test_user,):
    log = logging.getLogger("myApp")

    with application.app_context():
        assert db.session.query(User).count() == 1
        assert db.session.query(Transaction).count() == 0

    root = config.Config.BASE_DIR
    csv_file = 'transactions.csv'
    filepath = root + '/..app/uploads/' + csv_file


    uploadfolder = config.Config.UPLOAD_FOLDER
    file_upload = os.path.join(uploadfolder, csv_file)
    assert os.path.exists(file_upload) == True

    with application.test_client(test_user) as client:
        with open(file_upload, 'rb') as file:
            data = {
                'file': (file, csv_file),

                }
            resp = client.post('/transactions/upload',follow_redirects=True, data=data)

    assert resp.status_code == 200




# Test to check when access deny to user to the Transaction Management for csv file at dashboard#30

def test_access_transaction_manage_denied(client):
    response = client.get("/browse_transactions", follow_redirects=False)
    assert response.status_code == 404

# Test to check when access deny to user to upload the csv transactions file at dashboard#30

def test_upload_csvfile_access_denied(client):
    response = client.get("/upload", follow_redirects=False)
    assert response.status_code == 404

# Test to check for the logged in user csv file's columns works in the database and exists#32
def test_adding_one_user(application):
    # checks if my log works while we work with csv file
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0
        # showing how to add a record
        # create a record
        user = User('parth@webizly.com', 'testtest')
        # add it to get ready to be committed
        db.session.add(user)

        user = User.query.filter_by(email='parth@webizly.com').first()
        log.info(user)
        # asserting that the user retrieved is correct
        assert user.email == 'parth@webizly.com'
        # this is how we get a related record ready for insert
        user.transactions= [Transaction("-2324","DEBIT")]
        # commit is what saves the transactions
        db.session.commit()
        assert db.session.query(Transaction).count() == 1


# test ot check the log file in the folder and account balance function works#32
def test_uploaded_csv_balance(client, application,test_user):
    root = config.Config.BASE_DIR
    csv_file = 'transactions.csv'
    filepath = root + '/..app/uploads/' + csv_file



    uploadfolder = config.Config.UPLOAD_FOLDER
    file_upload = os.path.join(uploadfolder, csv_file)


    dire = os.path.join(os.getcwd(), 'uploads')
    with open(file_upload, encoding="utf-8") as f:
        file_content = f.read()

    # Post call after we have csv file in the app

    data = {
        'file': (io.BytesIO(file_content.encode()), csv_file)
    }
    response = client.post('/transactions/upload', data=data, follow_redirects=True)
    assert response.status_code == 200

    # test to checks if the function for current account balance works

    qry = db.session.query(func.sum(Transaction.amount)).group_by(Transaction.type).filter(Transaction.user_id).all()

    if qry:
        response = qry[0][0] + qry[1][0]
    assert response.status_code == 200









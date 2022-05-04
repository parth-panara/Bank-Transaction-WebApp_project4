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




#this test shows that user is logged in and able to read csv file in app#30

def test_file_uploads(application, test_user):
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

    with application.test_client() as client:
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



"""This test the authpages"""

from app.db import db
from app.db.models import User
import os
import io

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/register"' in response.data

# this test check if the if user is capable to register test#5

def test_register_user(client, application):
    response = client.post('/register', data={
        'email': 'parth@webizly.com',
        'password': '123456',
        'confirm': '123456'
    }, follow_redirects=True)
    assert response.status_code == 200


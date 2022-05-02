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
    assert b'href="/login"' in response.data

# this test check if the if user is capable to register test#5

def test_register_user(client, application):
    response = client.post('/register', data={
        'email': 'parth@webizly.com',
        'password': '123456',
        'confirm': '123456'
    }, follow_redirects=True)
    assert response.status_code == 200
    user = User.query.filter_by(email='parth@webizly.com').first()
    assert user is not None
    assert user.email == 'parth@webizly.com'


def test_user_login_post_registration(client):
    #this checks if after completing the registration user is allowed to log in test#6

    data = {
        'email' : 'parth@webizly.com',
        'password' : 'testtest'
    }
    resp = client.post('login', follow_redirects=True, data=data)
    assert resp.status_code == 200


#this checks if after completing the registration user is allowed to log in and entered to the dashboard test#8

def test_login_and_its_redirect_to_dashboard(client, application):
    # first register user before login
    response = client.post('/register', data={
        'email': 'parth@webizly.com',
        'password': 'testtest',
        'confirm': 'testtest'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == '/login'


    # now user will do login
    response = client.post('/login', data={
        'email': 'parth@webizly.com',
        'password': 'testtest',
    }, follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == '/dashboard'
    html = response.get_data(as_text=True)
    assert '<p>Welcome: parth@webizly.com!</p>' in html

    # user is entered on dashboard page
    response = client.get('/dashboard', follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == '/dashboard'
    html = response.get_data(as_text=True)
    assert '<p>Welcome: parth@webizly.com!</p>' in html


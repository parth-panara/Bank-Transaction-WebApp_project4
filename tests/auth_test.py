"""This test the authpages"""

from app.db import db
from app.db.models import User
import os
import io
from tests.transactions_test import test_user
from app import transactions

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

#user access deny to the dashboard test and get and error#9
def user_dashboard_access_deny(client):

    response = client.get("/dashboard")
    assert response.status_code == 403
    return client.get('/dashboard', follow_redirects=False)

#user access deny to the dashboard test and return to the login page#9

def test_deny_access_dashboard_page_without_login(client):
    response = client.get('/dashboard', follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == '/login'
    html = response.get_data(as_text=True)
    assert 'Please log in to access this page.' in html


#user logout test and able to redirect to login page test#10

def test_user_logout(client, application):
    """This tests the logout """
    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    assert b"<h2>Login</h2>" in response.data

#user logout failes and able to show error page test#10

def test_logout(client, application):
    """ GET to login """
    # pylint: disable=unused-argument,redefined-outer-name

    resp = client.get('/logout')

    # if login, redirect to index
    assert resp.status_code == 302


#user not eligible for logout without login test#10

def test_user_logout_fail_without_register(client, application):
    response = client.post('/logout', data={
        'email': 'mytest12@test12.com',
        'password': '12345678',
        'confirm': '12345678'
    }, follow_redirects=False)
    assert response.status_code == 405


#transactoion rout check if it shows the current balance#31
def test_upload_dashboard(application, test_user):
    """ test access to transactions when logged in """
    # pylint: disable=redefined-outer-name,unused-argument
    with application.test_client(test_user) as client:
        resp = client.get('/transactions')
    # check if successful at transaction dashboard
    assert resp.status_code == 200
    assert b'<h2>Browse: Transactions</h2>' in resp.data
    # check if it's able to show current account balance according to database



"""This test the homepage"""
from flask import Flask
import json

from app.auth import browse_users

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200

# user routes checked on profile edit test#11

def test_user_user_profile(client, application):
    response = client.post('/profile', data={
        'email': 'parth@webizly.com',
        'password': 'testtest',
        'confirm': 'testtest'
    }, follow_redirects=True)
    assert response.status_code == 200

# user routes checked on manage account where user can change password after login test#12

def test_user_manage_account(client, application):
    response = client.post('/account', data={
        'password': 'testtest12',
        'confirm': 'testtest12'
    }, follow_redirects=True)
    assert response.status_code == 200


# user management routes checked on manage test#13

def test_user_user_management(client):
    response = client.get('/users', follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == '/login'
    html = response.get_data(as_text=True)
    assert '<h2>Login</h2>' in html



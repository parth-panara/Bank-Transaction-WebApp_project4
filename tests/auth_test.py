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

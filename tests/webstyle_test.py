"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200


# test to check home page content#33
def test_request_index_content(client):

    response = client.get("/")
    assert b'<div class="d-flex flex-column align-items-stretch flex-shrink-0" style="width: 860px;">'in response.data
    assert b'<img src="/static/images/home.jpg"'in response.data

# test to check about page content#33
def test_request_about_content(client):
    response = client.get("/about")
    assert b'<h1>Transaction</h1>'in response.data
    assert b'<strong>T</strong>ransaction is considered to be one of the most reliable techniques within formal and'in response.data
    assert b'informal financial institutions.' in response.data
    assert b'electronic remittance transfer has become one of the most popular method of sending and receiving money' in response.data
    assert b'across the world.' in response.data
    assert b'<div class="d-flex flex-column align-items-stretch flex-shrink-0" style="width: 405px;">' in response.data
    assert b'<img src="/static/images/AboutPage_pic.jpg"' in response.data


# test to check welcome page content#33
def test_request_welcome_content(client):
    response = client.get("/welcome")
    assert b'<div class="d-flex flex-column align-items-stretch flex-shrink-0" style="width:1800px;">'in response.data
    assert b'<img src="/static/images/WelcomePic.jpg"'in response.data

# test to check register page content#33
def test_request_register_content(client):
    response = client.get("/register")
    assert b'Password Composition: To create strong Password you must include following'in response.data
    assert b'<li>Uppercase</li>'in response.data
    assert b'<li>Lowercase</li>'in response.data
    assert b'<li>Symbols (?#@...)</li>' in response.data
    assert b'<li>Numbers</li>' in response.data
    assert b'<img src="/static/images/RegisterPic.jpg"' in response.data

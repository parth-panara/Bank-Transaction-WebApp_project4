"""This test the homepage"""

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

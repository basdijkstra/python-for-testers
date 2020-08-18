import requests


def test_whether_im_ready():
    response = requests.get('http://jsonplaceholder.typicode.com/users/1')
    assert response.status_code == 200

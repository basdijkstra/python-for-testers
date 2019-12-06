import requests


def test_retrieve_token_then_use():
    response = requests.post("https://my.secure.api/token", auth=("username", "password"))
    response_body = response.json()
    token = response_body["token"]
    headers = {"Authorization", f"Bearer {token}"}
    new_response = requests.get("https://my.secure.api/secure/resource", headers=headers)
    assert new_response.status_code == 200


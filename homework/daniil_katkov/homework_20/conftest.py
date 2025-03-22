import requests
import pytest


@pytest.fixture(scope='session')
def start_complete():
    print('\nStart testing')
    yield
    print('Testing completed')


@pytest.fixture()
def before_after():
    print('before test')
    yield
    print('\nafter test')


@pytest.fixture()
def create_object_fixture():
    body = {
        "name": "C#",
        "data": {
            "book": "very long",
            "language": "very hard"
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    post_id = response.json()['id']
    print(post_id)
    yield post_id
    print('deleting the post')
    requests.delete(f'http://167.172.172.115:52353/object/{post_id}')

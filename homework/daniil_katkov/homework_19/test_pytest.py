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


@pytest.mark.parametrize('body', [
    {
        "name": "Python",
        "data": {
            "book": "long",
            "language": "easy"
        }
    },
    {
        "name": "Java",
        "data": {
            "book": "very long",
            "language": "hard"
        }
    },
    {
        "name": "JS",
        "data": {
            "book": "not long",
            "language": "not easy"
        }
    }
]
                         )
@pytest.mark.parametrize('headers', [{'Content-Type': 'application/json'}])
@pytest.mark.critical
def test_create_object(body, headers, start_complete, before_after):
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    assert response.json()['name'] == body["name"], f"Ожидаем: {body['name']}, получаем: {response.json()['name']}"


def test_put_object(create_object_fixture, before_after):
    body = {
        "name": "JS",
        "data": {
            "book": "long",
            "language": "not easy"
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.put(f'http://167.172.172.115:52353/object/{create_object_fixture}',
                            json=body, headers=headers)
    assert response.json()['name'] == "JS", 'Not JS'


def test_patch_object(create_object_fixture, before_after):
    body = {
        "name": "Python (basic)",
        "data": {
            "book": "not long"
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.put(f'http://167.172.172.115:52353/object/{create_object_fixture}',
                            json=body, headers=headers)
    assert response.json()['name'] == "Python (basic)", 'Not Python (basic)'


@pytest.mark.medium
def test_delete_object(create_object_fixture, before_after):
    response = requests.delete(f'http://167.172.172.115:52353/object/{create_object_fixture}')
    assert response.status_code == 200, 'No 200'

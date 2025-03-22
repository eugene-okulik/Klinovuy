import requests
import pytest
import allure


@allure.feature('Post')
@allure.story('Create post')
@allure.title('Создание нового поста')
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
    with allure.step('Send post request for creating a new post'):
        response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    with allure.step(f'Check that name is {body["name"]}'):
        assert response.json()['name'] == body["name"], f"Ожидаем: {body['name']}, получаем: {response.json()['name']}"


@allure.feature('Post')
@allure.story('Put post')
@allure.title('Обновление поста через метод PUT')
def test_put_object(create_object_fixture, before_after):
    with allure.step('Prepare test data'):
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
    with allure.step(f'Update post with id {create_object_fixture} via PUT method'):
        response = requests.put(f'http://167.172.172.115:52353/object/{create_object_fixture}',
                                json=body, headers=headers)
    with allure.step(f'Check that name is {body["name"]}'):
        assert response.json()['name'] == "JS", 'Not JS'


@allure.feature('Post')
@allure.story('Patch post')
@allure.title('Обновление поста через метод PATCH')
def test_patch_object(create_object_fixture, before_after):
    with allure.step('Prepare test data'):
        body = {
            "name": "Python (basic)",
            "data": {
                "book": "not long"
            }
        }
        headers = {
            'Content-Type': 'application/json'
        }
    with allure.step(f'Update post with id {create_object_fixture} via PATCH method'):
        response = requests.patch(f'http://167.172.172.115:52353/object/{create_object_fixture}',
                                  json=body, headers=headers)
    with allure.step(f'Check that name is {body["name"]}'):
        assert response.json()['name'] == "Python (basic)", 'Not Python (basic)'


@allure.feature('Post')
@allure.story('Delete post')
@allure.title('Удаление поста')
@pytest.mark.medium
def test_delete_object(create_object_fixture, before_after):
    with allure.step('Send delete request for deleting a new post'):
        response = requests.delete(f'http://167.172.172.115:52353/object/{create_object_fixture}')
    with allure.step('Check that status code is 200'):
        assert response.status_code == 200, 'No 200'

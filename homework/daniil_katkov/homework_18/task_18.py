import requests


# Тест на создание нового объекта
def create_object():
    body = {
        "name": "Python",
        "data": {
            "book": "long",
            "language": "easy"
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    assert response.json()['name'] == "Python", 'Not Python'


# Функция для создания нового объекта
def create_object_def():
    body = {
        "name": "Java",
        "data": {
            "book": "very long",
            "language": "hard"
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    return response.json()['id']


# Функция на удаление нового объекта
def remove(object_id):
    response = requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
    print(response.text)


# Тест на полное обновление нового объекта
def put_object():
    object_id = create_object_def()
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
    response = requests.put(f'http://167.172.172.115:52353/object/{object_id}', json=body, headers=headers)
    assert response.json()['name'] == "JS", 'Not JS'
    print(response.json())
    remove(object_id)


# Тест на частичное обновление нового объекта
def patch_object():
    object_id = create_object_def()
    body = {
        "name": "C#",
        "data": {
            "book": "long"
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.patch(f'http://167.172.172.115:52353/object/{object_id}', json=body, headers=headers)
    assert response.json()['name'] == "C#", 'Not C#'
    print(response.json())
    remove(object_id)


# Удаление нового объекта
def delete_object():
    object_id = create_object_def()
    response = requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
    assert response.status_code == 200, 'No 200'
    print(response.text)

import pytest
from test_api_daniil_katkov.my_endpoints.create_object import CreateObject
from test_api_daniil_katkov.my_endpoints.update_object import UpdateObject
from test_api_daniil_katkov.my_endpoints.delete_object import DeleteObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def object_id(create_object_endpoint):
    payload = {"name": "C#", "data": {"book": "very long", "language": "very hard"}}
    create_object_endpoint.create_new_object(payload)
    yield create_object_endpoint.object_id

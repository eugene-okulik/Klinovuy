import pytest


TEST_DATA = [
    {"name": "Python", "data": {"book": "long", "language": "easy"}},
    {"name": "Java", "data": {"book": "very long", "language": "hard"}},
    {"name": "JS", "data": {"book": "not long", "language": "not easy"}},
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_create_an_object(create_object_endpoint, data):
    create_object_endpoint.create_new_object(payload=data)
    create_object_endpoint.check_that_status_is_200()
    create_object_endpoint.check_response_name_is_correct(data['name'])


def test_put_an_object(update_object_endpoint, object_id):
    payload = {"name": "JS", "data": {"book": "long", "language": "not easy"}}
    update_object_endpoint.make_changes_in_object(object_id, payload)
    update_object_endpoint.check_that_status_is_200()
    update_object_endpoint.check_response_name_is_correct(payload['name'])


def test_patch_an_object(update_object_endpoint, object_id):
    payload = {"name": "Python (basic)", "data": {"book": "not long"}}
    update_object_endpoint.make_changes_in_object(object_id, payload)
    update_object_endpoint.check_that_status_is_200()
    update_object_endpoint.check_response_name_is_correct(payload['name'])


def test_delete_an_object(delete_object_endpoint, object_id):
    delete_object_endpoint.delete_new_object(object_id)
    delete_object_endpoint.check_that_status_is_200()

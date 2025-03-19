import requests
import allure
from test_api_daniil_katkov.my_endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):

    @allure.step('Update an object')
    def make_changes_in_object(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{object_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

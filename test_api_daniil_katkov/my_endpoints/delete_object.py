import requests
import allure
from test_api_daniil_katkov.my_endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):
    object_id = None

    @allure.step('Delete a new object')
    def delete_new_object(self, object_id):
        self.response = requests.delete(
            f'{self.url}/{object_id}'
        )
        return self.response

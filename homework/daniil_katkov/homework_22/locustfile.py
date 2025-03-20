from locust import task, HttpUser
import random

class MyObjects(HttpUser):
    object_id = None
    headers = {'Content-type': 'application/json'}
    test_data = [
        {"name": "Python", "data": {"book": "long", "language": "easy"}},
        {"name": "C#", "data": {"book": "very long", "language": "not easy"}},
        {"name": "C++", "data": {"book": "not long", "language": "not hard"}}
    ]

    @task
    def sequential_tasks(self):
        for element in self.test_data:
            response = self.client.post(
                '/object',
                json=element,
                headers=self.headers
            )
            self.object_id = response.json()['id']

            self.client.put(
                f'/object/{self.object_id}',
                json={"name": "JS", "data": {"book": "long", "language": "not easy"}},
                headers=self.headers
            )

            self.client.patch(
                f'/object/{self.object_id}',
                json={"name": "Python (basic)", "data": {"book": "not long"}},
                headers=self.headers
            )

            self.client.delete(
                f'/object/{self.object_id}'
            )

    @task
    def get_all_objects(self):
        self.client.get(
            '/object'
        )

    @task
    def get_one_object(self):
        self.client.get(
            f'/object/{random.choice([1, 1001, 1044, 1046, 1048, 1049])}'
        )

    def on_stop(self):
        if self.object_id:
            self.client.delete(
                f'/object/{self.object_id}'
            )

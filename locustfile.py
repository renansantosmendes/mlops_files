from locust import HttpUser, task, between


class ApiLoadRunner(HttpUser):
    """
    Sends a POST request to the '/predict' endpoint with a JSON payload.

    Args:
        self: The instance of the class.

    Returns:
        None
    """
    wait_time = between(min_wait=0.5, max_wait=2.5)

    @task
    def request(self):
        headers = {
            "Content-Type": "application/json"
        }
        request_body = {
            "accelerations": 0,
            "fetal_movement": 0,
            "uterine_contractions": 0,
            "severe_decelerations": 0
        }
        self.client.post('/predict', json=request_body, headers=headers)
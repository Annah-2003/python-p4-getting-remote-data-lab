import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)

# Example usage
if __name__ == "__main__":
    URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    requester = GetRequester(URL)
    response_body = requester.get_response_body()
    print(response_body)

    json_data = requester.load_json()
    print(json_data)

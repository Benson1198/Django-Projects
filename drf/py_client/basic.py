import requests

endpoint = "http://httpbin.org/status/200"
endpoint = "http://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(
    endpoint, params={'abs': 123}, json={'title': None, 'content': 'Hello World'})
print(get_response.json())

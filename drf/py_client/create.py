import requests


headers = {'Authorization': 'Bearer e54ebc8d3202b12a8c1a11281d3ed9e3de71e374'}
endpoint = "http://localhost:8000/api/products/"


data = {
    "title": "This field is done"
}
get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())

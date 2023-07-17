import requests

endpoint = "http://localhost:8000/api/products/184849827209/"

get_response = requests.get(endpoint)

print(get_response.json())

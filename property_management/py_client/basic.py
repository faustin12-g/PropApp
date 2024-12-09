import requests

endpoint = "http://localhost:8000/api"

# endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint)
print(get_response.json())
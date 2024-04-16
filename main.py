import requests

api_url = "http://shibe.online/api/shibes?count=10"
                                     
response = requests.get(api_url)

print(f"Response status code is:{response.status_code}")

response_json = response.json()

print(response_json)


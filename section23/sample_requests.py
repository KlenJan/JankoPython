import requests

response = requests.get("https://news.ycombinator.com/")
print(response.headers)
print(response.ok)
print(response.text)
print(response.status_code)

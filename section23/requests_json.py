import requests


url = "https://www.icanhazdadjoke.com"

# res = requests.get(url, headers={"Accept": "text/plain"})
res = requests.get(url, headers={"Accept": "application/JSON"})
# print(res.text)
res_json = res.json()
print(res_json["joke"])

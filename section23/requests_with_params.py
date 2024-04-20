import requests

url = "https://www.icanhazdadjoke.com/search"
term = "term=cat&limit=3"
headers = {"Accept": "application/json"}
params = {
    "term": "cat",
    "limit": "1",
}
res = requests.get(f"{url}?{term}")
print(res.text)

res = requests.get(url, headers=headers, params=params)
res_json = res.json()

print(tuple(x for x in res_json["results"]))

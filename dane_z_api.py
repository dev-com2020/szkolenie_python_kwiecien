import urllib.request

import requests
from bs4 import BeautifulSoup
import json

#
# slowo = "computer"
# res = requests.get("https://www.dictionary.com/browse/" + slowo)
# # print(res.url)
# # print(res.text)
#
# soup = BeautifulSoup(res.text, 'html.parser')
# desc = soup.find_all("meta")
# for tag in soup.find_all("meta"):
#     if tag.get("name") == "description":
#         print(tag.get("content"))

# param = {'miasto': 'Kielce', "kod": "25-900"}
# r = requests.get("https://httpbin.org/get", params=param)
# print(r.text)


# r = requests.get("https://api.github.com/user", auth=('login', 'haslo'))
# print(r.text)


# param = {'miasto': 'Kielce', "kod": "25-900"}
# r = requests.post("https://httpbin.org/post", data=param)
# print(r.text)

result = requests.get('https://jsonplaceholder.typicode.com/posts/100')
out = json.loads(result.text)
d = json.dumps(out["title"])
print(d)
# print(result.json())


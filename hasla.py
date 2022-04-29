import requests

s = requests.Session()
s.auth = ('user', 'psswd')

s.get('https://httpbin.org/basic-auth/user/psswd')


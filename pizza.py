import requests
from bs4 import BeautifulSoup
import re

# response = requests.get('https://httpbin.org/forms/post')
# page = BeautifulSoup(response.text, features="html.parser")
# form = page.find('form')
# print({field.get('name') for field in form.find_all(re.compile('input|textarea'))})

data = {'custname': "Szymon Obara", 'custtel': '123-456-789', 'custemail': 'szymon@obara.pl', 'size': 'small',
        'topping':
            ['bacon', 'onion'], 'delivery': '20:30', 'comments': ''}

response = requests.post('https://httpbin.org/post', data)
print(response.json())

import requests
from bs4 import BeautifulSoup

ip='183.246.196.78'
t_url = 'http://'+str(ip)
res = requests.get(t_url)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.title.text)
print(ip, 'is Up')
from bs4 import BeautifulSoup
import requests

url = input("enter url to get links: ")
web_page = requests.get(url)
#print(web_page.text)
soup = BeautifulSoup(web_page.text,'html.parser')
for link in soup.find_all('a'):
    ls = link.get('href')
    print(ls)

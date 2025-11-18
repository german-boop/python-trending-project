import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

titles = soup.find_all("a", class_="event-title")
for t in titles[:5]:
    print("-", t.get_text())

import httpx
from bs4 import BeautifulSoup
import json

url = "https://news.ycombinator.com/"

r = httpx.get(url)

soup = BeautifulSoup(r.text, "html.parser")

tds = soup.table.find_all("td", class_="title")

mydata = []

for i in tds[:-1]:
    hreflink = i.find("a")
    if hreflink is None:
        continue
    title = hreflink.string
    link = hreflink.get("href")
    mydata.append({"title": title, "link": link})


with open("./output/outputdata.json", "w") as j:
    json.dump(mydata, j, indent=4)

print("finished page 1")


for i in range(2, 11):
    r = httpx.get(f"{url}?p={i}")
    while r is None:
        r = httpx.get(f"{url}?p={i}")

    soup = BeautifulSoup(r.text, "html.parser")

    tds = soup.table.find_all("td", class_="title")

    mydata = []

    for k in tds[:-1]:
        hreflink = k.find("a")
        if hreflink is None:
            continue
        title = hreflink.string
        link = hreflink.get("href")
        mydata.append({"title": title, "link": link})


    with open(f"./output/outputdata{i}.json", "w") as j:
        json.dump(mydata, j, indent=4)

    print(f"finished page {i}")
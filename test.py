import httpx

r = httpx.get("https://news.ycombinator.com/")

with open("output/ycom1.html", "w") as fp:
    fp.write(r.text)

for i in range(2, 11):
    r = httpx.get(f"https://news.ycombinator.com/?p={i}")
    with open(f"output/ycom{i}.html", "w") as fp:
        fp.write(r.text)

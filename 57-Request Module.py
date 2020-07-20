import requests
r = requests.get("file:///D:/Data/Projects/HTML%20Projects/School%20project%20of%2010-D.html")
print(r.text)
print(r.status_code)

url = "www.something.com"
data = {"p1": 4, "p2": 8}

r1 = requests.post(url=url, data=data)

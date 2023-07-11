import requests

r=requests.get("https://www.facebook.com/")
print(r.text)
print(r.status_code)


# url="www.something.com"
# data={
#     "p1":4,
#     "p2":5
# }
#
# r2=requests.post(url=url,data=data)
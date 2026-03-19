import requests
r = requests.get("http://shopee.com.br/")
print(r.status_code)
print(r.headers)
print(r.content)
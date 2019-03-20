import requests

file = "C:/Users/asdim/Envs/python_four/four/static/img/kot_risunok.jpg"
url = "http://127.0.0.1:8000/drf/create"
data = {'name':'NewImg'}
f = {'foto':open(file, 'rb')}
rt = requests.post(url, files=f, data=data)
print(rt)
print(rt.text)

url = "http://127.0.0.1:8000/drf/all"
rt = requests.get(url)
print(rt)
print(rt.text)

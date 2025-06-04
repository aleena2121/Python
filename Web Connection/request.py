import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)


url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title":'foo',
    "body":'bar',
    "userId":1,
}

headers = {
    'Content-type': 'application/json; charset=UTF-8',
}

response = requests.post(url, headers=headers, json=data)

print(response.text)
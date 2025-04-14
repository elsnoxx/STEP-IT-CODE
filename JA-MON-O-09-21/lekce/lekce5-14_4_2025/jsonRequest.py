import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')

datas = response.json()

# print(data['title'])

for data in datas:
    print(f'Uzivatel {data["userId"]}, titulek je: {data['title']}')


payload = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}


# Odeslání POST požadavku
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)

# Získání odpovědi
print(response.status_code)
print(response.json())
    
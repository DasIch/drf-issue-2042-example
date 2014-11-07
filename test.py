import requests


s = requests.session()
response = s.post('http://localhost:8000/a', json={})
assert response.status_code == 201, response.status_code
id = response.json()['id']

response = s.post('http://localhost:8000/b', json={'a': id})
assert response.status_code == 201, response.status_code
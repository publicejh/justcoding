# 유튜브 4
import requests

headers = {}

access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQ5MjY4NDYyLCJqdGkiOiJjZjk0MjZmMTc4NjA0NTdjYmU2MGEzYjRmMGZiNTBkMiIsInVzZXJfaWQiOjF9.qS7IexN8CosPRgxAJgg6NJHVVZdmcg7KyGkLR9m9sZM'

headers['Authorization'] = 'Bearer ' + access_token
r = requests.get('http://127.0.0.1:8000/paradigms/', headers=headers)

print(r.text)

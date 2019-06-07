import requests

url = 'http://172.24.11.48.:32400/library/sections/2/all?X-Plex-Token=WgQ6JgEQeTShpPYCzgk1'
data = ''
response = requests.get(url, data=data)
print(response.text)

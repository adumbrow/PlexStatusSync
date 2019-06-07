import requests

url = 'http://172.24.11.48.:32400/?X-Plex-Token=WgQ6JgEQeTShpPYCzgk1'
response = requests.post(url, data=data)

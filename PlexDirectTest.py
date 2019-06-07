import requests

url = 'http://172.24.11.48.:32400/library/sections/29/all?X-Plex-Token=WgQ6JgEQeTShpPYCzgk1'
data = '''{
  "query": {
    "bool": {
      "must": [
        {
          "text": {
            "record.document": "SOME_JOURNAL"
          }
        },
        {
          "text": {
            "record.articleTitle": "farmers"
          }
        }
      ],
      "must_not": [],
      "should": []
    }
  },
  "from": 0,
  "size": 50,
  "sort": [],
  "facets": {}
}'''
response = requests.post(url, data=data)
print(response)

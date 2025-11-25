import requests 
song = input ("what song are you looking for ? ")
response = requests.get("http://itunes.apple.com/search?entity=song&limit=1&term=" + song)
# print (json.dumps(response.json(), indent = 2 ))

search = response.json()
for result in search ["results"]: 
    print (result["trackName"], "by", result["artistName"])
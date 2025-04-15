# itunes

import requests
import sys


if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())

# python comes with a library called json, to manipulate json data



import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# http request to 'itunes' server, browser equivalent 
print(json.dumps(response.json(), indent=2))

# alternatively, we can iterate through the results, which return a python dictionary
# printing only what we keys or values we are interested in 
o = response.json()
# .json() will give us specifically the json object from the servers response
for result in o["results"]:
    # we know the json object (dictionary in this case) has a key called 'results'
    print(result["trackName"])
    # we iterate through and print the track name, in this case 1 because we only request 1 per the URL
    


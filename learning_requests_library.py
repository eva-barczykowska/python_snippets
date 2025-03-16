import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(response.json())
# print(json.dumps(response.json(), indent=4))


response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

object = response.json()
for result in object["results"]:
    print(result["trackName"])
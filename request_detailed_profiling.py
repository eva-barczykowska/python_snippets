import cProfile
import requests

def fetch_url():
    requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=coldplay")

cProfile.run('fetch_url()')

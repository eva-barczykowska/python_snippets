import requests
import timeit

def fetch_url():
    requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=coldplay")

execution_time = timeit.timeit(fetch_url, number=100)
print(f"Average time per request: {execution_time / 100:.4f} seconds")

# Average time per request: 0.0629 seconds
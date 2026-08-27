import time
import warnings
warnings.filterwarnings("ignore")
import requests


def fetch_and_save_sync(user_id):
    print(f"Fetching user {user_id}...")
    # BLOCKS: Loop sits idle waiting for the internet
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    data = response.text

    print(f"Saving user {user_id}...")
    # BLOCKS: Loop sits idle waiting for the hard drive
    with open(f"user_{user_id}.json", "w") as f:
        f.write(data)


def main_sync():
    start = time.time()
    for user_id in range(1, 4):
        fetch_and_save_sync(user_id)
    print(time.time() - start)  # Takes ~3 to 4 seconds total

main_sync()
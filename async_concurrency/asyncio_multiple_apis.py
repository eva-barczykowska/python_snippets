# import asyncio
# import aiohttp
#
#
# async def fetch_data(session, url, api_key):
#     headers = {
#         'Authorization': f'Bearer {api_key}'
#     }
#     async with session.get(url, headers=headers) as response:
#         return await response.json()
#
#
# async def main():
#     urls = [
#         "https://api.weather.com/v1",  # Replace with real API URLs
#         "https://api.stockprices.com/v1",
#         "https://api.news.com/v1"
#     ]
#
#     api_key = ""  # Replace with your actual API key
#
#     async with aiohttp.ClientSession() as session:
#         tasks = [fetch_data(session, url, api_key) for url in urls]
#         results = await asyncio.gather(*tasks)  # Run all tasks concurrently
#         for result in results:
#             if result.startswith('Ruby'):
#             print(result)
#
#
# asyncio.run(main())

# the above didn't work because the actual API URLs and API keys are not provided.
# subscribed to the RapidAPI platform for a free API key.
# 2 ways to get the info, with http.client as first option:
# import http.client
#
# conn = http.client.HTTPSConnection("weatherapi-com.p.rapidapi.com")
#
# headers = {
#     'x-rapidapi-key': "b5fccb821cmsha40a5260de74a69p18212fjsnb5b962496059",
#     'x-rapidapi-host': "weatherapi-com.p.rapidapi.com"
# }
#
# conn.request("GET", "/current.json?q=53.1%2C-0.13", headers=headers)
#
# res = conn.getresponse()
# data = res.read()
#
# print(data.decode("utf-8"))
# local data gets printed

# another way with requests:
# import requests
#
# url = "https://weatherapi-com.p.rapidapi.com/current.json"
#
# querystring = {"q":"53.1,-0.13"}
#
# headers = {
# 	"x-rapidapi-key": "b5fccb821cmsha40a5260de74a69p18212fjsnb5b962496059",
# 	"x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())

# another API Linkedin
# import http.client
#
# conn = http.client.HTTPSConnection("linkedin-data-api.p.rapidapi.com")
#
# headers = {
#     'x-rapidapi-key': "b5fccb821cmsha40a5260de74a69p18212fjsnb5b962496059",
#     'x-rapidapi-host': "linkedin-data-api.p.rapidapi.com"
# }
#
# conn.request("GET", "/get-company-by-domain?domain=apple.com", headers=headers)
#
# res = conn.getresponse()
# data = res.read()
#
# print(data.decode("utf-8"))

# get jobs from LinkedIn if they have the words "Ruby" and "junior"
import http.client

conn = http.client.HTTPSConnection("linkedin-data-api.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "b5fccb821cmsha40a5260de74a69p18212fjsnb5b962496059",
    'x-rapidapi-host': "linkedin-data-api.p.rapidapi.com"
}

# Make the request to fetch jobs
conn.request("GET", "/search-jobs", headers=headers)

res = conn.getresponse()
data = res.read()

# Print the raw response to inspect its structure
print("Raw response data:")
print(data.decode("utf-8"))

# didn't work, was returning  1 irrelevant result then exceeded monthly plan

import requests
import influxdb

# import requests
#
# url = "http://localhost:8086/api/v2/query"
# headers = {
#     "Authorization": "Token Z3IZe_8g1KuNuebccwn2QYyLBqHsasH2ULeq65uL3SFiEvoGvhUZssbe_GUedwUpktJdu0z-KoQz_uSydIx66w==",
#     "Content-Type": "application/vnd.flux"
# }
# query = """
# from(bucket: "my_bucket")
#   |> range(start: -1h)
# """
# params = {
#     "org": "my_org"
# }
# response = requests.post(url, headers=headers, params=params, data=query)
# print(response.text)



import requests

url = "http://localhost:8086/api/v2/query"
headers = {
    "Authorization": "Token Z3IZe_8g1KuNuebccwn2QYyLBqHsasH2ULeq65uL3SFiEvoGvhUZssbe_GUedwUpktJdu0z-KoQz_uSydIx66w==",
    "Content-Type": "application/vnd.flux"
}
query = """
from(bucket: "my_bucket")
  |> range(start: -1h)
"""
params = {
    "org": "my_org"
}
response = requests.post(url, headers=headers, params=params, data=query)

# Print raw response content
print("Response Status Code:", response.status_code)
# print("Response Text:", response.text)
print("Response Text:", response.content)

# Try to parse JSON
try:
    response_json = response.json()
    print("Response JSON:", response_json)
except requests.exceptions.JSONDecodeError:
    print("Failed to decode JSON. Response might not be JSON formatted.")

import http.client

# Instantiate a connection to the server (example: 'www.example.com')
conn = http.client.HTTPSConnection("www.example.com")

# Define the path of the resource you are requesting
url_path = "/"

# Send a GET request
conn.request("GET", url_path)

# Get the response
response = conn.getresponse()

# Print the status and reason
print(f"Status: {response.status}, Reason: {response.reason}")

# Read the response data
data = response.read()

# Print the response content
print(data.decode('utf-8'))

# Close the connection
conn.close()
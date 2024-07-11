import requests

url = "ANY_IMAGE_LINK"

response = requests.get(url)

with open ("image.jpg", "wb") as file:
    file.write(response.content)

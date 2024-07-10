import requests

api_key = "7ce2552ba0704fb19975b4c33863a065"
url = "https://newsapi.org/v2/everything?q=tesla&" \
       "from=2024-06-08&sortBy=publishedAt&apiKey=" \
       "7ce2552ba0704fb19975b4c33863a065"

request = requests.get(url)
content = request.json()
test = request.text

print(content)
print(type(content))
print(type(request))
print(type(test))
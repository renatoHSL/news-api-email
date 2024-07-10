import requests

api_key = "7ce2552ba0704fb19975b4c33863a065"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-06-10&sortBy=publishedAt&apiKey=" \
      "7ce2552ba0704fb19975b4c33863a065"

request = requests.get(url)
content = request.json()


for article in content["articles"]:
    print(article["title"])
    print(article['description'])




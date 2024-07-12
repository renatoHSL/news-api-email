import requests
from send_email import send_email

topic = "tesla"

api_key = "YOUR_API_HERE"
url = "https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
       "from=2024-07-10&" \
       "sortBy=publishedAt&" \
       "apiKey=7ce2552ba0704fb19975b4c33863a065&" \
       "language=en"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = "Subject: Today's news" \
                + body + article["title"] + "\n" \
                + article["description"] \
                + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)

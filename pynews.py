# google news - api key
import requests
import time

def pynewsindia():
    main_url = "http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=########"
    open_google_page = requests.get(main_url).json()
    articles = open_google_page["articles"]

    result = []

    for a in articles:
        result.append(a["title"])

    for i in range(10):
        time.sleep(5)
        Headline = i+1, result[i]
        print(Headline)

pynewsindia()

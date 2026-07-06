from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/news")
def get_news(page: int = 1, limit: int = 5):
    # both are query params with defaults — caller can do /news?page=2&limit=10
    # page = which "page" of results to return, limit = how many items per page
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    # fetch raw HTML of Hacker News homepage
    soup = BeautifulSoup(response.text, "html.parser")
    # parse it into a searchable structure

    titles = []
    # will hold every headline text scraped from the page

    for item in soup.find_all("span", class_="titleline"):
        # find every <span class="titleline"> on the page — this wraps each headline
        titles.append(item.text)
        # .text pulls the visible headline text out and adds it to the list

        #Pagination Logic
        start = (page - 1) * limit
        end = start + limit
        # calculates which slice of 'titles' to return based on page/limit
        # e.g. page=1,limit=5 → start=0,end=5 (items 0-4)
        # page=2,limit=5 → start=5,end=10 (items 5-9)

    return {"page": page,
            "limit": limit,
            "total": len(titles),
            "data": titles[start:end]
            # slices the full scraped list down to just this "page" of results
            }
#Crawling with Python Code
#import requests
#from bs4 import BeautifulSoup

#url = "https://www.example.com"
#response = requests.get(url)
#soup = BeautifulSoup(response.text, "html.parser")
#print(soup.title.text)
# ^ plain-Python version: fetch raw HTML, parse it, grab the <title> tag text


from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
# BeautifulSoup ("bs4") = library that parses raw HTML into a searchable structure,
# so you can find specific tags/classes instead of regex-ing through text

app = FastAPI()

@app.get("/crawl")
def crawl_website():
    # 'url' as a query param — intended to let caller choose which site to crawl
    url = "https://indianexpress.com/"

    response = requests.get(url)
    # fetch the raw HTML of the page (just text, not yet structured)

    soup = BeautifulSoup(response.text, "html.parser")
    # parse that raw HTML into a navigable structure you can search through
    title= []
    # list to collect scraped items (named 'title' but really holds headline texts)

    for item in soup.find_all("a",class_="topBlockNews__sidebarLink"):
        # find_all() = find every tag matching these conditions (here: every <a> tag
        # with this specific CSS class) — returns a list of matches, not just one
        title.append(item.get_text())
        # get_text() = strips out the HTML tags, keeps just the visible text

    return{"news": title}
    # send back the scraped headlines as JSON
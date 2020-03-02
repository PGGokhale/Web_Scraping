from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.parse
import requests
import pandas as pd

BASE_URL = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
FILE = "html-selenium.txt"
FILE_WAIT = "html-selenium-wait.txt"
FILE_JPL = "html-selenium-jpl.txt"

def fetch_mars_news():

    # first try
    driver = webdriver.Firefox()
    driver.get(BASE_URL)
    html = driver.page_source
    with open(FILE, "w+", encoding="utf-8") as f:
        f.write(html)

    # second try
    driver.get(BASE_URL)
    driver.implicitly_wait(10)
    html = driver.page_source
    driver.close()
    with open(FILE_WAIT, "w+", encoding="utf-8") as f:
        f.write(html)

    soup = BeautifulSoup(html, "html.parser")
    title_div_class = "image_and_description_container"
    div_tags = soup.find_all("div", class_=title_div_class)
    # print(div_tags)
    results = [
        {
            "name": div_tag.a.text,
            "url": urllib.parse.urljoin("https://mars.nasa.gov/", div_tag.a["href"]),
        }
        for div_tag in div_tags
    ]

    
    JPL_URL = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    response = requests.get(JPL_URL)

    html1 = response.text

    soup1 = BeautifulSoup(html1, "html.parser")
    title_a_class = "button fancybox"
    div_tag = soup1.find("a", class_=title_a_class)
    info = div_tag["data-fancybox-href"]

    featured_image_url = urllib.parse.urljoin("https://www.jpl.nasa.gov", div_tag["data-fancybox-href"])
    dict_news = {"News": results[0]["name"], "Featured_img":featured_image_url }

    return(dict_news)


from bs4 import BeautifulSoup
import requests
from pprint import pprint

WEATHER_URL = "https://twitter.com/marswxreport?lang=en"

def fetch_mars_weather():

    response = requests.get(WEATHER_URL)

    soup = BeautifulSoup(response.text, 'lxml')

    tweets_list = list()
    tweets = soup.find_all("li", {"data-item-type": "tweet"})

    tweet_text_box = tweets[0].find("p", {"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
    weather_text = tweet_text_box.a
    weather_text.clear()
    mars_weather = weather_text.parent.text
    mars_weather = mars_weather.replace('\n', ' ')
    mars_weather = mars_weather.replace('\'', '')
    dict_weather = {"weather": mars_weather}
    return(dict_weather)




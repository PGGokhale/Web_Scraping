from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from bs4 import SoupStrainer
import re
import pandas as pd
from pprint import pprint

HEMISPHERE_URL = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"


def fetch_hemi_pics():

    only_a_tags = SoupStrainer("a")
    response = requests.get(HEMISPHERE_URL)
    soup = BeautifulSoup(response.text, 'lxml')
    hemisphere_dict = dict()
    list_of_dict = []



    tweets = soup.find_all("h3")
    for item in tweets:
        text = item.text
        text = text.replace(' Enhanced', '')
        list_of_dict.append({"title": text})

   

    driver = webdriver.Firefox()
    driver.get(HEMISPHERE_URL)
    html = driver.page_source
    driver.close()

    list_of_links =[]

    for link in BeautifulSoup(html, "html.parser", parse_only=only_a_tags):
        if link.has_attr('href'):
            list_of_links.append(link['href'])

    link_list =[]
    names = ["cerberus_enhanced", "schiaparelli_enhanced", "syrtis_major_enhanced","valles_marineris_enhanced" ]
    for i in range(len(list_of_links)):
        list_of_links[i].replace(' Enhanced', '')
        for name in names:
            if name in list_of_links[i]:
                link_list.append(list_of_links[i])

    res = [] 
    for i in link_list: 
        if i not in res: 
            res.append(i) 

    for i in range(4):
        list_of_dict[i].update({"img_url": f"https://astrogeology.usgs.gov{res[i]}"})

    list_of_dict
    for i in range(4):
        response = requests.get(list_of_dict[i]["img_url"])
        soup = BeautifulSoup(response.text, 'lxml')
        img_urls_tags = soup.find_all("div", class_="downloads")
        #print(img_urls_tags)
        for tag in img_urls_tags:
            #print(tag.li.a)
            list_of_dict[i].update({"img_url_hd":tag.li.a['href']})

    return(list_of_dict)


            


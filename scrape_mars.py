from mars_news import fetch_mars_news
from mars_weather import fetch_mars_weather 
from mars_facts import fetch_mars_facts
from mars_hemisphere import fetch_hemi_pics 





def scrape():
    dict_mars = {}
    dict_mars.update({"Mars_News" : fetch_mars_news()})
    dict_mars.update(fetch_mars_weather())
    dict_mars.update({"Mars_facts":fetch_mars_facts()})
    dict_mars.update({"Mars_Img":fetch_hemi_pics()})

    return(dict_mars)






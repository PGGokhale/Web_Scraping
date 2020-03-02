import pandas as pd
from pprint import pprint

FACTS_URL = "http://space-facts.com/mars/"

def fetch_mars_facts():

    data_list = pd.read_html(FACTS_URL,attrs={'id': 'tablepress-p-mars-no-2'})
    list1 = data_list[0]

    df = pd.DataFrame(list1)
    df = df.set_index(0)
    return(df.to_dict()[1])


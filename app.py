from flask import Flask, render_template
from scrape_mars import scrape
import pandas as pd
import pymongo
from pprint import pprint

# Create an instance of our Flask app.
app = Flask(__name__)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.mars_db


# Set route
@app.route('/')
def index():
    db.mars.drop()
    dict_scrape = scrape()
    db.mars.insert_one(dict_scrape)
    # Store the entire team collection in a list
    data_set = list(db.mars.find())
    data = data_set[0]
    news = data["Mars_News"]["News"]
    features_image = data["Mars_News"]["Featured_img"]
    
    weather = data["weather"]
    df = pd.DataFrame.from_dict({"Mars_facts":data["Mars_facts"]})
    facts_table = df.to_html()
    


    cerberus = {"img":data["Mars_Img"][0]["img_url_hd"], "title":data["Mars_Img"][0]["title"]}
    schiaparelli = {"img":data["Mars_Img"][1]["img_url_hd"], "title":data["Mars_Img"][1]["title"]}
    Syrtis = {"img":data["Mars_Img"][2]["img_url_hd"], "title":data["Mars_Img"][2]["title"]}
    Valles = {"img":data["Mars_Img"][3]["img_url_hd"], "title":data["Mars_Img"][3]["title"]}


    # Return the template with the teams list passed in
    return render_template('index.html', 
    news=news, 
    weather=weather, 
    features_image=features_image, 
    facts_table=facts_table, 
    cerberus=cerberus,
    schiaparelli=schiaparelli,
    Syrtis=Syrtis,
    Valles=Valles)


if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pandas as pd
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
#db = mongo.db


@app.route("/")
def home():
    mars = mongo.db.mars.find_one()
    print(mars)
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    # Run the scrape function
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_info()

    mars.update_one({}, {"$set": mars_data}, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
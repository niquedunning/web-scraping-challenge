from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create connection variable
app = Flask(__name__)


mongo = PyMongo(app, uri="mongodb://localhost:27017/space_db.mars")


@app.route('/')
def home():
    
    mars_scrape = mongo.db.mars_scrape.find_one()

    return render_template('index.html', mars_scrape=mars_scrape)

@app.route("/scrape")
def scrape():
    
    mars_scrape = scrape_mars.scrape()
    
    mongo.db.mars_scrape.update({}, mars_scrape, upsert=True)
    
    return redirect('/', code=302)


if __name__ == "__main__":
    app.run(debug=True)

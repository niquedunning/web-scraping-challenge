from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

# Create connection variable
app = Flask(__name__)


conn = "mongodb://localhost:27017/space_db.mars"
client = pymongo.MongoClient(conn)


@app.route('/')
def home():
    
    mars_scrape = client.db.mars_scrape.find_one()

    return render_template('index.html', mars_scrape=mars_scrape)

@app.route("/scrape")
def scrape():
    
    mars_scrape = client.db.mars_scrape.find_one()
    mars_data = scrape_mars.scrape()
    mars_scrape.update({}, mars_data, upsert=True)
    return redirect('/', code=302)


if __name__ == "__main__":
    app.run(debug=True)

Mission to Mars
Built a web app that scraped info from various websites on the planet of Mars. This info included general headlines, photos, and weather data about the red planet.


Step 1 - Scraping
The initial scraping processwas performed in Juptyer notebook. This was completed by using PANDAS, BEAUTIFUL SOUP, PYMONGO, AND REQUESTS/SPLINTERS.

NASA Mars News
Scraped the latest headlines from the Mars Nasa website.

JPL Mars Space Images - Scraped the URL for the featured image on the Mars JPL website.
Mars Facts
Visited the Mars Facts webpage here scraped weather data from a table on the website.
After, used pandas to convert it into an HTML string.
Mars Hemispheres
Visited the USGS Astrogeology site to gather high resolution photos of Mar's hemispheres. 

Step 2 - MongoDB and Flask Application
Used MongoDB with Flask templating to create a new HTML page that presents all the data scraped in the previous exercise.

Created a route called /scrape that imported scrape_mars.py script and called the scrape function.

Sent the returned info to MongoDB as a Python dictionary and stored it there.

Created a root route / that allows visitor to query the MongoDB and pass the data into an HTML page to display the data.

Created a HTML page that takes the data and displays all of it in a presentable fashion.
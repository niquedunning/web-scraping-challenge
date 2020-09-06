from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
from webdriver_manager.chrome import ChromeDriverManager


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)
def scrape():
    browser = init_browser()

    mn_url = 'https://mars.nasa.gov/news/'
    browser.visit(mn_url)
    html = browser.html
    mn_soup = BeautifulSoup(html, 'html.parser')
    # Retrieve the latest news title and paragraph
    news_title = mn_soup.find_all('div', class_='content_title')[0].text
    news_paragraph = mn_soup.find_all('div', class_='article_teaser_body')[0].text

    jpl_url = 'https://www.jpl.nasa.gov'
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)
    html = browser.html
    image_soup = BeautifulSoup(html, 'html.parser')
    image_path = image_soup.find_all('img')[3]["src"]
    featured_img_url = jpl_url + image_path

    url1 = "https://space-facts.com/mars/"
    tables = pd.read_html(url1)
    marsdf = tables[1]
    marsdf.columns = [
    'Mars - Earth Comparison','Mars', 'Earth']
    html_table = marsdf.to_html()

    astro_url = "https://astrogeology.usgs.gov"
    hem_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hem_url)
    hem_html = browser.html
    hem_soup = BeautifulSoup(hem_html, 'html.parser')
    all_images = hem_soup.find('div', class_='collapsible results')
    mars_hem = all_images.find_all('div', class_='item')
    hem_pic_url = []
    for x in mars_hem:
    # Collect Title
        hem = x.find('div', class_="description")
        title = hem.h3.text
        
        # Collect image link by browsing to hemisphere page
        hem_link = hem.a["href"]    
        browser.visit(astro_url + hem_link)
        
        pic_html = browser.html
        pic_soup = BeautifulSoup(pic_html, 'html.parser')
        
        pic_link = pic_soup.find('div', class_='downloads')
        pic_url = pic_link.find('li').a['href']

        # Create Dictionary to store title and url info
        hem_dict = {}
        hem_dict['title'] = title
        hem_dict['img_url'] = pic_url
        
        hem_pic_url.append(hem_dict)

    mars_dictionary = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image_url": featured_img_url,
        "fact_table": str(html_table),
        "hemisphere_images": hem_pic_url
    }

    return mars_dictionary
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time


def scrape_info():
# Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Scrape the Mars News Site
    url = "https://redplanetscience.com/"
    browser.visit(url)

    # Create html and tie to BeautifulSoup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Find Title 
    news_title = soup.find('div', class_="content_title").text
    news_title

    # Find Paragraph Text
    news_p = soup.find('div', class_="article_teaser_body").text
    news_p

    # MARS Image Scraping
    # Pull Image

    # Scrape the Mars Image Site
    img_url = "https://spaceimages-mars.com/"
    browser.visit(img_url)

    time.sleep(1)
    browser.links.find_by_partial_text('FULL IMAGE').click()

    # Find Image
    # Create HTML object
    featured_pg = browser.html
    # Create BeautifulSoup object and parse with HTML parser
    img_soup = BeautifulSoup(featured_pg, "html.parser")

    # Get featured image url
    featured_img = img_soup.find("img", class_="fancybox-image")
    featured_img_url =featured_img["src"]
    print(featured_img_url)

    featured_img_url = ("https://spaceimages-mars.com/" + featured_img_url)
    featured_img_url

    browser.quit()

    #MARS Facts Table Pull
    #Pull table
    import pandas as pd

    url = 'https://galaxyfacts-mars.com'
    tables = pd.read_html(url)
    tables

    df = tables[0]
    df.columns = ['Details','Mars', 'Earth']
    df.set_index('Details', inplace=True)
    print(df)
    df_html = df.to_html()
    print(df_html)
    #MARS Hemispheres Img Scraping

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Scrape the Mars Image Site
    hem_url = 'https://marshemispheres.com/'
    browser.visit(hem_url)

    hem_imgs_html = browser.html
    hem_soup = BeautifulSoup(hem_imgs_html, 'html.parser')

    # Article Titles
    hem_titles = hem_soup.find_all('h3')
    hem_titles

    hemisphere_image_urls = []
    hemisphere_dicts = {"title": [] , "img_url": []}

    for titles in hem_titles[0:4]:

        title = titles.text
        
        # Scrape the Mars Image Site
        img_url = "https://marshemispheres.com/"
        browser.visit(img_url)
        
        browser.links.find_by_partial_text(title).click()
        browser.links.find_by_partial_text("Sample").click()
        
        # Create HTML and tie to BeautifulSoup
        img_html = browser.html

        # Create BeautifulSoup object and parse with HTML parser
        img_soup = BeautifulSoup(img_html, "html.parser")
        
        featured_img = img_soup.find("div", class_ = "downloads").find("ul").find("li").find("a")["href"]
        featured_img = ("https://marshemispheres.com/" + featured_img)
        
        
        hemisphere_dicts = {"title": title, "img_url": featured_img}
        hemisphere_image_urls.append(hemisphere_dicts)

    mars = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_img_url": featured_img_url,
        "hemisphere_image_urls":hemisphere_image_urls,
        "df_html":df_html
    }

    browser.quit()



    return mars
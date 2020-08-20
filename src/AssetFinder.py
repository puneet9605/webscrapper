from bs4 import BeautifulSoup
import requests
from requests.exceptions import MissingSchema
import traceback


def fetch(url: str) -> dict:
    """
    Fucntion takes in a url and returns a dict containing with 2 keys
    - assets - an list of urls present in the <img> tags on the page
    - links - an list of urls present in the <a> tags on the page
    Args:
        url: URL of the page to scrape for links

    Returns:

    """
    # todo handle request status codes
    # only process requests with response 200
    asset = {'assets': list(), 'links': list()}
    try:
        htmlbody = requests.get(url).text
    except MissingSchema as ex:
        print(traceback.format_exc())
        return asset

    soup = BeautifulSoup(htmlbody, 'lxml')
    # getting all the img tags
    imgtags = soup.find_all('img')
    # creating a set of src from the img tags
    imgurls = {imgtag.get('src') for imgtag in imgtags}
    # getting all the a tags
    atags = soup.find_all('a')
    # creating a set of links from the atags
    # todo change logic to add the base url to relative links
    aurll = {atag.get('href') for atag in atags if atag.get('href') and atag.get('href').startswith('http')}
    asset = {'assets': list(imgurls), 'links': list(aurll)}
    return asset


def getWebsiteAssets(url: str) -> list:
    """
    function that returns list of image urls
    Args:
        url:

    Returns:
        list of image urls

    """
    # todo add logic to control depth
    # todo try to implement this using recursion
    # todo convert the image relative url to full urls

    urls = set()
    imgurls = set()
    result = fetch(url)
    urls.update(result['links'])
    imgurls.update(result['assets'])
    # lopping through all the links and adding them to the list
    # using set to remove duplicates
    for link in result['links']:
        page = fetch(link)
        imgurls.update(page['assets'])
        print(imgurls)
        temp = set()
        temp.update(page['links'])
        new_urls = urls - temp
        urls.update(new_urls)
        result['links'].extend(new_urls)
        len(result['links'])
    return imgurls



if __name__ == '__main__':
    #fetch('https://google.com')
    getWebsiteAssets('www.udemy.com/')
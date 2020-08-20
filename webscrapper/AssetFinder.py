from bs4 import BeautifulSoup
import requests
from requests.exceptions import MissingSchema
import traceback
from urllib.parse import urlparse


def fetch(url: str) -> dict:
    """
    Fucntion takes in a url and returns a dict containing with 2 keys
    - assets - an list of urls present in the <img> tags on the page
    - links - an list of urls present in the <a> tags on the page
    Args:
        url: URL of the page to scrape for links

    Returns:

    """
    # todo handle request status code only process requests with response 200
    asset = {'assets': list(), 'links': list()}
    parse_url = urlparse(url)
    base_url = parse_url[0]+'://'+parse_url[1]
    try:
        res = requests.get(url)
        res.raise_for_status()
        htmlbody = requests.get(url).text
    except requests.exceptions.HTTPError as err:
        return asset
    except requests.ConnectionError as ex:
        print("url is not present on the internet :)")
        return asset
    except MissingSchema as ex:
        print(traceback.format_exc())
        return asset

    soup = BeautifulSoup(htmlbody, 'lxml')
    # getting all the img tags
    imgtags = soup.find_all('img')
    # creating a set of src from the img tags
    imgurls = {imgtag.get('src') if imgtag.get('src').startswith('http')
               else base_url+imgtag.get('src')for imgtag in
               imgtags}
    # getting all the a tags
    atags = soup.find_all('a')
    # creating a set of links from the atags
    aurll = set()
    for atag in atags:
        if atag.get('href'):
            if atag.get('href').startswith('http'):
                aurll.add(atag.get('href'))
            else:
                aurll.add(base_url + atag.get('href'))
    asset = {'assets': list(imgurls), 'links': list(aurll)}
    return asset

def getWebsiteAssets(url: str, url_count: int = -1) -> list:
    """
    function that returns list of image urls
    Args:
        url: url of the website to grab data from
        count(optional): the number of urls we want to hit, useful when testing to make sure it takes too much time to run

    Returns:
        list of image urls

    """
    # todo add logic to control depth
    # todo try to implement this using recursion
    urls = set()
    imgurls = set()
    result = fetch(url)
    urls.update(result['links'])
    imgurls.update(result['assets'])
    # lopping through all the links and adding them to the list
    # using set to remove duplicates
    for link in result['links']:
        if url_count == 0:
            break
        page = fetch(link)
        imgurls.update(page['assets'])
        temp = set()
        temp.update(page['links'])
        new_urls = urls - temp
        urls.update(new_urls)
        result['links'].extend(new_urls)
        url_count -= 1
    return list(imgurls)

if __name__ == '__main__':
    fetch('http://www.udemy.com/')
    #getWebsiteAssets('http://www.udemy.com/', 3)
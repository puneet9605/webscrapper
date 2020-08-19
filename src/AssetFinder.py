from bs4 import BeautifulSoup
import requests


def fetch(url: str) -> dict:
    """
    Fucntion takes in a url and returns a dict containing with 2 keys
    - assets - an list of urls present in the <img> tags on the page
    - links - an list of urls present in the <a> tags on the page
    Args:
        url: URL of the page to scrape for links

    Returns:

    """
    htmlbody = requests.get(url).text
    soup = BeautifulSoup(htmlbody, 'lxml')
    # getting all the img tags
    imgtags = soup.find_all('img')
    # creating a list of src from the img tags
    imgurls = [imgtag['src'] for imgtag in imgtags]
    # getting all the a tags
    atags = soup.find_all('a')
    # creating a list of links from the atags
    aurll = [atag['href'] for atag in atags]
    asset = {'assets': imgurls, 'links': aurll}
    return asset


if __name__=='__main__':
    fetch('https://google.com')
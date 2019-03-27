from bs4 import BeautifulSoup
import requests


def scrape_budim():
    session = requests.Session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"}
    url = 'https://www.budimex-nieruchomosci.pl/'
    content = session.get(url, verify=False).content

    soup = BeautifulSoup(content, "lxml")
    posts = soup.find_all("div", {"class": "inwestycja miasta jeden", })  # returns a list

    urls = []
    image_srcs = []
    titles = []

    for element in posts:
        investment_title = element.find("div", {"class": "metka-tytul"}).text
        titles.append(investment_title)
        i_url = element.find("a")["href"]
        urls.append(i_url)
        i_img = element.find("img")["src"]
        image_srcs.append(i_img)

    return zip(urls, image_srcs, titles)

x = {"class": "c-offertiles__item js-invest to-show", }
def scrape_dd():
    session = requests.Session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"}
    url = 'https://www.domd.pl/inwestycje/'
    content = session.get(url, verify=False).content

    soup = BeautifulSoup(content, "lxml")
    posts = soup.find_all("div", {"data-id"})  # returns a list
    print(posts)
    urls = []
    image_srcs = []
    titles = []

    for element in posts:
        investment_title = element.find("p", {"class": "desc-lead"}).text
        titles.append(investment_title)
        i_url = element.find("a")["href"]
        urls.append(i_url)
        i_img = element.find("img")["src"]
        image_srcs.append(i_img)

    return zip(urls, image_srcs, titles)


from bs4 import BeautifulSoup
import requests
import re


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


def scrape_dd():
    session = requests.Session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"}
    url = 'https://www.domd.pl/inwestycje/'
    content = session.get(url, verify=False).content

    soup = BeautifulSoup(content, "lxml")
    posts = soup.find_all("div", {"class": "c-offertiles__item js-invest"})  # returns a list
    # print(posts)
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


def scrape_victoria():
    session = requests.Session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"}
    url = 'http://www.victoriadom.pl/'
    content = session.get(url, verify=False).content

    soup = BeautifulSoup(content, "lxml")
    posts = soup.find_all("a", {"class": "banner--header js-animate col-lg-4 col-xl-3 col-md-6 new"})  # returns a list
    # print(posts)
    urls = []
    image_srcs = []
    titles = []

    for element in posts:
        investment_title = element.find("h2", {"class": "banner__heading playfair"}).text
        titles.append(investment_title)
        i_url = element["href"]
        urls.append(i_url)
        i_img = element.find("div")["style"]
        img_url_extracted = re.findall("http.*[)]", i_img)
        image_srcs.append(img_url_extracted)
    print(image_srcs)
    print(titles)
    print(urls)
    return zip(urls, image_srcs, titles)

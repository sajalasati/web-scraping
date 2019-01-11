from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

import csv

filename = "in_bestseller.csv"
f = open(filename, "w")

headers = "Name,URL,Author,Price,Number of Ratings,Average Rating\n"
f.write(headers)

for page_number in range(1, 6):

    my_url = "https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_" + \
        str(page_number) + "?ie=UTF8&pg=" + str(page_number)
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # html parsing
    page_soup = soup(page_html, "html.parser")
    # to grab each product
    containers = page_soup.findAll("div", {"class": "zg_itemWrapper"})

    for container in containers:
        book_name = container.div.a.div.img["alt"]
        url_name = "https://www.amazon.in" + container.div.a["href"]
        if container.findAll(
            "div", {
                "class": "a-row a-size-small"})[0].a is None:
            author = container.findAll(
                "div", {"class": "a-row a-size-small"})[0].span.text
        else:
            author = container.findAll(
                "div", {"class": "a-row a-size-small"})[0].a.text
        try:
            price = container.findAll(
                "span", {"class": "p13n-sc-price"})[0].text.strip()
        except BaseException:
            price = "Not available"

        number_of_ratings = container.findAll(
            "a", {"class": "a-size-small a-link-normal"})[0].text
        average_rating = container.findAll(
            "span", {"class": "a-icon-alt"})[0].text
        f.write(
            book_name.replace(
                ",",
                "").strip() +
            ";" +
            url_name +
            ";" +
            author.replace(
                ",",
                "").strip() +
            ";" +
            price.replace(
                ",",
                "").strip() +
            ";" +
            number_of_ratings.replace(
                    ",",
                    "") +
            ";" +
            average_rating.replace(
                ",",
                "").strip() +
            ";\n")

f.close()

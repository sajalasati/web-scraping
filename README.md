# Python Web Scraping

## Introduction

This is a python script to scrape the details about top 100 bestseller books on amazon.com and amazon.in. This code has been written using Python and BeautifulSoup. The corresponding python scripts for the two websites have been named accordingly.

Details of the data fetched include Name, url, author, price, number of ratings and average rating of the book. Output will be stored in a palin text file in csv format in the current directory.

Important to note that the code has been tested on **ONLY** Linux-based OSs, and _may not_ work on Windows.

## Running the program

- Run the following code on terminal
  - `pip3 install beautifulsoup4`
  - `pip3 install requests`
- Execute the code by using `python3 com_bestseller.py` and `python3 in_bestseller.py` in the current directory.

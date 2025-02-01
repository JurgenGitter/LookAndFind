import requests
import html
from bs4 import BeautifulSoup


def get_data(tags, url, wordsgohere):

    page = requests.get(url) #Get html page

    if page.ok: # Check the page was returned ok
        soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup
        links = soup.select(tags) # filter on tags

        f = open(wordsgohere + ".txt", 'w') # Open/create file in write mode

        for link in links:
            f.write(link.text + '\n')
            #f.write(link.text.upper() + '\n')
            #f.write(link.text.lower() + '\n') Both lines were used for generating wordlists prior

        f.close() # close our file handle
    else:
        print("Error: Could not retrieve page")

tags = input("Please enter the location of within the webpage in which your data lays using html tags EX: (table tbody tr td a): ")
url = input("Please enter the url: ")
wordsgohere = input("Please enter the name of the file to be created for data storage: ")

url.encode()

get_data(tags, url, wordsgohere)

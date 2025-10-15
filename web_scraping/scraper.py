import requests
from bs4 import BeautifulSoup
import csv

URL = "https://quotes.toscrape.com/"

response = requests.get(URL)

# Status codes and their meanings
"""
200 -> OK
400 -> Bad request
404 -> Not found
500 -> Internal server error
"""

# print(response.status_code)  # 200 -> OK

if response.status_code == 200:
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    title = soup.find("title")
    quotes = soup.find_all("span", class_="text")  # ["abc", "bcd"]
    authors = soup.find_all("small", class_="author")  # ["xyz", "pqr"]

    # for quote in quotes:
    #     print(quote.text)

    # for author in authors:
    #     print(author.text)

    # for index in range(len(quotes)):
    #     quote = quotes[index].text
    #     author = authors[index].text

    #     print(quote, "written by", author)
    quotes_and_authors_list = []
    for quote, author in zip(quotes, authors):
        row = (quote.text, author.text)
        quotes_and_authors_list.append(row)

    with open("quotes.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author"])
        writer.writerows(quotes_and_authors_list)


else:
    print("Error")

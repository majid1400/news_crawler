"""title"""

"""imports"""
import requests
from bs4 import BeautifulSoup

URl = "https://www.farsnews.ir/news/14010204000332/%D9%87%D8%B4%D8%AF%D8%A7%D8%B1-%D8%A8%D8%A7%D9%86%DA%A9-%D9%85%D8%B1%DA%A9%D8%B2%DB%8C-%D8%A2%D9%84%D9%85%D8%A7%D9%86-%D8%A8%D9%87-%D8%B1%DA%A9%D9%88%D8%AF-%D8%A8%DB%8C-%D8%B3%D8%A7%D8%A8%D9%82%D9%87-%D8%A8%D8%A7-%D8%A7%D8%B9%D9%85%D8%A7%D9%84-%D8%AA%D8%AD%D8%B1%DB%8C%D9%85-%DA%AF%D8%A7%D8%B2%DB%8C-%D8%B9%D9%84%DB%8C%D9%87-%D8%B1%D9%88%D8%B3%DB%8C%D9%87"
page = requests.get(URl)

soup = BeautifulSoup(page.content, "html.parser")


"""functions"""


def get_title():
    results = soup.find(class_="title mb-2 d-block text-justify")
    print(results.text.strip())


"""*********************************"""
get_title()

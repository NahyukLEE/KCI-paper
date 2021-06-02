from selenium import webdriver
from bs4 import BeautifulSoup as soups


def search_selenium(search_name, search_path, search_limit):
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"

    browser = webdriver.Chrome('chromedriver.exe')
    browser.get(search_url)

    image_count = len(browser.find_elements_by_tag_name("img"))

    print("Number you will load images : ", image_count)

    browser.implicitly_wait(2)

    for i in range(search_limit):
        image = browser.find_elements_by_tag_name("img")[i]
        image.screenshot("imgfile/comfort/" + str(i) + ".png")

    browser.close()


if __name__ == "__main__":
    search_name = input("Search Keyword : ")
    search_limit = int(input("Num : "))
    search_path = "Your Path"
    # search_maybe(search_name, search_limit, search_path)
    search_selenium(search_name, search_path, search_limit)

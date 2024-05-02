import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string


# Check if the webdriver is installed and install it if it is not
# try:
#     print(webdriver.__version__)
# except AttributeError:
#     print("Installing webdriver")
#
#     # Install the webdriver
#     os.system("pip install selenium")

# Create options that store the user's profile
options = webdriver.EdgeOptions()
options.add_argument("--user-data-dir={}".format(os.getcwd() + r".\profile"))

# Create the webdriver with the options
driver = webdriver.Edge(options=options)
driver.get("https://www.bing.com/?FORM=Z9FD1")


def random_word(size: int = 5) -> str:
    """
    Generate a random word with a given size
    :param size: parameter that defines the size of the word
    :return: a random word
    """
    return "".join(random.choices(string.ascii_lowercase, k=size))


def search_bing(query: str) -> None:
    """
    Search for a query in Bing
    :param query: the query to be searched
    :return: None
    """
    search_box = driver.find_element(By.ID, "sb_form_q")
    search_box.send_keys(query)
    search_box.submit()


# create a loop that searches for random words 10 times
for _ in range(1):
    search_bing(random_word())
    time.sleep(1)

driver.quit()

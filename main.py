from pprint import pprint
from time import sleep
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

FORM_URL = "https://forms.gle/4AM7KNvr7nr9toqC6"
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(ZILLOW_URL)

soup = BeautifulSoup(response.content, "html.parser")

all_links = soup.find_all(name='a', attrs={"class": "StyledPropertyCardDataArea-anchor"})
links = []

for link_tag in all_links:
    links.append(link_tag.get("href"))

# pprint(links)

all_prices = soup.find_all(name='span', attrs={"class": "PropertyCardWrapper__StyledPriceLine"})
prices = []

for price_tag in all_prices:
    prices.append(price_tag.getText().replace("/mo", "").split("+")[0])

# pprint(prices)

all_addresses = soup.find_all(name="address")
addresses = []

for address_tag in all_addresses:
    addresses.append(address_tag.getText().replace("\n                                  ", "")
                     .replace("\n                                ", ""))

# pprint(addresses)

all_houses = [addresses, prices, links]
pprint(all_houses)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(FORM_URL)

for i in range(len(all_houses[0])):
    i += 0
    sleep(2)
    address_textbox = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/"
                                                          "div[1]/div/div[1]/input")
    address_textbox.send_keys(all_houses[0][i])

    price_textbox = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/"
                                                        "div[1]/div/div[1]/input")
    price_textbox.send_keys(all_houses[1][i])

    link_textbox = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/d"
                                                       "iv[1]/div/div[1]/input")
    link_textbox.send_keys(all_houses[2][i])

    # sleep(5) # Slow down to clicking submit button to check items typed
    submit_button = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span")
    submit_button.click()

    sleep(2)
    # send_another_link_text = driver.find_element(By.LINK_TEXT, value="Başka bir yanıt gönder")
    # send_another_link_text.click()

    send_another = driver.find_element(By.CLASS_NAME, value="Uc2NEf a")
    send_another.click()
# script to scrape concert info from setlist.fm

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# testing purposes, might keep for demo purposes
import time

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# open a website in a tab
driver.get("https://www.setlist.fm/")

if not (driver.title == "setlist.fm - the setlist wiki"):
    print("ERROR: Site was not loaded properly.")
    exit()

search = driver.find_element_by_id("id6")
# TODO: GUI input
search.send_keys("babymetal")
search.send_keys(Keys.RETURN)

# search and wait for the page to load results
try:
    results = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".row.contentBox.visiblePrint"))
    )
    print(results.text)
except:
    print("ERROR: Results were not loaded properly.")
    driver.quit()


time.sleep(5)

driver.quit()

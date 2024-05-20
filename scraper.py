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
ARTIST = "babymetal"
search.send_keys(ARTIST)
search.send_keys(Keys.RETURN)

# search and wait for the page to load results
try:
    contents = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".row.contentBox.visiblePrint"))
    )
    # print(contents.text)
except:
    print("ERROR: Results were not loaded properly.")
    driver.quit()

results = contents.find_elements(By.CSS_SELECTOR, ".col-xs-12.setlistPreview")

# print(results)

show = {}

# parse thru each result and store info in a list
for result in results:
    condensedDateBlock = result.find_element(By.CSS_SELECTOR, ".condensed.dateBlock").text
    month = result.find_element(By.CSS_SELECTOR, ".month").text
    day = result.find_element(By.CSS_SELECTOR, ".day").text
    year = result.find_element(By.CSS_SELECTOR, ".year").text
    date = (month, day, year)
    showName = result.find_element(By.TAG_NAME, "h2").find_element(By.TAG_NAME, "a").text
    details = result.find_element(By.CSS_SELECTOR, ".details").text
    setTimes = result.find_element(By.CSS_SELECTOR, ".setlistPreviewSetTimes").text
    setSummary = result.find_element(By.CSS_SELECTOR, ".setSummary").text
    for info in date:
        print(info, end=" ")
    print(showName)
    print(details)
    print(setTimes)
    print(setSummary)
    print("-------------")

# time.sleep(5)

driver.quit()

# script to scrape concert info from setlist.fm

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re


# testing purposes, might keep for demo purposes
import time

# TODO: pass in argument from gui for artist input
def getWriteShows():
    PATH = "C:\\Program Files (x86)\\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    # open a website in a tab
    driver.get("https://www.setlist.fm/")

    if driver.title != "setlist.fm - the setlist wiki":
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
    # probably a way to handle exceptions or store error msgs better 
    except:
        print("ERROR: Results were not loaded properly.")
        driver.quit()

    results = contents.find_elements(By.CSS_SELECTOR, ".col-xs-12.setlistPreview")

    shows = []

    # parse thru each result and store info in a list
    for result in results:
        condensedDateBlock = result.find_element(By.CSS_SELECTOR, ".condensed.dateBlock").text
        month = result.find_element(By.CSS_SELECTOR, ".month").text
        day = result.find_element(By.CSS_SELECTOR, ".day").text
        year = result.find_element(By.CSS_SELECTOR, ".year").text
        date = (month, day, year)
        dateStr = ', '.join(date)
        showName = result.find_element(By.TAG_NAME, "h2").find_element(By.TAG_NAME, "a").text
        details = result.find_element(By.CSS_SELECTOR, ".details").text
        setTimes = result.find_element(By.CSS_SELECTOR, ".setlistPreviewSetTimes").text
        setSummary = result.find_element(By.CSS_SELECTOR, ".setSummary").text

        # check for valid characters
        curList = [dateStr, showName, details, setTimes, setSummary]
        for listIndex, item in enumerate(curList):
            for itemIndex, string in enumerate(item):
                maybeBadStr = re.sub('[ -~]', '', string)
                if (maybeBadStr != ""):
                    newString = string.replace(maybeBadStr, "-")
                    curList[listIndex][itemIndex].replace(curList[listIndex][itemIndex], newString)

        shows.append(curList)

    driver.quit()

    # write the info to a csv file
    headers = ['Show date', 'Show name', 'Show details', 'Set times', 'Set summary']
    
    with open('concerts.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(headers)
        for show in shows:
            writer.writerow(show)
    print("Successfully wrote to concerts.csv")

getWriteShows()
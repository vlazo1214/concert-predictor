# script to scrape concert info

from selenium import webdriver


PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# open a website in a tab
driver.get("https://www.setlist.fm/")

if not (driver.title == "setlist.fm - the setlist wiki"):
    print("ERROR: Site was not loaded properly.")
    exit()




driver.quit()

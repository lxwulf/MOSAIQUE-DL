import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#------------------------------------------------
#settings for driver

chromeOptions = webdriver.ChromeOptions()
chromeOptions.binary_location = r"/usr/bin/brave-browser-nightly"
chromeOptions.add_argument('headless')
chromeOptions.add_argument('window-size=1200x600')

driverselector = './drivers/chromedriver'
browser = webdriver.Chrome(driverselector, options=chromeOptions)

#------------------------------------------------
#list

linklist = [
   'https://store.steampowered.com/points/shop/app/1192640',
   'https://store.steampowered.com/points/shop/app/1299120',
   'https://store.steampowered.com/points/shop/app/1385730',
   'https://store.steampowered.com/points/shop/app/1504020'
]

#------------------------------------------------
#vardb

test_screenshot = browser.save_screenshot('./test.png')

web_item = "/html/body/div[1]/div[7]/div[4]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/img"


#------------------------------------------------
#script

for items in linklist:
  browser.get((len(linklist)))
  time.sleep(6)
  browser.find_elements_by_xpath(web_item)
  print(items)

browser.quit()
"""
find_class = browser.find_elements_by_xpath('/html/body/div[1]/div[7]/div[4]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div/div[2]/img')
#browser.save_screenshot('./test.png')

print(find_class)

find_class.get_attribute('src')

browser.quit()

linklist
-----------------------------------------------------------
linkstorage = [
   "https://store.steampowered.com/points/shop/app/1192640",
   "https://store.steampowered.com/points/shop/app/1299120",
   "https://store.steampowered.com/points/shop/app/1385730",
   "https://store.steampowered.com/points/shop/app/1504020"
]

url = 'https://store.steampowered.com/points/shop/app/1192640'

url1 = 'https://store.steampowered.com/points/shop/app/1192640/cluster/1'


"""
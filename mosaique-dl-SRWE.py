import os
import time
import pretty_errors
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#------------------------------------------------
#settings for chromium driver

dlc = {"download.default_directory" : "./DLC", "savebrowsing.enabled" : "false"}
chromeOptions = webdriver.ChromeOptions()
chromeOptions.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser-Nightly\Application\brave.exe"
chromeOptions.add_argument('headless')
chromeOptions.add_argument('window-size=1920x1080')
chromeOptions.add_argument('disable-extensions')
chromeOptions.add_experimental_option('prefs', dlc)
chromeOptions.add_experimental_option('excludeSwitches',['enable-logging'])
#chromeOptions.add_argument('test-type')

driverselector = './drivers/chromedriver.exe'
browser = webdriver.Chrome(driverselector, options=chromeOptions)

#------------------------------------------------
#working list

linkdb = [
   'https://store.steampowered.com/points/shop/app/1192640',
   'https://store.steampowered.com/points/shop/app/1299120',
   'https://store.steampowered.com/points/shop/app/1385730',
   'https://store.steampowered.com/points/shop/app/1504020'
]

#------------------------------------------------
#code

for links in linkdb:
   getlinks = browser.get(links)
   browser.implicitly_wait(1)
   ani_av = browser.find_elements_by_class_name('rewarditem_ImageAnimatedAvatar_2YbSw')
   for items in ani_av:
      print(items.get_attribute('src'), file=open('output.txt', 'a'))
      file = open('output.txt', 'r')
file.close()
#os.remove("output.txt")
browser.quit()
import time
import wget
import pretty_errors
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#------------------------------------------------
#settings for driver

dlc = {"download.default_directory" : "./DLC", "savebrowsing.enabled" : "false"}
chromeOptions = webdriver.ChromeOptions()
chromeOptions = webdriver.ChromeOptions()
chromeOptions.binary_location = r"/usr/bin/brave-browser-nightly"
chromeOptions.add_argument('headleass')
chromeOptions.add_argument('window-size=1920x1080')
chromeOptions.add_argument('disable-extensions')
chromeOptions.add_experimental_option('prefs', dlc)
chromeOptions.add_experimental_option('excludeSwitches',['enable-logging'])
#chromeOptions.add_argument('test-type')

driverselector = './drivers/chromedriver'
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
    print(items.get_attribut('src'), file=open('output.txt', 'a'))
browser.quit()

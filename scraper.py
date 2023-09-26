from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from settings import CHROMEDRIVER_PATH, WIKIPEDIA_URL

service = Service(executable_path=CHROMEDRIVER_PATH)

driver = webdriver.Chrome(service=service)
driver.get(WIKIPEDIA_URL)

TFA_CSS_LOCATOR = 'div#mp-tfa'
ITN_CSS_LOCATOR = 'div#mp-itn'
DYK_CSS_LOCATOR = 'div#mp-dyk'
OTD_CSS_LOCATOR = 'div#mp-otd'

locator_list = [TFA_CSS_LOCATOR, ITN_CSS_LOCATOR, DYK_CSS_LOCATOR, OTD_CSS_LOCATOR]
link_dictionary = {}
for locator in locator_list:
    div_element = driver.find_element(By.CSS_SELECTOR, locator)
    info_list = []
    for link in div_element.find_elements(By.TAG_NAME, 'a'):
        info_dict = {
            'title': link.get_attribute('title'),
            'text': link.text,
            'href': link.get_attribute('href')}
        info_list.append(info_dict)
    link_dictionary[locator] = info_list
print(link_dictionary)
for key, value in link_dictionary.items():
    print(f'{key} --- {len(value)} links')
driver.quit()
#this program initializes the tables to be run on day 1
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import constants
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import sys




web = 'https://www.amazon.in'
driver_path = 'D:/Chrome/chromedriver' #change this to the path on your system

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
w = WebDriverWait(driver, 3)
new_page = []

driver.get(web)

driver.implicitly_wait(5)

keyword = "Samsung"

search = driver.find_element(By.XPATH, '//*[(@id = "twotabsearchtextbox")]')
search.send_keys(keyword)

search_button = driver.find_element(By.ID, 'nav-search-submit-button')
search_button.click()


driver.implicitly_wait(5)

# products = [my_elem.text for my_elem in driver.find_elements
# (By.XPATH, '//*[(@class = "a-size-medium a-color-base a-text-normal")]')]

# for i in range(19):
#     new_page.append([my_elem.text for my_elem in w.until(driver.find_elements(By.XPATH, '//*[(@class = "a-size-medium a-color-base a-text-normal")]'))])
#     next_page = driver.find_element(By.XPATH, '//*[(@class = "s-pagination-item s-pagination-next s-pagination-button s-pagination-separator")]')
#     next_page.click()

for i in range(19):
    new_page.append([my_elem.text for my_elem in w.until(EC.presence_of_all_elements_located((By.XPATH, '//*[(@class = "a-size-medium a-color-base a-text-normal")]')))])
    driver.implicitly_wait(5)
    next_page = driver.find_element(By.XPATH, '//*[(@class = "s-pagination-item s-pagination-next s-pagination-button s-pagination-separator")]')
    next_page.click()

# print(new_page)
#writing initial database as a spreadsheet
print(sys.getsizeof(new_page), sys.getsizeof(new_page) )
# arr = np.array(new_page, dtype=object)
# new_page_flat = arr.reshape(-1)
# df = pd.DataFrame(new_page_flat, columns=['Products'])
# df.to_excel(excel_writer = constants.path)
#
# driver.quit()
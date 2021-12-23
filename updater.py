#this program can be run everyday to check for new products and updating
import pandas as pd
import constants
from selenium import webdriver
from selenium.webdriver.common.by import By


web = 'https://www.amazon.in'
driver_path = 'D:/Chrome/chromedriver'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get(web)

driver.implicitly_wait(5)

keyword = "Samsung"

search = driver.find_element(By.XPATH, '//*[(@id = "twotabsearchtextbox")]')
search.send_keys(keyword)

search_button = driver.find_element(By.ID, 'nav-search-submit-button')
search_button.click()


driver.implicitly_wait(5)

new_products = [my_elem.text for my_elem in driver.find_elements(By.XPATH, '//*[(@class = "a-size-medium a-color-base a-text-normal")]')]

df2 = pd.DataFrame(new_products, columns=['Products'])
df2.to_excel(excel_writer = constants.path2)


column = ['Products']
df1 = pd.read_excel(constants.path, usecols=['Products'])
df1_lower = df1['Products'].str.lower()
df1_snake = df1_lower.str.replace(' ', '_')
print()

df2 = pd.read_excel(constants.path2, usecols=['Products'])
df2_lower = df2['Products'].str.lower()
df2_snake = df2_lower.str.replace(' ', '_')




for i in range (len(df1)):
    if df1_snake[i] not in df2_snake.unique():
        print(f"{df1.iloc[i]['Products']} is removed")

for i in range (len(df2)):

    if df2_snake[i] not in df1_snake.unique():
        print(f"New Product {df2.iloc[i]['Products']} is added")
    else:
        print(f"New Product {df2.iloc[i]['Products']} is already present in our table")

print("Updating tables for the day")

df = pd.DataFrame(new_products, columns=['Products'])
df.to_excel(excel_writer = constants.path)

print("Tables are now updated")

driver.quit()






import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Initialize the driver
driver = webdriver.Chrome()

#Go to URL:
driver.get("https://www.scrapingcourse.com/infinite-scrolling")
driver.maximize_window()

#Infinite scroll
"""
Logic: 
1) store initial scroll height in a variable
2) in a loop add the following till the condition of loop becomes false:
    - scroll to the bottom of the page
    - wait for page to load
    - store the height of the current scroll into a new variable
    - check the initial height vs new scroll, if same then break the loop because you have reached the end of the page
    - else , initial height = new height
"""
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if last_height == new_height:
        break
    last_height = new_height

time.sleep(5)

#Fetch data after infinite scroll
product_count = driver.find_elements(By.CSS_SELECTOR, ".product-item")
pp = pprint.PrettyPrinter(indent=3)
count=0
for product in product_count:
    product_details = {
        "Image URL": product.find_element(By.CSS_SELECTOR, ".product-image").get_attribute('src'),
        "Product title": product.find_element(By.CSS_SELECTOR , ".product-name").text,
        "Price": product.find_element(By.CSS_SELECTOR, ".product-price").text
    }
    pp.pprint(product_details)
    count+=1
print("Count of products: ", count)

#close driver:
driver.quit()


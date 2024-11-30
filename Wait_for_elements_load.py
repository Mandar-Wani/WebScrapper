import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.scrapingcourse.com/javascript-rendering")

#goal is to wait for all elements to load then scrape all items and print them

element_visibility = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-grid")))

product_details = driver.find_elements(By.CSS_SELECTOR, ".product-item")

pp = pprint.PrettyPrinter(indent=3)
for product in product_details:
    product_info = {
        "Name" : product.find_element(By.CSS_SELECTOR, ".product-name").text,
        "Price": product.find_element(By.CSS_SELECTOR, ".product-price").text
    }
    pp.pprint(product_info)

driver.quit()
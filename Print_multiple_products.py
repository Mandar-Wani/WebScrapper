#Coupling multiple projects into one(extract multiple product data of a ecommerce website then add it to a CSV file)
import csv
import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By

#initialize the driver in headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

#go to URL
driver.get("https://www.scrapingcourse.com/ecommerce/")

#extract all product details and store it in an array
extracted_data = []

#Loop through the products
products = driver.find_elements(By.CSS_SELECTOR, ".product")
for product in products:
    product_details = {"Image URL": product.find_element(By.CSS_SELECTOR, ".attachment-woocommerce_thumbnail").get_attribute("src"),
                       "Product title": product.find_element(By.CSS_SELECTOR, ".product-name").text,
                       "Price": product.find_element(By.CSS_SELECTOR, ".product-price").text}
    extracted_data.append(product_details)

#pretty print the array
pp=pprint.PrettyPrinter(indent=3)
pp.pprint(extracted_data)

#csv file name:
csv_file ="product.csv"

#add data to csv file
with open(csv_file,mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Image URL","Product title","Price"])
    writer.writeheader()
    writer.writerows(extracted_data)
print(f"Data has been writen to {csv_file}")

#drive close
driver.quit()
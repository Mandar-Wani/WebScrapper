from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.scrapingcourse.com/login")

#login and logout

#login:
email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "password")
email.send_keys("admin@example.com")
password.send_keys("password")

login_button = driver.find_element(By.CSS_SELECTOR, ".btn.submit-btn")
login_button.click()

#logout
logout_button = driver.find_element(By.CSS_SELECTOR, ".text-blue-500")
logout_button.click()

#driver close
driver.quit()

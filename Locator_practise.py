import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")

#clicking the alt tab
all_tab = driver.find_element(By.ID , "nav-hamburger-menu")
all_tab.click()
time.sleep(3)

#clicking the mens fashion tab:
mens_fashion = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT , "Men\'s Fashion")))
mens_fashion.click()
time.sleep(3)

#clicking watches:
#in_mens_fashion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li/a[contains(text(), \'T-shirts & Polos\')]")))
in_mens_fashion = driver.find_element(By.XPATH, "//li/a[contains(text(), 'T-shirts & Polos')]")
driver.execute_script('arguments[0].click()', in_mens_fashion)
time.sleep(2)

driver.quit()


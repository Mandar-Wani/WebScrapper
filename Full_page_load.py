from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()

driver.get("https://www.scrapingcourse.com/javascript-rendering")
try:
    WebDriverWait(driver, 10).until(
        lambda driver : driver.execute_script("return document.readystate") == "complete"
    )
except Exception as e:
    print(f"Exception occured: {e}")
finally:
    driver.quit()

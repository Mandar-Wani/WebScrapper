#import libraries
import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By

#initialize headless operations
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options,)

#navigate to the website
driver.get("https://www.scrapingcourse.com/ecommerce/")

#Find element:
"""
product: <li> tag and class = "product type-product post-246 status-publish first outofstock product_cat-hoodies-sweatshirts has-post-thumbnail shipping-taxable purchasable product-type-variable"
image: <a href="https://www.scrapingcourse.com/ecommerce/product/abominable-hoodie/" class="woocommerce-LoopProduct-link woocommerce-loop-product__link"><img width="1274" height="1580" src="https://www.scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh09-blue_main.jpg" class="attachment-woocommerce_thumbnail product-image size-woocommerce_thumbnail product-image" alt="" decoding="async" fetchpriority="high" srcset="https://www.scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh09-blue_main.jpg 1274w, https://www.scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh09-blue_main-242x300.jpg 242w, https://www.scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh09-blue_main-826x1024.jpg 826w, https://www.scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh09-blue_main-768x952.jpg 768w, https://www.scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh09-blue_main-1239x1536.jpg 1239w, https://www.scrapingcourse.com/ecommerce/wp-content/uploads/2024/03/mh09-blue_main-416x516.jpg 416w" sizes="(max-width: 1274px) 100vw, 1274px"><h2 class="product-name woocommerce-loop-product__title">Abominable Hoodie</h2>
title: <h2 class="product-name woocommerce-loop-product__title">Abominable Hoodie</h2>
price: <span class="price" data-testid="product-price" data-products="price"><span class="product-price woocommerce-Price-amount amount"><bdi><span class="woocommerce-Price-currencySymbol">$</span>57.00</bdi></span></span>
"""
#add the above details in the form of a dictionary so you can print the dictionary
product_details = {"Image URL" : driver.find_element(By.CSS_SELECTOR, "a.woocommerce-LoopProduct-link.woocommerce-loop-product__link").get_attribute("href"),
                   "Product title" : driver.find_element(By.CSS_SELECTOR, "h2.product-name.woocommerce-loop-product__title").text,
                   "Price": driver.find_element(By.CSS_SELECTOR, "span.price").text}

#pretty printing otherwise the output only appears on one line
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(product_details)


#close browser
driver.quit()

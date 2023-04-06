import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=opts)
driver.get("https://rozetka.com.ua/")

search = driver.find_element(By.NAME, "search")
search.click()
search.send_keys("Кабель")
button = driver.find_element(By.CSS_SELECTOR, "button[class*=ng-tns-c65-1]").click()
check = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h1[class*=catalog-heading]"))).text
search_results = "«Кабель»"
assert check == search_results, f"Test failed{check}"

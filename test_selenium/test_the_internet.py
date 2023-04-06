from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(chrome_options=opts)

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
xpath_add = "//button[text()='Add Element']"
add_button = driver.find_element(By.XPATH, xpath_add)
add_button.click()
xpath_delete = "//button[text()='Delete']"
delete_button = driver.find_element(By.XPATH, xpath_delete)
delete_button.click()

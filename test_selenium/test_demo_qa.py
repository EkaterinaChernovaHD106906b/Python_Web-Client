from telnetlib import EC

from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(chrome_options=opts)
driver.get("https://demoqa.com/")

element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[viewBox= 0 0 448 512]"))).click

css_elements = "svg[viewBox= 0 0 448 512]"
elements = driver.find_element(By.CSS_SELECTOR, css_elements)
elements.click()
xpath_text_box = "//span[text()='Text Box']"
text_box = driver.find_element(By.XPATH, xpath_text_box)
text_box.click()

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.python.org/')

driver.find_element(By.ID, "id-search-field").send_keys("image picker")
driver.find_element(By.ID, "submit").click()
sleep(10)

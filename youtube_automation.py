from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
driver.find_element(By.NAME, "search_query").send_keys("Lud Session")
driver.find_element(By.ID, "search-icon-legacy").click()

print([my_href.get_attribute("href") for my_href in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.yt-simple-endpoint.style-scope.ytd-video-renderer#video-title")))])

sleep(10)

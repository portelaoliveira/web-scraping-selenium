import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

caminho = os.getcwd()
arquivo = caminho + r"\Pagina Hashtag.html"
driver = webdriver.Chrome()
driver.get(arquivo)

lista_elementos = driver.find_elements(By.TAG_NAME, "figure")
for elemento in lista_elementos:
    try:
        link = elemento.find_element(By.TAG_NAME, "a").get_attribute("href")
        print(link)
    except:
        continue

sleep(10)

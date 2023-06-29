from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

path = os.getcwd()
archive = path + r"\formulario.html"
driver = webdriver.Chrome()
driver.get(archive)
driver.find_element(By.XPATH, '/html/body/form/input[1]').click()
alert = driver.switch_to.alert
alert.accept()

# Botão de seleção estilo Checkbox (clicar botão)
# driver.find_element(By.XPATH, '/html/body/form/input[2]').click()
# valor = driver.find_element(By.XPATH, '/html/body/form/input[2]').is_selected()
# print(valor)

# Botão de seleção de cores (enviar valor)
# driver.find_element(By.XPATH, '/html/body/form/input[4]').send_keys("#894d4d")
# valor = driver.find_element(By.XPATH, '/html/body/form/input[4]').get_attribute("value")
# print(valor)

# Botão de datas (enviar valor)
# driver.find_element(By.XPATH, '/html/body/form/input[6]').send_keys("31/08/1997")
# valor = driver.find_element(By.XPATH, '/html/body/form/input[6]').get_attribute("value")
# print(valor)

# # Botão de Datas com Horas (enviar valor)
# driver.find_element(By.XPATH, '/html/body/form/input[7]').send_keys("31/08/1997", Keys.TAB, "12:10")
# valor = driver.find_element(By.XPATH, '/html/body/form/input[7]').get_attribute("value")
# print(valor)

# Botão de Datas com Horas (enviar valor)
# driver.find_element(By.XPATH, '/html/body/form/input[8]').send_keys(r"C:\Users\RT-000312\Documents\workspace\web-scraping-selenium\formulario.html")
# valor = driver.find_element(By.XPATH, '/html/body/form/input[8]').get_attribute("value")
# print(valor)

# Botão para selecionar mês e ano (enviar valor)
# driver.find_element(By.XPATH, '/html/body/form/input[9]').clear()
# driver.find_element(By.XPATH, '/html/body/form/input[9]').send_keys("Janeiro", Keys.TAB, "1940")
# valor = driver.find_element(By.XPATH, '/html/body/form/input[9]').get_attribute("value")
# print(valor)

# Slider (enviar valor)
# elements = driver.find_element(By.XPATH, '/html/body/form/input[15]')
# elements.clear()

# for i in range(70 - 50):
#     elements.send_keys(Keys.ARROW_RIGHT)

# valor = driver.find_element(By.XPATH, '/html/body/form/input[15]').get_attribute("value")
# print(valor)

# Selecionar itens de uma lista
elements = driver.find_element(By.TAG_NAME, 'select')
elements_select = Select(elements)
elements_select.select_by_visible_text("C")

sleep(10)

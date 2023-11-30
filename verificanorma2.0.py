import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import threading

obj_norma = {
        "Nome": "",
        "Ano": "",
        "Parte": "",
        "ISO": False,
        "ABNT": False,
        "ASTM": False,
        "IEC": False
    }

lista_das_normas = ["ISO", "ABNT", "ASTM", "IEC"]

def verifica_nome(norma):
    for tag in lista_das_normas:
        if tag in norma:
            print('Tem a tag {} na norma'.format(tag))
            obj_norma[tag] = True

def remove_letras(norma):
    numeros = ''.join(c for c in norma if c.isdigit())
    return numeros

norma = "ABNT ISO IEC 2917"
verifica_nome(norma)
print(remove_letras(norma))
print(norma)
print(obj_norma)

# options = Options()
# options.binary_location = r'C:\Users\matheus.calvet\AppData\Local\Mozilla Firefox\firefox.exe'
# driver = webdriver.Firefox(executable_path=r'C:\Users\matheus.calvet\AppData\Local\Programs\Python\Python311\geckodriver.exe', options=options)

# driver.get("https://www.abntcatalogo.com.br/pav.aspx")
# time.sleep(5)
# driver.maximize_window()
# time.sleep(1)
# driver.execute_script('document.body.style.MozTransform = "scale({})";'.format(0.8))
# time.sleep(5)

# #Botão ABNT
# if obj_norma["ABNT"]:
#     driver.find_element('xpath', '/html/body/form/div[4]/div/main/div[2]/section/div/div/div/div[2]/div/div/div[1]/div[2]/label').click()
#     time.sleep(2)
#     driver.find_element('xpath', '/html/body/form/div[4]/div/main/div[2]/section/div/div/div/div[2]/div/div/div[1]/div[2]/label').click()
#     time.sleep(2)
# else:
#     driver.find_element('xpath', '/html/body/form/div[4]/div/main/div[2]/section/div/div/div/div[2]/div/div/div[1]/div[2]/label').click()
#     time.sleep(2)

# #Botão ISO
# if obj_norma["ISO"]:
#     driver.find_element('xpath', '/html/body/form/div[4]/div/main/div[2]/section/div/div/div/div[2]/div/div/div[1]/div[3]/label').click()
#     time.sleep(2)

# #Botão IEC
# if obj_norma["IEC"]:
#     driver.find_element('xpath', '/html/body/form/div[4]/div/main/div[2]/section/div/div/div/div[2]/div/div/div[1]/div[4]/label').click()
#     time.sleep(2)

# #Botão ASTM
# if obj_norma["ASTM"]:
#     driver.find_element('xpath', '/html/body/form/div[4]/div/main/div[2]/section/div/div/div/div[2]/div/div/div[1]/div[11]/label').click()
#     time.sleep(2)

# time.sleep(2)
# driver.find_element('xpath', '//*[@id="ctl00_cphPagina_txtNM_Numero"]').send_keys(remove_letras(norma))
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR, 'div.form-group:nth-child(7) > div:nth-child(1) > div:nth-child(5) > label:nth-child(2)').click()
# time.sleep(4)
# driver.find_element('xpath', '//*[@id="cphPagina_cmdNM_Buscar"]').click()
# time.sleep(20)


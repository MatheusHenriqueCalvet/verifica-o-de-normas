import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import threading

# Configuração do driver do Selenium
options = Options()
options.binary_location = r'C:\Users\matheus.calvet\AppData\Local\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'C:\Users\matheus.calvet\AppData\Local\Programs\Python\Python311\geckodriver.exe', options=options)
driver.get("https://scitec.ultralims.com.br/public/index.php")
driver.find_element('xpath', '//*[@id="icon-id"]').send_keys('matheus.calvet')
driver.find_element('xpath', '//*[@id="icon_password"]').send_keys('99281718Mm.')
driver.find_element('xpath', '/html/body/div/div[2]/form/button').click()
time.sleep(5)
element = driver.find_element('xpath', '//*[@id="botaoModal"]')
driver.execute_script("arguments[0].click();", element)
time.sleep(1)
driver.get("https://scitec.ultralims.com.br/app/control/cadastro2Control.php?action=consultaEquipamento&operacaoPrincipal=menu&chamada=consulta")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '[title="Filtrar"]').click()
time.sleep(3)
tabela = driver.find_element('xpath', '/html/body/div[2]/form/div[1]/table[2]/tbody')
linhas = tabela.find_elements(By.TAG_NAME, 'tr')

# Função para simular o processamento longo
def simular_processamento_longo():
    global i
    dados = []
    for linha in linhas:
        nome_equipamento = linha.find_element('xpath', './td[2]').text
        im_equipamento = linha.find_element('xpath', './td[7]').text
        print('Nome do equipamento: ', nome_equipamento)
        print('IM do equipamento: ', im_equipamento)
        dados.append({'Nome do equipamento': nome_equipamento, 'IM do Equipamento': im_equipamento})
        i += 1
        print(i)
        progress_bar['value'] = i
        root.update_idletasks()
    df = pd.DataFrame(dados)
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Arquivos Excel", "*xlsx")])
    if file_path:
        df.to_excel(file_path, index=False)
        print("Dados salvos com sucesso no arquivo Excel: ", file_path)
    root.after(100, loading_window.destroy)

def iniciar_processamento():
    global loading_window, i
    loading_window = tk.Toplevel(root)
    loading_window.title("Loading")
    ttk.Label(loading_window, text="Carregando...").pack(padx=20, pady=20)
    i = 0
    progress_bar['maximum'] = len(linhas)
    threading.Thread(target=simular_processamento_longo).start()

root = tk.Tk()
root.title("Tela de Loading")
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=20)


button = tk.Button(root, text="Iniciar Processamento", command=iniciar_processamento)
button.pack(pady=20)

root.mainloop()
driver.quit()
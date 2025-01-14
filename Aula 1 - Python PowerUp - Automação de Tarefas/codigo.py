# Instalar o pyautogui
# - pip install pyautogui
# - pip install pandas
import pyautogui
import time

# pyautogui.PAUSE = 0.4
# pyautogui.click()

#Passo 1: Abrir o sistema da empresa

pyautogui.press('win')
time.sleep(1)
pyautogui.write('firefox')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)

#Passo 2: Fazer login
pyautogui.click(x=1684, y=396)
pyautogui.write("italae.barbosa")
pyautogui.press("tab")
pyautogui.write("italae.barbosa")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)

#Passo 3: Importar a base de dados dos produtos
import pandas

tabela = pandas.read_csv("produtos.csv")

# print(tabela)
time.sleep(1)

for linha in tabela.index:
    
    codigo = str(tabela.loc[linha, "codigo"])
    marca = str(tabela.loc[linha, "marca"])
    tipo = str(tabela.loc[linha, "tipo"])
    categoria = str(tabela.loc[linha, "categoria"])
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    custo = str(tabela.loc[linha, "custo"])
    obs = str(tabela.loc[linha, "obs"])
    if obs == 'nan':
        obs = ''
    
    #Passo 4: Cadastrar 1 produto
    pyautogui.click(x=1768, y=283)

    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(marca)
    pyautogui.press("tab")
    pyautogui.write(tipo)
    pyautogui.press("tab")
    pyautogui.write(categoria)
    pyautogui.press("tab")
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    pyautogui.write(custo)
    pyautogui.press("tab")
    pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    print(f'produto {linha} cadastrado!')
    pyautogui.scroll(10000)
    time.sleep(1)
#Passo 5: Repetir o passo 4 até acabar todos os produtos

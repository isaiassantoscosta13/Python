#Automatização de tarefas com o mouse e teclado
import pyautogui
from time import sleep

#Clicar e digitar meu usuário 
pyautogui.click(988,542, duration=2)
pyautogui.write('jhonatan')
#clicar e digitar a senha 
pyautogui.click(991,573, duration=2)
pyautogui.write('123456')
#Clicar no botão entrar 
pyautogui.click(852,613, duration=2)
#Extrair produtos 
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        #Digitar as informações: produto, quantidade e preço
        pyautogui.click(646,523, duration=2)
        pyautogui.write(produto)
        pyautogui.click(644,556, duration=2)
        pyautogui.write(quantidade)
        pyautogui.click(642,593, duration=2)
        pyautogui.write(preco)
        #Clicar para cadastrar
        pyautogui.click(495,786, duration=2)
        sleep(1)
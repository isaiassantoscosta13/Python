import requests
import json

#Api que retorna as cotações em tempo real das moedas 
cot = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cot = cot.json()
dolar = cot['USDBRL']['bid']
euro = cot['EURBRL']['bid']
bit = cot['BTCBRL']['bid']

print(f"Dolar: {dolar}")
print(f"Euro: {euro}")
print(f"Bit: {bit}")
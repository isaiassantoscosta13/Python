import requests
import json

#Api de CEP
cot = requests.get("https://cep.awesomeapi.com.br/json/69306250")
cot = cot.json()

rua = cot['address_name']
bairro = cot['district']
cidade = cot['city']
estado = cot['state']

print(f"Rua: {rua}")
print(f"Bairro: {bairro}")
print(f"Cidade: {cidade}")
print(f"Estado: {estado}")


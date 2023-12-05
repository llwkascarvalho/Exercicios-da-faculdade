import re

texto = "Algoritmos e Programação de Computadores"
result = re.findall(r'\w+', texto)
print(result) # ['Algoritmos', 'e', 'Programação', 'de', 'Computadores']

telefone = "(84) 91234-5678"
result = re.findall(r'[0-9]+', telefone)
print(result) # ['84', '91234', '5678']
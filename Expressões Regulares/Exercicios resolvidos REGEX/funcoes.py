#MATCH

import re

def validar_email(email):

    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # re.match tenta encontrar o padrão desde o início da string.
    # Se encontrar uma correspondência, retorna um objeto Match; caso contrário, retorna None.
    if re.match(pattern, email):
        return True
    return False


print(validar_email("lwkascarvalho1@gmail.com")) # True
print(validar_email("exemplo@dominio")) # False


# FINDALL 

def extrair_telefones(texto):
    # Define um padrão regex para números de telefone
    pattern = r'\b\d{1,3}[-\s]?\d{2,3}[-\s]?\d{4}\b'
    # re.findall retorna todas as correspondências do padrão no texto.
    return re.findall(pattern, texto)


texto = "Contate-nos no 123-456-789 ou 987 654 321."
print(extrair_telefones(texto)) # ['123-456-789', '987 654 321']


#SUB

#Exercicio 1 

def substituir_urls(texto):
    # Define um padrão regex para URLs
    pattern = r'https?://\S+'
    # re.sub substitui todas as correspondências do padrão por "[LINK]"
    return re.sub(pattern, '[LINK]', texto)


texto = "Visite nosso site em http://www.exemplo.com ou https://exemplo.com.br para mais informações."
print(substituir_urls(texto)) # "Visite nosso site em [LINK] ou [LINK] para mais informações."


#Exercicio 2

texto = "Removendo as <em>marcas</em> do <pre>texto</pre>."
print(re.sub(r'<.*>', "", texto))
# Removendo as .
print(re.sub(r'</.*>', "", texto))
# Removendo as <em>marcas.
print(re.sub(r'<.*?>', "", texto))
# Removendo as marcas do texto.


# SEARCH 

#Exercicio 1

import re

texto = "Algoritmos e Programação de Computadores"

print(re.search(r'o(.*)e(.*)o', texto).group())
# oritmos e Programação de Computado

print(re.search(r'o(.*)e(.*?)o', texto).group())
# oritmos e Programação de Co

print(re.search(r'o(.*?)e(.*?)o', texto).group())
# oritmos e Pro

#Exercicio 2

regexp = r'^[+-]?[0-9]+(\.[0-9]+)?$'

while True:
    numero = input()

    if not(numero):
        break
    
    if re.search(regexp, numero):
        print(numero)
    else:
        print("ERRO")


#Exercicio 3 
        

texto = "Data de Nascimento: 19/09/1975"
result = re.search(r'(\d{2})/(\d{2})/(\d{4})', texto)
print(result.group())
# 19/09/1975
print("Dia:", result.group(1))
# Dia: 19
print("Mês:", result.group(2))
# Mês: 09
print("Ano:", result.group(3))
# Ano: 1975
print(result.group(1, 2, 3))
# ('19', '09', '1975')
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

def substituir_urls(texto):
    # Define um padrão regex para URLs
    pattern = r'https?://\S+'
    # re.sub substitui todas as correspondências do padrão por "[LINK]"
    return re.sub(pattern, '[LINK]', texto)


texto = "Visite nosso site em http://www.exemplo.com ou https://exemplo.com.br para mais informações."
print(substituir_urls(texto)) # "Visite nosso site em [LINK] ou [LINK] para mais informações."


# SEARCH 

import re

regexp = r'^[+-]?[0-9]+(\.[0-9]+)?$'

while True:
    número = input()

    if not(número):
        break
    
    if re.search(regexp, número):
        print ("OK")
    else:
        print("ERRO")
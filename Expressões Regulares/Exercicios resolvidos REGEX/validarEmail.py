import re 

def validarEmail(email):
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]\.[a-zA-Z]{2,}$'

    if re.match(pattern,email):
        return True
    return False

print(validarEmail("lwkascarvalho1@gmail.com"))
print(validarEmail("exemplo@dominio.com"))

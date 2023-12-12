import re 

def validar_email(email): 

    pattern = r'^[a-zA-Z0-9-._]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        return True
    else: 
        return False

print(validar_email("lwkascarvalho1@gmail.com"))
print(validar_email("naovalido@222.b"))



import re 

texto = "Algoritmos e Programação de Computadores"
result = re.search(r'(\w*)ama(\w*)', texto)

print(type(result)) # <class 're.Match'>
print(result.group()) # Programação
print(result.span()) # (13,24)
print(re.search(r'^\w*', texto)) # <re.Match object; span=(0, 10), match='Algoritmos'>
print(re.search(r'\w*$', texto)) # <re.Match object; span=(28, 40), match='Computadores'>

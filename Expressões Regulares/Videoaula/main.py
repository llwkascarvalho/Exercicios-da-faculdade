import re

string = "Lwkas"

pattern = re.compile("Lwkas")

resultado = re.fullmatch(pattern, string)

print(resultado)
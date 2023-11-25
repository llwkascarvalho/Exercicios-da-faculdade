import time

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    a, b = divmod(x, 10**m)
    c, d = divmod(y, 10**m)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a + b), (c + d)) - ac - bd

    resultado = ac * 10**(2*m) + ad_bc * 10**m + bd

    return resultado

def multiplicacao_tradicional(x, y):
    return x * y


num1 = 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
num2 = 2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222

# Aumentando a duração da execução
num_iteracoes = 10000

# Tempo de execução para o algoritmo de Karatsuba
inicio_tempo_karatsuba = time.time()
for _ in range(num_iteracoes):
    resultado_karatsuba = karatsuba(num1, num2)
fim_tempo_karatsuba = time.time()
tempo_karatsuba = (fim_tempo_karatsuba - inicio_tempo_karatsuba) / num_iteracoes

# Tempo de execução para a multiplicação tradicional
inicio_tempo_tradicional = time.time()
for _ in range(num_iteracoes):
    resultado_tradicional = multiplicacao_tradicional(num1, num2)
fim_tempo_tradicional = time.time()
tempo_tradicional = (fim_tempo_tradicional - inicio_tempo_tradicional) / num_iteracoes


print(f"Resultado Karatsuba: {resultado_karatsuba}")
print(f"Resultado Tradicional: {resultado_tradicional}")

print(f"Tempo médio de execução Karatsuba: {tempo_karatsuba} segundos")
print(f"Tempo médio de execução Tradicional: {tempo_tradicional} segundos")










'''
como o python faz essa multiplicação por trás dos panos. Colocar no relatório.
'''


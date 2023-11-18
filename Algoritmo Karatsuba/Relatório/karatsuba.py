import os
import timeit
import csv
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def multiplicacao_convencional(x, y):
    return x * y

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    
    m = max(len(str(x)), len(str(y)))
    m2 = m // 2

    a, b = divmod(x, 10**m2)
    c, d = divmod(y, 10**m2)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    return ac * 10**(2*m2) + ad_bc * 10**m2 + bd

# Números para multiplicação
num1 = 12345678901234567890
num2 = 98765432109876543210

# Obter o caminho completo para o diretório do script
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Corrigir o caminho do arquivo CSV
caminho_arquivo_csv = os.path.join(diretorio_atual, 'Arquivo CSV', 'tempos_execucao.csv')

# Medir o tempo de execução da multiplicação convencional usando timeit
tempo_execucao_convencional = timeit.timeit(lambda: multiplicacao_convencional(num1, num2), number=100)

# Medir o tempo de execução da multiplicação com o algoritmo de Karatsuba usando timeit
tempo_execucao_karatsuba = timeit.timeit(lambda: karatsuba(num1, num2), number=100)

# Criar o diretório se não existir
if not os.path.exists(os.path.dirname(caminho_arquivo_csv)):
    os.makedirs(os.path.dirname(caminho_arquivo_csv))

# Armazenar os tempos em um arquivo CSV
with open(caminho_arquivo_csv, 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(['Algoritmo', 'Tempo de Execução'])
    escritor_csv.writerow(['Convencional', tempo_execucao_convencional])
    escritor_csv.writerow(['Karatsuba', tempo_execucao_karatsuba])

# Criar um gráfico de barras comparativo usando seaborn
dados = {'Algoritmo': ['Convencional', 'Karatsuba'],
         'Tempo de Execução': [tempo_execucao_convencional, tempo_execucao_karatsuba]}
df = pd.DataFrame(dados)

plt.figure(figsize=(8, 6))
sns.barplot(x='Algoritmo', y='Tempo de Execução', data=df, palette='viridis')
plt.xlabel('Algoritmos')
plt.ylabel('Tempo de Execução (s)')
plt.title('Comparação de Tempo de Execução')
plt.show()


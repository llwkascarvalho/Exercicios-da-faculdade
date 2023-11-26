import time
import random
import json
import matplotlib.pyplot as plt

def karatsuba(x, y):
    # Implementação do algoritmo de Karatsuba
    x_str, y_str = str(x), str(y)

    if len(x_str) == 1 or len(y_str) == 1:
        return int(x_str) * int(y_str)

    n = max(len(x_str), len(y_str))
    m = n // 2

    x_str = x_str.zfill(n)
    y_str = y_str.zfill(n)

    a, b = int(x_str[:m]), int(x_str[m:])
    c, d = int(y_str[:m]), int(y_str[m:])

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    result = ac * 10**(2 * m) + ad_bc * 10**m + bd
    return result

# Função para medir o tempo de execução
def measure_time(func, *args, num_iterations=1000):
    total_time = 0
    for _ in range(num_iterations):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        total_time += end_time - start_time
    return total_time / num_iterations

# Função para salvar resultados em um arquivo JSON
def save_results_to_file(data, file_path):
    with open(file_path, "a") as file:
        json.dump(data, file)
        file.write("\n")

# Função para carregar resultados de um arquivo JSON
def load_results_from_file(file_path):
    results = []
    with open(file_path, "r") as file:
        for line in file:
            if line.strip():
                result = json.loads(line)
                results.append(result)
    return results

# Teste com números de 100 dígitos
num_digits = 100
num1 = random.randint(10**(num_digits-1), 10**num_digits - 1)
num2 = random.randint(10**(num_digits-1), 10**num_digits - 1)

# Medir o tempo de execução e salvar em um arquivo JSON
karatsuba_time_100 = measure_time(karatsuba, num1, num2)
standard_time_100 = measure_time(lambda x, y: x * y, num1, num2)

# Salvar dados em um arquivo
data_100 = {"karatsuba_time": karatsuba_time_100, "standard_time": standard_time_100}
save_results_to_file(data_100, "results_large_numbers_100.json")

# Leitura dos dados do arquivo
results_large_numbers_100 = load_results_from_file("results_large_numbers_100.json")

# Exibição dos resultados
print(f"Números (100 dígitos): {num1} e {num2}")
print(f"Tempo de execução do Karatsuba: {karatsuba_time_100}")
print(f"Tempo de execução da multiplicação padrão: {standard_time_100}")

# Teste com números de 500 dígitos
num_digits = 500
num1 = random.randint(10**(num_digits-1), 10**num_digits - 1)
num2 = random.randint(10**(num_digits-1), 10**num_digits - 1)

# Medir o tempo de execução e salvar em um arquivo JSON
karatsuba_time_500 = measure_time(karatsuba, num1, num2)
standard_time_500 = measure_time(lambda x, y: x * y, num1, num2)

# Salvar dados em um arquivo
data_500 = {"karatsuba_time": karatsuba_time_500, "standard_time": standard_time_500}
save_results_to_file(data_500, "results_large_numbers_500.json")

# Leitura dos dados do arquivo
results_large_numbers_500 = load_results_from_file("results_large_numbers_500.json")

# Exibição dos resultados
print(f"\nNúmeros (500 dígitos): {num1} e {num2}")
print(f"Tempo de execução do Karatsuba: {karatsuba_time_500}")
print(f"Tempo de execução da multiplicação padrão: {standard_time_500}")

# Plotagem do gráfico para 100 dígitos
x_values_100 = ["Karatsuba", "Multiplicação Padrão"]
y_values_100 = [karatsuba_time_100, standard_time_100]

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(x_values_100, y_values_100)
plt.ylabel("Tempo de Execução (s)")
plt.title("Comparação para Números de 100 Dígitos")

# Plotagem do gráfico para 500 dígitos
x_values_500 = ["Karatsuba", "Multiplicação Padrão"]
y_values_500 = [karatsuba_time_500, standard_time_500]

plt.subplot(1, 2, 2)
plt.bar(x_values_500, y_values_500)
plt.ylabel("Tempo de Execução (s)")
plt.title("Comparação para Números de 500 Dígitos")

plt.tight_layout()
plt.show()

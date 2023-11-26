import json
import matplotlib.pyplot as plt
import timeit

def karatsuba(x, y):
    # Implementação do algoritmo de Karatsuba para lidar com diferentes tamanhos de números
    x_str, y_str = str(x), str(y)

    if len(x_str) == 1 or len(y_str) == 1:
        return int(x_str) * int(y_str)

    n = max(len(x_str), len(y_str))
    m = n // 2

    # Preencher com zeros à esquerda se a string não tiver comprimento suficiente
    x_str = x_str.zfill(n)
    y_str = y_str.zfill(n)

    a, b = int(x_str[:m]), int(x_str[m:])
    c, d = int(y_str[:m]), int(y_str[m:])

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    result = ac * 10**(2 * m) + ad_bc * 10**m + bd
    return result

def measure_time(func, *args, num_iterations=1000):
    time = timeit.timeit(lambda: func(*args), number=num_iterations)
    return time / num_iterations

def save_results_to_file(data):
    with open("results_exercise2.json", "a") as file:
        json.dump(data, file)
        file.write("\n")

def load_results_from_file(file_path):
    results = []
    with open(file_path, "r") as file:
        for line in file:
            if line.strip():
                result = json.loads(line)
                results.append(result)
    return results

def plot_results(results):
    x_values = list(range(1, len(results) + 1))
    y_values_karatsuba = [result["karatsuba_time"] for result in results]
    y_values_standard = [result["standard_time"] for result in results]

    plt.plot(x_values, y_values_karatsuba, label="Karatsuba")
    plt.plot(x_values, y_values_standard, label="Multiplicação Padrão")
    plt.xlabel("Execução")
    plt.ylabel("Tempo de Execução (s)")
    plt.legend()
    plt.show()

# Teste com os pares de números fornecidos
num_pairs = [
    (123, 456789),
    (12345, 678),
    (123456, 78901234)
]

for i, (num1, num2) in enumerate(num_pairs, 1):
    karatsuba_time = measure_time(karatsuba, num1, num2)
    standard_time = measure_time(lambda x, y: x * y, num1, num2)

    # Salvar dados em um arquivo
    data = {"karatsuba_time": karatsuba_time, "standard_time": standard_time}
    save_results_to_file(data)

    print(f"Execução {i}:")
    print(f"Karatsuba Time: {karatsuba_time}")
    print(f"Standard Time: {standard_time}")
    print("-" * 30)


# Leitura dos dados do arquivo e plotagem do gráfico
results = load_results_from_file("results_exercise2.json")
plot_results(results)

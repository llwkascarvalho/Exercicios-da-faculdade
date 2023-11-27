import json
import matplotlib.pyplot as plt
import timeit

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

def measure_time(func, *args, num_iterations=1000):
    time = timeit.timeit(lambda: func(*args), number=num_iterations)
    return time / num_iterations

def save_results_to_file(data):
    with open("results.json", "a") as file:
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
num1 = 1234
num2 = 5678

karatsuba_time = measure_time(karatsuba, num1, num2)
standard_time = measure_time(lambda x, y: x * y, num1, num2)

# Salvar dados em um arquivo
data = {"karatsuba_time": karatsuba_time, "standard_time": standard_time}
save_results_to_file(data)

# Leitura dos dados do arquivo e plotagem do gráfico
results = load_results_from_file("results.json")
plot_results(results)
def karatsuba(x,y):
    if x < 10 or y < 10:
        return x * y
    
    n = max(len(str(x)),len(str(y)))
    m = n // 2

    x_high, x_low = divmod(x, 10**m)
    y_high, y_low = divmod(y, 10**m)

    z0 = karatsuba(x_low, y_low)
    z1 = karatsuba((x_low + x_high), (y_low + y_high))
    z2 = karatsuba(x_high, y_high)

    return z2 * 10**(2 * m) + ((z1 - z2 - z0) * 10**m) + z0

#testando o algoritmo 

resultado = karatsuba(1414213562373095048801688724209, 3141592653589793238462643383)
print(f"Resultado: {resultado}")








'''
como o python faz essa multiplicação por trás dos panos. Colocar no relatório.
'''


def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibo = [0, 1]
    for i in range(2, n):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    return fibo

def suma_total(serie):
    return sum(serie)

def suma_acumulada(serie):
    acumulada = []
    suma = 0
    for num in serie:
        suma += num
        acumulada.append(suma)
    return acumulada

def main():
    try:
        n = int(input("¿Cuántos números de Fibonacci desea?: "))
        serie = fibonacci_sequence(n)
        print("\nSerie Fibonacci:")
        print(serie)

        total = suma_total(serie)
        print("\nSuma total de la serie:", total)

        print("\nSuma acumulada paso a paso:")
        acumulada = suma_acumulada(serie)
        for i, val in enumerate(acumulada):
            print(f"Suma hasta el término {i}: {val}")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
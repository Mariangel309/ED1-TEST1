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

def main():
    try:
        n = int(input("¿Cuántos números de Fibonacci desea?: "))
        serie = fibonacci_sequence(n)
        print("Serie Fibonacci:")
        for num in serie:
            print(num)
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()

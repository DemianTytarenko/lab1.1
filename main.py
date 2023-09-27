def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        next_fib = fib[i - 1] + fib[i - 2]
        fib.append(next_fib)
    return fib[n]

# Введіть число n для розрахунку n-го числа Фібоначчі
n = int(input("Введіть число n: "))

if n < 0:
    print("Число має бути додатнім")
else:
    result = fibonacci(n)
    print(f"{n}-е число Фібоначчі: {result}")

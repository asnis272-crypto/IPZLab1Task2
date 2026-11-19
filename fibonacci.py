"""
Програма для обчислення чисел Фібоначчі
Лабораторна робота №1 - Завдання 2
Автор: Снісар Андрій Валентинович
"""


def fibonacci(n):
    """Обчислює перші n чисел Фібоначчі."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence


def main():
    print("Програма для обчислення чисел Фібоначчі")
    print("=" * 45)
    
    n = int(input("Введіть кількість чисел Фібоначчі: "))
    
    if n <= 0:
        print("Помилка: число повинно бути додатнім!")
        return
    
    result = fibonacci(n)
    print(f"\nПерші {n} чисел Фібоначчі:")
    for i, num in enumerate(result):
        print(f"  F({i}) = {num}")
    
    print(f"\nСума: {sum(result)}")


if __name__ == "__main__":
    main()

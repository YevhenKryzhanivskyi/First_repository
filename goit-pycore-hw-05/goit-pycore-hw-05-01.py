def caching_fibonacci(n, cache=None):
    """Обчислює число Фібоначчі з кешуванням результатів."""
    if cache is None:
        cache = {}

    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n in cache:
        return cache[n]

    cache[n] = caching_fibonacci(n - 1, cache) + caching_fibonacci(n - 2, cache)
    return cache[n]


def main():
    """Основна функція для взаємодії з користувачем."""
    try:
        n = int(input("Введіть число для обчислення числа Фібоначчі: "))
        result = caching_fibonacci(n)
        print(f"Число Фібоначчі для n = {n} дорівнює: {result}")
    except ValueError:
        print("Будь ласка, введіть ціле число.")

if __name__ == "__main__":
    main()
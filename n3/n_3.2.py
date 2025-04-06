def addition():
    try:
        a = float(input("Слагаемое 1: "))
        b = float(input("Слагаемое 2: "))
    except ValueError:
        raise ValueError("Оба слагаемых должны быть числами")
    return a + b

def subtraction():
    try:
        a = float(input("Уменьшаемое: "))
        b = float(input("Вычитаемое: "))
    except ValueError:
        raise ValueError("Оба числа должны быть числовыми")
    return a - b

def multiplication():
    try:
        a = float(input("Множитель 1: "))
        b = float(input("Множитель 2: "))
    except ValueError:
        raise ValueError("Оба множителя должны быть числами")
    return a * b

def division():
    print("Типы деления:\n1. Обычное\n2. Остаток\n3. Целочисленное")
    choice = input("Выберите тип (1-3): ")
    
    try:
        a = float(input("Делимое: "))
        b = float(input("Делитель: "))
    except ValueError:
        raise ValueError("Делимое и делитель должны быть числами")
    
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    
    if choice == '1':
        return a / b
    elif choice == '2':
        return a % b
    elif choice == '3':
        return a // b
    else:
        raise ValueError("Неверный выбор операции деления")

def exponentiation():
    try:
        base = float(input("Основание: "))
        exponent = float(input("Показатель: "))
    except ValueError:
        raise ValueError("Основание и показатель должны быть числами")
    return base ** exponent

def factorial():
    try:
        n = int(input("Число: "))
    except ValueError:
        raise ValueError("Число должно быть целым")
    
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def square_root():
    try:
        num = float(input("Число: "))
    except ValueError:
        raise ValueError("Число должно быть числовым")
    
    if num < 0:
        raise ValueError("Квадратный корень из отрицательного числа не определен")
    
    guess = num
    precision = 10 ** (-10)
    while abs(guess * guess - num) > precision:
        guess = (guess + num / guess) / 2
    return guess

def average():
    try:
        numbers = list(map(float, input("Список чисел через пробел: ").split()))
    except ValueError:
        raise ValueError("Все элементы должны быть числами")
    
    if not numbers:
        raise ValueError("Список не может быть пустым")
    
    return sum(numbers) / len(numbers)

operations = {
    '1': ('Сложение', addition),
    '2': ('Вычитание', subtraction),
    '3': ('Умножение', multiplication),
    '4': ('Деление', division),
    '5': ('Возведение в степень', exponentiation),
    '6': ('Факториал', factorial),
    '7': ('Квадратный корень', square_root),
    '8': ('Среднее арифметическое', average)
}

while True:
    print("\nДоступные операции:")
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")
    
    choice = input("Операция: ").strip().lower()
    
    if choice == 'exit':
        print("Завершение работы калькулятора")
        break
    
    if choice not in operations:
        print("Ошибка: неизвестная операция!")
        continue
    
    try:
        _, operation = operations[choice]
        result = operation()
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        print(f">>> {result}")
    except Exception as e:
        print(f"Ошибка: {e}")
    
from typing import List

def mult(numbers: List[int], multiplier: int = 2) -> List[int]:
    
    return [num * multiplier for num in numbers]

def l_mult(numbers: List[int], multiplier: int = 2) -> List[int]:
   
    return list(map(lambda x: x * multiplier, numbers))


nums = []
while not nums:
    try:
        input_str = input("Введите числа через пробел: ").strip()
        if not input_str:
            raise ValueError("Пустая строка")
        nums = [int(num) for num in input_str.split()]
    except ValueError as e:
        print("Ошибка:", "Введите только целые числа!" if "invalid literal" in str(e) else "Список не может быть пустым!")
        continue

while True:
    m_input = input("Множитель (по умолчанию 2): ").strip()
    if not m_input:
        multiplier = 2
        break
    try:
        multiplier = int(m_input)
        break
    except ValueError:
        print("Множитель должен быть целым числом!")


print("Результат (функция):", mult(nums, multiplier))
print("Результат (лямбда):", l_mult(nums, multiplier))



    
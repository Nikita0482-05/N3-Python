def function_name(search: str, status: bool, *args: 'Any', **kwargs: 'Any') -> 'list[int] | str':
    """
    Обрабатывает аргументы в зависимости от параметров search и status.

    Args:
        search: Режим обработки ("args" для позиционных аргументов, "kwargs" для именованных)
        status: Флаг обработки (для режима "args" определяет тип возвращаемого значения)
        *args: Позиционные аргументы произвольных типов
        **kwargs: Именованные аргументы произвольных типов

    Returns:
        list[int] | str: 
        - Если search="args" и status=True: список целых чисел из args
        - Если search="args" и status=False: строку с конкатенацией всех args
        - Если search="kwargs": строку с описанием пар ключ-значение

    Raises:
        ValueError: Если параметр search не "args" или "kwargs"

    Examples:
        >>> function_name("args", True, 1, 2, "a", 3)
        [1, 2, 3]
        
        >>> function_name("args", False, 1, 2, "a")
        '12a'
        
        >>> function_name("kwargs", False, a=1, b="test")
        'Key: a, Value: 1; Key: b, Value: test; '
    """
    result: list[int] = []
    result_2: str = ""

    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        for i in args:
            result_2 += f"{i}"
        return result_2
    
    if search == "kwargs":
        for k, v in kwargs.items():
            result_2 += f"Key: {k}, Value: {v}; "
        return result_2
    
    raise ValueError("Error for search")

print(function_name("args", True, 1, 2, "a", 3))
print(function_name("args", False, 1, 2, "a"))
print(function_name("kwargs", False, a=1, b="test"))

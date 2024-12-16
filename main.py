import random

class Encryptor:
    """
    Об'єкт-шифратор, який приховує вхідні числа та виконує випадкову математичну операцію над ними.
    """
    
    def __init__(self, *numbers):
        """
        Ініціалізує шифратор зі списком чисел.
        
        Args:
            *numbers (int, float): числа, які будуть зашифровані.
        """
        self._numbers = list(numbers)  # Приватний список чисел
        self._result = self._perform_random_operation()  # Результат випадкової операції
    
    def _perform_random_operation(self):
        """
        Виконує випадкову математичну операцію над числами.
        
        Returns:
            float: Результат виконаної операції.
        """
        if not self._numbers:
            return 0
        
        operation = random.choice(['add', 'subtract', 'multiply', 'divide'])
        result = self._numbers[0]
        
        for num in self._numbers[1:]:
            if operation == 'add':
                result += num
            elif operation == 'subtract':
                result -= num
            elif operation == 'multiply':
                result *= num
            elif operation == 'divide':
                if num != 0:
                    result /= num
                else:
                    result += 0  # Уникнення ділення на нуль
        
        return result
    
    def __str__(self):
        """
        Перевантажує метод __str__ для виведення результату обчислень.
        
        Returns:
            str: Результат обчислень у вигляді рядка.
        """
        return f"Результат обчислень: {self._result:.2f}"
    
    def get_numbers(self):
        """
        Метод для отримання прихованих чисел (для тестування або налагодження).
        
        Returns:
            list: Список вихідних чисел.
        """
        return self._numbers
    
    def get_result(self):
        """
        Метод для отримання результату виконаної математичної операції.
        
        Returns:
            float: Результат обчислень.
        """
        return self._result


# Демонстрація роботи шифратора
if __name__ == "__main__":
    encryptor = Encryptor(10, 5, 2)
    print(encryptor)  # Виведення результату обчислень
    print("Числа, що були зашифровані:", encryptor.get_numbers())  # Для налагодження
    print("Результат виконаної операції:", encryptor.get_result())  # Виведення результату

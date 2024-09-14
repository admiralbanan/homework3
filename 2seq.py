# Ввод элементов через запятую, точку с запятой или слэш
user_input = input("Введите элементы списка через запятую, точку с запятой или слэш: ")

# Определение разделителя
if ',' in user_input:
    separator = ','
elif ';' in user_input:
    separator = ';'
else:
    separator = '/'

# Преобразование строки в список
numbers = user_input.split(separator)

# Поиск уникальных элементов
unique_numbers = [num for num in numbers if numbers.count(num) == 1]

# Вывод результата
print("Уникальные элементы:", unique_numbers)

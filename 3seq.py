# Ввод первого списка
first_list = input("Введите элементы 1-го списка через запятую: ").split(',')

# Ввод второго списка
second_list = input("Введите элементы 2-го списка через запятую: ").split(',')

# Удаление элементов второго списка из первого
result = [item for item in first_list if item not in second_list]

# Вывод результата
print("Результат:", result)

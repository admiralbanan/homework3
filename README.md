# Часто используемые методы для разных типов данных

## Списки (list):
  * append(x) — добавление элемента в конец списка.
  * remove(x) — удаление первого элемента, равного x.
  * pop([i]) — удаление элемента по индексу, если индекс не указан — удаление последнего элемента.
  * sort(reverse=False) — сортировка списка.
  * extend(iterable) — расширение списка элементами другого итерируемого объекта.
## Словари (dict):
  * get(key, default=None) — получение значения по ключу, если ключ отсутствует — возврат значения default.
  * items() — возвращает пары ключ-значение в виде объектов.
  * keys() — возвращает ключи словаря.
  * values() — возвращает значения словаря.
  * pop(key, default=None) — удаление элемента по ключу с возможностью вернуть значение по умолчанию, если ключ отсутствует.
## Множества (set):
  * add(x) — добавление элемента в множество.
  * remove(x) — удаление элемента, если его нет — ошибка.
  * discard(x) — удаление элемента, если его нет — ничего не делает.
  * union(other) — объединение множеств.
  * intersection(other) — пересечение множеств.
## Cтроки (str):
  * split(separator) — разделение строки по разделителю.
  * replace(old, new, count) — замена подстроки.
  * find(substring) — поиск подстроки, возвращает индекс или -1.
  * lower() — преобразование строки к нижнему регистру.
  * strip() — удаление пробелов по краям строки.

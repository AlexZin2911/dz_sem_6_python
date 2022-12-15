import task_2_2 as t

length = t.enter_num('Введите размер массива: ')
print('Сгенерированный массив: ')
lst = t.create_list(length)
print(lst)

print('Отсортированный массив: ')
print(t.separate_by_elements(lst))
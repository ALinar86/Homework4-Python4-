# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Пример:
# Волков Андрей 5
# Наталья Тарасова 5
# Фредди Меркури 3
# Денис Байцуров 4

# Программа выдаст:
# ВОЛКОВ АНДРЕЙ 5
# НАТАЛЬЯ ТАРАСОВА 5
# Фредди Меркури 3
# Денис Байцуров 4

def turn_to_int(elem):
    if elem.isdigit():
        return int(elem)
    return elem


with open('text.txt', encoding='utf-8') as file:
    name_with_marks = file.read().split('\n')

print(name_with_marks)

for i, record in enumerate(name_with_marks):
    record = record.rsplit(' ', maxsplit=1)
    name_with_marks[i] = list(map(turn_to_int, record))
    if name_with_marks[i][-1] > 4:
        name_with_marks[i][0] = record[0].upper()

print(name_with_marks)
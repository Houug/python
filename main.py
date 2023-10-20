#for number in range(3):
#    print(f"{number}) Первый цикл")
#    
#   for number in range(5):
#       print(f"{number}) Второй цикл")
# Имортируем библиотеку
import random
# Создаем случайное число типа int от 0 до 10
rand_num = random.randint(0, 10)

print(rand_num)

# Создание пустого массива
array = []
# Заполнение массива
for i in range(10):
    num = random.randint(0,10)
    array.append(num)

print(array)
# Перевернуть массив
array.reverse()
print(array)
# Отсортировать
array.sort()
print(array)

array.reverse()
print(array)

#            0        1        2  ...
student = ["Олег", "Артем", "Егор"]
print(student)
# Вывод по индексу
print(student[-1])

# Удалить из массива по индексу
student.pop()
print(student)

# Удалить из массива по занчению
student.remove("Артем")
print(student)


# 1) Создать массив учеников
# 2) Каждому ученику нужно поставить СЛУЧАЙНУЮ оценку
# Артем - 4
# 3) ВСЕМ АРТЕМАМ СТАВИМ ТОЛЬКО 5

students = ["Олег", "Артем", "Егор"]

for i in students:
    rand = random.randint(1,5)
    print(f"{i} - {rand}")



#rang_to_arr = list(range(10))
#print(rang_to_arr)

#for i in array:
#    print(i)

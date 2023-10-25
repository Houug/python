#      { Ключ : Значение }
#      { Key : Value }  
a = {
        "cat" : "кошка",
        "dog" : "собака",
        "monkey" : "обезьяна"
    }
# Вывод значений через ключ
print(a["cat"])
print(a["dog"])
print(a["monkey"])
# Вывод всех ключей
print(a.keys())
# Вывод всех значаний 
print(a.values())

b = {
        "name": "Artem",
        "age": 42,
        "city": "Zelenograd",
        "job": "KIBERone"
    }

c = {
        "name": "Oleg",
        "age": 45,
        "city": "Zelenograd",
        "job": "KIBERone"
    }



# Вводим число 1 или 2 и в зависимости от него подставляем значением в переменную human
ch = int(input())

if ch == 1: 
    human = b
if ch == 2:
    human = c

print(human["name"], human["age"])
#------------------

# Создаем пустой массив
array = []
# Вписываем количество людей, которое будем создавать и добавлять в массив
count = int(input("Сколько людей добавить? "))

# Вводим данные и формируем словарь
for i in range(count):

    name = input("Введите имя: ")
    age = input("Введите возраст: ")

    d = { "name": name, "age": age }
    # Добавляем словать в массив
    array.append(d)
# Выводим словарь 
for i in array:
    print(f"Имя: {i['name']}\nВозраст: {i['age']}")

# Имя: Артем
# Возраст: 33

# Имя: Олег
# Возраст: 32

# f"Привет {i['name']} \n тут новая строка"


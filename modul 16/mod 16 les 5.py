#Задача 2. Вредоносное ПО
first_message = input("Первое сообщение: ")
second_message = input("Второе сообщение: ")

# Подсчитываем количество специальных символов в каждом сообщении
count_first = first_message.count("!") + first_message.count("?")
count_second = second_message.count("!") + second_message.count("?")

# Если в первом сообщении больше символов, чем во втором
if count_first > count_second:
    third_message = first_message + " " + second_message
# Если во втором сообщении больше символов, чем в первом
elif count_second > count_first:
    third_message = second_message + " " + first_message
# Если количество символов в обоих сообщениях равно
else:
    third_message = "Ой"

# Выводим третье сообщение
print("\nТретье сообщение:", third_message)
#В этом коде мы сначала считаем количество специальных символов (! и ?) в каждом из двух сообщений. Затем, в зависимости от сравнения этих количеств, формируем третье сообщение.








#Задача 2. Соседи
#Дана строка S и номер позиции символа в строке. Напишите программу, которая выводит соседей этого символа и сообщение о количестве таких же символов среди этих соседей: их нет, есть ровно один или есть два таких же.
#Пример 1:
#Введите строку: abbc
#Номер символа: 3
#Символ слева: b
#Символ справа: c
#Есть ровно один такой же символ.

#Пример 2:
#Введите строку: abсd
#Номер символа: 3
#Символ слева: b
#Символ справа: d
#Таких же символов нет.

s = input('Строка: ')
n = int(input('номер символа: '))
symbol = s[n-1]
right = s[n]
left = s[n-2]

print('Символ слева:', right, '\nСимвол справа: ',left)
if symbol == right and symbol == left:
    print('Есть два таких же')
elif symbol == right or symbol == left:
    print('Есть ровно один такой же символ.')
else:
    print('Таких же символов нет')
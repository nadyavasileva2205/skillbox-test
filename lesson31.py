a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
x = input('Введите действие: +, -, * или /')

if x == '+':
    print('c=', a+b)
elif x == '-':
    print('c=', a-b)
elif x == '*':
    print('c=', a*b)
elif x == '/':
    print('c=', a/b)
else:
    print('Ошибка ввода')
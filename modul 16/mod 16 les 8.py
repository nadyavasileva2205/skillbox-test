#Задача 2. Олимпиада
N = int(input('Кол-во человек: '))
K = int(input('Кол-во человек в команде: '))
members = []
num = 1
for _ in range(N // K):
    if N%K !=0:
        print('ошибка')
        break
    else:
        members.append(list(range(num, num+K)))
        num += K

print(members)

#Задача 3. Контроль

people_list = []
people_num = int(input('Введите кол-во сотрудников: '))

for i in range(people_num):
    people_id = int(input('ID сотрудника: '))

new_id = int(input('Какой ID ищем? '))
if new_id == people_id:
    print('Сотрудник на месте')
else:
    print('Сотрудника нет')



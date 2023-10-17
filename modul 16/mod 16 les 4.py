#Задача 1. Задачи компаний
main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
first_company = [0, 0, 0]
second_company = [1, 0, 0, 1, 1]
third_company = [1, 1, 1, 0, 1]

main.extend(first_company)
main.extend(second_company)
main.extend(third_company)

print('Общий список задач: ', main)
# Подсчитываем количество невыполненных задач
uncompleted_tasks = main.count(0)

# Выводим итоговый список и количество невыполненных задач
print("Кол-во невыполненных задач:", uncompleted_tasks)
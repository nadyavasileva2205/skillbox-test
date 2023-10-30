#Задача 1. Матрица
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i_team in matrix:
    for i_man in i_team:
        print(i_man, end='')
    print()
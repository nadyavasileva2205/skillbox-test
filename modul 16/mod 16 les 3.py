#Задача 3. Кино
films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]
def is_fil_exist(movie, films_list):
    for i_movie in films_list:
        if i_movie==movie:
            return True
    return False

my_list = []

while True:
    print('\nВаш текущий список фильмов: ', my_list)
    new_movie = input('Название фильма: ')
    if is_fil_exist(new_movie, films):
        print('Команды: добавить, удалить, вставить')
        command = input('Введите команду: ')
        if command == 'добавить':
            my_list.append(new_movie)
        if command == 'удалить':
            if is_fil_exist(new_movie, my_list):
                my_list.remove(new_movie)
            else:
                print('Такого фильма нет в нашем рейтинге.')
        if command == 'вставить':
            index = int(input('На какое место?'))
            my_list.insert(index - 1, new_movie)
    else:
        print('Такого фильма нет на сайте')
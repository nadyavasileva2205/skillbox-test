films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
new_films = []

for _ in range(len(films)):
    # Проходимся по циклу с запросом названия фильма
    movie = input('Какой искать фильм?: ')
    if movie is not films:
        # Проверяем условие на соответствие названию фильма
        print("Такого фильма нет")
        #break
    else:
        new_films.append(movie) # Создаем новый список с фильмами

print('\nСписок любимых фильмов: ')
print(new_films)

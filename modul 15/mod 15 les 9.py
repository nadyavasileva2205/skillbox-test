
#Задача 3. Улучшенная лингвистика
#Мы уже писали программу для лингвистов, которая считала количество определённых букв в тексте. Теперь эту программу нужно улучшить. Есть список из трёх слов, которые вводит пользователь. Затем вводится сам текст произведения строго по словам. Текст вводится до тех пор, пока не встретится слово end. Напишите программу, которая посчитает, сколько раз слова пользователя встречаются в тексте.
#Пример:
#Введите 1 слово: я
# 2 слово: год
#Введите 3 слово: лучший
#Слово из текста: этот
#Слово из текста: год
#Слово из текста: -
#Слово из текста: лучший
#Слово из текста: год
#Подсчёт слов в тексте
#я: 0
#год: 2
#лучший: 1

words_list = []
counts = [0, 0, 0]

for i in range(3):
    print('Введите',  i + 1, 'слово: ', end = '')
    word = input()
    words_list.append(word)

text = input('Слово из текста: ')
while text != 'end':
    for index in range(3):
        if words_list[index]== text:
            counts[index] += 1
    text = input('Слово из текста: ')

print('\nПодсчет слов в тексте')
for i in range(3):
    print(words_list[i], ':', counts[i])
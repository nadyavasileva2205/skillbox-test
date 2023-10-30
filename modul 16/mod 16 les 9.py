#Задача 3. Лавка
goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
fruit_name = input('Новый фрукт: ')
price = int(input('Цена: '))
procent = 1.08
goods.append([fruit_name, price])
print("Новый ассортимент:", goods)

for fruit in goods:
    fruit[1] = round(fruit[1] * 1.08, 2)

print("Новый ассортимент с увеличенной ценой:", goods)



#Задача 2. Кратность
nums_list = []
i=0
N = int(input('Кол-во чисел в списке: '))
K =  int(input('Введите делитель: '))
for _ in range(N):
 num = int(input('Очередное число: '))
 if num % K == 0:
  i+=1
  print(i)
#решено не до конца








print('Задача 4. Театр')
a = int(input("Введите кол-во рядов:"))
b = int(input("Введите кол-во сидений ряду:"))
c = int(input("Введите кол-во метров между рядами:"))

for i in range(a):
  print("="*b, "="*b, sep="*"*c)
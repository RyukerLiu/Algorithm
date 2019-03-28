Num_1 = int(input('First Number:'))
Num_2 = int(input('Second Number:'))
if Num_1 < Num_2:
    Num_1, Num_2 = Num_2, Num_1
while Num_2 != 0:
    Num_1, Num_2 = Num_2, Num_1 % Num_2
print('最大公因數 (g.c.d): ', Num_1)
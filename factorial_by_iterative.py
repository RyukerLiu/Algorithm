
def factorial(n):
    sum = 1
    for i in range(n, 0, -1):
        sum *= i
    return sum

Num = int(input('key in number for factorial'))
print(factorial(Num))
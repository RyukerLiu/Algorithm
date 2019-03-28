database = [None]*1000

def fib(n):
    result = database[n]
    if result == None:
        if n == 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = (fib(n-1) + fib(n-2))
        database[n] = result
    return result
num = int(input('Key in number for fibonacci polynomial'))
for i in range(num+1):
    print(fib(i))
def fib(n=5):
    fib_num = [1,1]
    for i in  range(0,n):
        fib_num = [sum(fib_num), fib_num[0]]
    return sum(fib_num)

print(fib())
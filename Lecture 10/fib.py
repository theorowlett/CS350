def bad_class_fib(n):
    if n <= 1:
        return n
    else:
        return bad_class_fib(n-1) + bad_class_fib(n-2)

def iwrote_fib(n):
    if n <= 1:
        return n
    else:
        return n + iwrote_fib(n-1)

def fib(x):
    memos = None * x + 1
    return fib_memos(x,memos)

def fib_memos(x, memos):
    if memos[x] is not None:
        return memos[x]
    else:
        if x <= 1:
            memos[x] = x
            return x
        else:
            fibx = fib_memos(x-1, memos) + fib_memos(x-2, memos)
            memos[x] = fibx
            return fibx

def main():
    print(bad_class_fib(10))
    print(iwrote_fib(10))


main()
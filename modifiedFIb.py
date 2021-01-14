def modifiedFib(t1, t2, n):
    def fib(m, data={}):
        if m > 0:
            if m in data:
                return data[m]
            elif m == 0:
                return 0
            elif m == 1:
                return t1
            elif m == 2:
                return t2
            elif m > 2:
                a = fib(m-1, data)
                b = fib(m-2, data)
                data.update({m: a*a+b})
                return data[m]
    return fib(n)


print(modifiedFib(0, 1, 20))
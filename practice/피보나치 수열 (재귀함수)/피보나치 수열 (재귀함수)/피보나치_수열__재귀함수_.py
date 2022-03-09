def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

for n in range (1,11):
    print(n,fibo(n))
def factorial(x):
    f=1
    for i in range (1, x+1):
        f=f*i
    return f

m=int(input("Introdu m="))
n=int(input("Introdu n="))
print((factorial(n))/((factorial(m))*(factorial(n-m))))

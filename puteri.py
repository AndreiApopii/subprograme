a=int(input(""))
b=int(input(""))
def putere(x,y):
    p=0
    for i in range(x,y):
        p+=1+(x**y+2)
    return p
print(putere(a,b))
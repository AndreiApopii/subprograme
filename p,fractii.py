x,y=int(input('Introduceti prima fractie: ')),int(input())
q,z=int(input('Introduceti a doua fractie: ')),int(input())
def adunare(a,b,c,d):
    i=((a*m)+(b*c))/(b*d)
    return (i)
print(x,'/',y,'+',q,'/',z,'=',adunare(x,y,q,z),sep='')

def inmultire(a,b,c,d):
    i=(a*c)/(b*d)
    return (i)
print(x,'/',y,'*',q,'/',z,'=',inmultire(x,y,q,z),sep='')

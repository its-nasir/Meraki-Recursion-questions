def pat(a):
    if a==16:
        print(a)
    else:
        print(a)
        pat(a+3)
pat(1)
#######################################################
def ty(a):
    if a>10000000:
        print(a)
    elif a%2==0:
        print(a)
        ty(a+1)
    else:
        print(a)
        ty(a*10)
ty(1)
###########################################################
def factorial(a):
    if a==1:
        return 1
    return a * factorial(a-1)
print(factorial(7))
###########################################################
b=[1,2,3,4]
def func(a,c):
    if len(b)==a:
        print(c) 
    else:
        c+=b[a]
        a+=1
        func(a,c)
func(0,0)
##############################################################
a='pape'
def pal(z,b):
    if b==-len(a):
        z+=a[b]
        if z==a:
            print('it is pallindrome')
        else:
            print('naah its not a pallindrome')
    else:
        z+=a[b]
        pal(z,b-1)
pal('',-1)
##############################################################
def feboni(a,b,z):
    if z>100:
        return
    else:
        print(a)
        c=a
        a=b
        z+=1
        feboni(a,b+c,z)
feboni(0,1,1)
############################################################
def febo_list(a,b,x):
    if b>100:
        print(x)
    else:
        x.append(a)
        c=a
        a=b
        febo_list(a,b+c,x)
febo_list(0,1,[])
#############################################################
b=int(input())
def find(a):
    if a[0]==b:
        print('yeah it is here')
    elif len(a)==1:
        print('naah its not here')
    else:
        find(a[1::])
find([1,2,3,4,5,6,7,88,9])
#####################################################
def flat(a,b):
    if b==len(a)-1:
        a.extend(a[b])
        a.remove(a[b])
        print(a)
    elif type(a[b])==list:
        a.extend(a[b])
        a.remove(a[b])
        b+=1
        flat(a,b)
    else:
        b+=1
        flat(a,b)
a=[1, 2, [3, 4, [5, 6, [7, 8]], 9, 10], 11, 12] 
flat(a,0)
############################################################
def pat(a,b=0):
    if a>200:
        return
    elif b%2==0:
        b+=1
        print(a)
        pat(a+3,b)
    else:
        b+=1
        print(a)
        pat(a+a,b)
pat(1)
##############################################################
def odev(a):
    if a%2==0:
        print('even=',a)
    else:
        print('odd=',a)
    if a==995:
        return
    odev(a+1)
odev(1)
##############################################################

# -*- coding: utf-8 -*-
"""Assignment1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rwO1gyq9tulpvgRHubc7Q1-20s897FKx
"""

n= input('Number of elements in array')
N= int(n)
A=[]
B=[]
C=[]

a = input('Enter elements of a list separated by space ')
print("\n")
A = a.split()
for i in range(0,N):
  A[i]=int(A[i])
for i in range(0,N):
  B.append(A[N-i-1])
for i in range(0,N):
  y= A[i]*B[i]
  C.append(y)

print(*C)

"""# Q2"""

n= input('Number of elements in array')
N= int(n)
A=[]
max1=0
max2=0

a = input('Enter elements of a list separated by space ')
print("\n")
A = a.split()
for i in range(0,N):
    A[i]=int(A[i])
for i in range(0,N):
    if max1>A[i]:
        max2=max1
        max1=A[i]
    else:
        max1=max1
        
min1=A[0]
min2=A[0]
for i in range(0,N):
    if min1<A[i]:
        min2=min1
        min1=A[i]
    else:
        min1=min1
        
print(max2,' ',min2)

"""# Q3"""

n= input('Number of elements in array')
N= int(n)
A=[]


a = input('Enter elements of a list separated by space ')
print("\n")
A = a.split()
for i in range(0,N):
    A[i]=int(A[i])
for i in range(0,N):
    if(A[i]%5==0):
        A[i]=A[i]
    else:
        print(A[i],end=' ')

"""# Q4"""

n= input('Number of bits in binary')
N= int(n)
A=[]
count0=0
count1=0
a = input('Enter elements of a list separated by space ')
print("\n")
A = a.split()
for i in range(0,N):
    A[i]=int(A[i])
for i in range(0,N):
    if A[i]==0 or A[i]==1:
        A[i]=A[i]
    else:
        print('Error! Invalid Values entered!')
        
for i in range(0,N):
    if A[i]==0:
        count0=count0+1
    else:
        count1=count1+1
if count0==1 or count1 == 1:
    print('YES')
else:
    print('NO')

"""# Q5"""

n= input('Enter Number')
N= int(n)
fact=1
for i in range(1,N+1):
    fact=fact*i
print(fact)

"""# Q6"""

n= input('Enter lower limit')
N= int(n)

m= input('Enter upper limit')
M= int(m)

for i in range (N,M+1):
    c=i
    while c!=0:
        if c%2==0:
            if c<10:
                print(i, end=',')
                c=0
            else :
                c=c/10
        else:
            c=0
"""num1=10
num2=20
num3=15
if num1%2==0:
    print("even")
else:
    print("odd")
if num2%2==0:
    print("even")
else:
    print("odd")
if num3%2==0:
    print("even")
else:
    print("odd")"""
"""#find which is even or odd from list numbers
lst=[11,12,13,14,15,16]
for i in range(0,5,1):
    if lst[i]%2==0:
        print(lst[i],"is even")
else:
        print(lst[i],"is odd")"""
"""#print even number b/w 20-40
for i in range(20,41,2):
    print(i,"even")"""

"""#method2
for i in range(20,41):
    if  i%2==0:
        print(i)"""
"""#print num 1-100
for i in range(1,101,1):
        print(i,end =" ")"""
"""#sum of n natrual numbers
n=int(input())
total = 0
for num in range(1,n+1):
    total = total+num
print(total)"""
"""#while loop###########################################################
#print 1-100 numbers
num=1
while num<101:
    print(num)
    num+=1"""

"""#print even numbers between 10-40
num=10
while num<=40:
    if num%2==0:
        print(num)
    num+=1"""

"""#print odd numbers between 1-50
num=1
while num<=50:
    if num%2==1:
        print(num)
    num+=1"""

"""#find which is even or odd from the list of numbers
lst=[10,20,13,23,5,32,91,87,54]
i=0
while i<len(lst):
    num=lst[i]
    if num%2==0:
        print(num, "even")
    else:
        print(num, "odd")
    i+=1"""

"""#sum of even numbers upto n
num=int(input())
i=0
sum=0
while i<=num:
    if i%2==0:
        sum+=i
    i+=1
print(sum)"""
"""#print100-1
num=100
while num>0:
    print(num,end=" ")
    num-=1"""
"""#find even number between the range n and m
n,m=(int,input().split())
if n%2!=0:
    n=n+1
while n<m:
    if n%2==0:
        total+=n
        n+=2 
print(total)"""
n=156
count=0
while n>0:
    n//=10
    count+=1
    print(count)
    
    



    
    

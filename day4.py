"""age=int(input())
if age>0 and age<=3:
    print("free ticket")
elif age>3 and age<=12:
    print("half ticket")
elif age>12 and age<=55:
    print("full ticket")
elif age>55:
    print("senior citizens")
else:
    print("enter a valid age")"""
"""#FIND The no is +ve even or-ve even or +odd or -odd
num=int(input())
if num>=0 and num%2==0:
    print("+ve even")
elif num<=0 and num%2==0:
    print("-ve even")
elif num>=0 and num%2==1:
    print("+ve odd")
elif num<=0 and num%2==1:
    print("-ve odd")
else:
    print("enter a valid number")"""
"""#find the biggest number among the 3 numbers
num1,num2,num3=map(int,input().split())
if num1>num2 and num1>num3:
    print("num1 is big")
elif num2>num1 and num2>num3:
    print("num2 is big")   
elif num3>num1 and num3>num2:
    print("num3 is big")
elif num1==num2==num3:
    print("three numbs are equal")
elif num1==num2 and num1>num3:
    print("num1 and num2 are equal and biggest")
elif num1==num2 and num1<num3:
    print("num3 is biggest")
elif num1==num3 and num1>num3:
    print("num1 and num3 are equal and biggest")
elif num1==num3 and num1<num3:
    print("num2 is biggest")
elif num1==num3 and num1>num3:
    print("num2 and num3 are equal and biggest")
elif num2==num3 and num1<num3:
    print("num1 is biggest")
else:
    print("enter a valid number")"""
"""#nested if else
num=int(input())
num1, num2, num3 = map(int, input().split())

if num1 == num2 == num3:
    print("Three numbers are equal")

elif num1 == num2:
    if num1 > num3:
        print("num1 and num2 are equal and biggest")
    else:
        print("num3 is biggest")

elif num1 == num3:
    if num1 > num2:
        print("num1 and num3 are equal and biggest")
    else:
        print("num2 is biggest")

elif num2 == num3:
    if num2 > num1:
        print("num2 and num3 are equal and biggest")
    else:
        print("num1 is biggest")

else:
    if num1 > num2 and num1 > num3:
        print("num1 is biggest")
    elif num2 > num1 and num2 > num3:
        print("num2 is biggest")
    else:
        print("num3 is biggest")"""
#


    
    

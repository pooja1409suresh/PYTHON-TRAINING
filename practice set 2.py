#last digit of no.
a=4567
print("last digit:",a%10)

#sum of first and last digit using two digit number
number = 98452
num_str = str(abs(number)) 
first_digit = int(num_str[0])
last_digit = int(num_str[-1])
print(first_digit+last_digit)

#swap 2 number without 3 number
a=10
b=20
print(a,b)
a=a+b
b=a-b
a=a-b
print(a,b)

#number lies in range
x=int(input())
if(x>20 and x<60):
    print("lies in range")
else:
    print("not lies in range")

#triangle is valid
x=int(input())
y=int(input())
z=int(input())
if(x+y>z):
    print("valid")
elif(x+z>y):
     print("valid")
elif(y+z>x):
     print("valid")
else:
     print("invalid")
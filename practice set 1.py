#even or odd
x=int(input("enter a no.: "))
if(x%2==0):
    print("this is even")
else:
    print("this is odd")
    
# #positive or negative
x=int(input("enter a number: "))
if(x>0):
    print("this  is positive")
elif(x<0):
    print("this  is negative")
else:
    print("invalid")

#largest of 2 no.
x=20
y=30
if(x>y):
    print("x is largest number")
else:
    print("y is largest number")

#voting eligibility
age=int(input("enter your age: "))
if(age>=18):
    print("eligible to vote")
else:
    print("not eligible to vote")

#pass or fail
marks=int(input("Enter your marks: "))
if(marks>35):
    print("you are pass")
else:
    print("you are fail")

#largest of 3 number
x=int(input())
y=int(input())
z=int(input())
if(x>y and x>z):
    print("x is larger than y and z")
elif(y>x and y>z):
    print("y is larger than x and z")
else:
    print("z is larger than x and y")

#leep year
x=int(input("year: "))
if(x/4):
    print("this is leap year")
else:
    print("this is not leap year")

#simple calculator
def Calculator(a,b):
    def Add():
        return a+b
    def sub():
        return a-b
    def multi():
        return a*b
    def div():
        return a/b
    print("Addition: ", Add())
    print("subtraction: ",sub())
    print("multiplication: ",multi())
    print("division: ",div())

#divisible by 5
x=int(input("enter the number: "))
print("divisible by 5",x%5==0)

#discount
a=int(input("enter: "))
r='eligible'if a>18 else 'not'
print(a)
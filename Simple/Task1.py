# 1)Python program to add two numbers

x=10
y=20
print("sum =",x+y)

"""
2) Python program to find the area of Triangle
Formula:  ½ * b * h
b - base
h-height

"""

base=4
height=5
area=1/2*base*height
print("Area of triangle is ",area)

"""
3)Python program to swap two variable 
Ex : a = 5, b = 10
 Output: a = 10, b = 5

"""

x=5
y=10
x,y=y,x
print("x=",x)
print("y=",y)

# 4)Python program to find the average of given numbers ( eg : a = 10, b = 30, c = 12 )	

a=10
b=30
c=12

avarage=(a+b+c)/3
print("avarage",avarage)

"""
5) Python program to add a two numbers ( a and b ) and multiply the result by ( c ) and divide that final result by ( d ) ( eg :  a = 10, b = 30, c = 12 , d = 3 )	
"""
a=10
b=30
c=12
d=3

sum=a+b
mul=sum*c

div=mul/d

print('final result',div)

"""
6) Python program to store the below details with a separate variables			( name , age , dob , height, weight, degree, gender, isAlive ) 
"""
name="Indhuja"
age=23
dob="23/10/2000"
height=157.4
weight=165
degree="B.Tech"
gender="Female"
isAlive=True

print(type(name))
print(type(age))
print(type(dob))
print(type(height))
print(type(weight))
print(type(degree))
print(type(gender))
print(type(isAlive))

"""
7) Python program to store 2 strings ( eg : word1 = “hello” word2 = “world” )  
with 2 separate variables and result the two string into one string 
( eg : helloworld ) using string concatenation	
"""

word1="hello"
word2="world"

word=word1 + word2
print('word is',word)

                                                        # Getting User Input	


"""
1)Python program to get the name from user and display the name with greetings 	 
( Sample Input : 							
Given Input : Vignesh 
Sample Output : Hello! Vignesh ) 

"""          
name=input("Enter your Name:")
print('Hello ',name)  

"""
2)Python program to get the age as input from the user. Store the input in a variable named user_age (remember to convert it to an integer).
 Calculate how many years it will take to turn 100 years old and print it
"""
user_age=int(input("Enter Your Age :"))

years=100-user_age

print('remaining age is',years )

tamil=int(input('Enter your Tamil Mark:'))
english=int(input('Enter Your English mark:'))
maths=int(input('Enter Your maths mark:'))
science=int(input('Enter Your science mark:'))
social=int(input('Enter Your social mark:'))

sumof_marks=tamil+english+maths+science+social
avarage=sumof_marks/5
print("sum of marks",sumof_marks)
print("average of marks",avarage)

"""
Make a simple numeric calculator. It should prompt the user for three numbers.
 Then add the numbers together and divide by 2. 
 Display the result. Your program must support numbers with decimals and not just integers.

"""

num1=float(input("Enter num1:"))
num2=float(input("Enter num2:"))
addition=num1+num2

divnum=addition/2

print(divnum,"divnum")


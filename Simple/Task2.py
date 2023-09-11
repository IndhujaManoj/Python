"""
1) Make a program which displays a different message depending on the age given. 
Here are the possible responses:
age is less than 16, say "You can't drive." 	
age is less than 18, say "You can't vote." 	
age is less than 25, say "You can't rent a car." 	
age is 25 or over, say "You can do anything that's legal."
Here's a sample run. Notice that a person who is under 16 will display three messages,
 one for being under 16, one for also being under 18, and one for also being under 25
"""

age=int(input('Enter Your Age'))
if age<16:
    print('You cant Drive')
elif age<18:
    print('You cant Vote')
elif age<25:
    print("you can't rent a car")
elif age>=25:
        print("you can do anything")

"""
2)Write a program that takes integer input from the  user  print  “FizzBuzz” if the number is divisible by both 3 and 5 and print 
“Fizz” if the number is divisible by 3 and print “Buzz” if the number is divisible by 5.
"""

number=int(input('Enter number :'))

if number % 3==0 and number % 5==0:
     print('FizzBuzz')
elif number % 3==0:
     print('Fizz')
elif number % 5==0:
     print('Buzz')
else:
     print(number)
"""
Write a Python program that determines if a given year is a leap year.Enter a year as input.
Use conditional statements to check if the year satisfies the leap year conditions:
The year should be divisible by 4 but not divisible by 100, or
The year should be divisible by 400.
Use appropriate logical operators and conditions to implement the leap year logic.
Display an appropriate message indicating whether the year is a leap year or not.
	Example output:
	Enter the year=2024
	2024 is a leap year
"""


year=int(input('Enter year'))

if (year%4==0 and year%100!=0) or (year%100==0):
     print(year," is leap year")
else:
     print('year is not leap year')
     


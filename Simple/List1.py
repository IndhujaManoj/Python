#Write a program to reverse a given list.

list=[1,2,3,4,5]
reverse=list[::-1]
print('reverse',reverse)

#Implement a function that finds the sum of all elements in a list.

sum=sum(list)
print('sum',sum)

# Create a function that returns the largest and smallest elements in a list.

small=min(list)
large=max(list)

print('large number is',large,"and small number is",small)

myli=[1,2,4,4,5,6]

dup=set(myli)
dup1=[x for x in dup]
print(dup1)
element=5
index=dup1.index(element)
print(index)



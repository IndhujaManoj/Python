# Write a program to reverse a given list.

list=["orange","apple","orange","banana"]
print(list[::-1])

# Implement a function that finds the sum of all elements in a list.

sumlist=[1,2,3,4,5]
totalsum=sum(sumlist)
print(totalsum)
#Remove 2nd index
pop= sumlist.pop(2)
print('pop',pop)
print(sumlist)
#Create a function that returns the largest and smallest elements in a list.

print(max(sumlist))
print(min(sumlist))

#Write a program to remove duplicate elements from a list.

original_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = set(original_list) # Changed variable name
unique_list = [x for x in unique_elements]
print (unique_list)

element=2
find=sumlist.index(element)

print(find)

# Build a program that merges two lists and sorts the result.

list1=[5,2,3,4,0]
list2=[6,7,8,9,1]
addList=list1+list2
print(sorted(addList))

#Create a function that returns the intersection of two lists (common elements).

num1=[1,3,4,5,7]
num2=[3,5,8,9]
intersection=set(num1)&set(num2)
inter=[x for x in intersection]
print(inter)

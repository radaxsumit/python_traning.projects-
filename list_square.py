# Create a a list of numbers then get squares of all the numbers in the list and put it in a new list 

list1=[1,2,3,4,5,6,7,8,9,10]
list2=[]
for i in list1:
    list2.append(i*i)
print(list1, list2)
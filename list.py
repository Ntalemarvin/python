#LISTS  
names = ['john','isaac','Marvin','frost','Mary','Benj']
print(names[4])
print(names[2:3])
print(names[:])
names[3]='frosts'
print(names)

#write a program to find the largest number in a list

numbers = [2,3,5,6,17,69,7,9,10,69,200,453,23,45]
'''lets assume the largest number is numbers[0]'''

max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)

#write a programm to remove all duplicates in a list

numbers = [2,4,5,6,7,8,2,9,6,2,9]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
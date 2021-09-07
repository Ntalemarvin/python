#2D list
matrix = [
    [1,2,3],#0
    [4,5,6],#1
    [7,8,9]#2
]

#Acess individual item
print(matrix[0][2])

print(matrix[2][0])
#modify element
matrix[1][1] = 34
print(matrix[1])

#use Nested loop to itrate through the items
for row in matrix:
    for item in row:
        print(item)

#nested loop is like a loop in a loop
#you can create coo-ordinates x,y 

for x in range(4):
    for y in range(3):
        print(f"({x},{y})")
#create a F shape using nested loop

numbers = [5,2,5,2,2]

for x_count in numbers:
    #print("x" * x_count)
    output = ""
    for count in range(x_count):
        output += 'x'
    print(output)


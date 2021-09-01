first = 'john'
last = 'smith'
#to print john [smith] is a coder

message = first + '[' + last + ']' + ' is a coder'# to tidious concatenation
#formmated strings
msg = f'{first} [{last}] is a coder'
print(message) 
print(msg)

#formatted strings
course = 'Python course by mosh'
print(course.upper()) #lower() .functions are reffered to as methods
print(course.find('p'))
print(course.find('by'))
print(course.replace('mosh','marvin frost'))
#checks for a character is a str use in opperater produces boolean

recieved = 'generally the python syntax is awesome'
print('python' in recieved)
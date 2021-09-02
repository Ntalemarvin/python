#write a code
'''
if temperature is greater than 30
    it's a hot day
otherwise if it's less than 30
    it's a cold day
otherwise 
    it's neither hot nor cold
'''

temp = 40

if temp >= 30:
    print("it's a hot day")
elif temp < 30:
    print("it's a cold day")
else:
    print("it's niether hot or cold")

name_char = "j"
len(name_char)

if len(name_char) < 3:
    print("name must be atleast 3 characters ")
elif len(name_char) > 50:
    print("name can be a maximum number of 50 characters")
else:
    print("name looks good")
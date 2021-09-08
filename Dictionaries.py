'''
used to store key value pairs ie name:marvin
'''

customer = {
    'name' : 'john smith',
    'email' : 'john@gmail.com',
    'age' : 23,
    'phone' : 1234565,
    'is_verified' : True
}

#acces a value in customer
customer['name'] #or customer.get('name')
print( customer.get('name'))

#add a value in customer
customer['passcode'] = 2341
print(customer)
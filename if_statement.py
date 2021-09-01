is_hot = False
is_cold = True

if is_hot:
    print("It's hot")
    print('Take plenty of water')
elif is_cold:
    print("It's cold")
    print('wear warm clothes')
else:
    print("It's a lovely day")
print('Have a lovely day')

#write the code where:
'''
price of a house is $1M
if buyer has good credit,
    they need to put down 10%
otherwise
    they need to put down 20%
print the down the payment

'''

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print(f"Down payment: ${down_payment}")

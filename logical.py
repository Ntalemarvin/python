#write a code for that
'''
if applicant has high income AND/OR good credit 
Eligible for a loan
'''

has_high_income = False
has_good_credit = True

#and operator
if has_high_income and has_good_credit:
    print('Eligible for a loan')

#or aoperator
if has_high_income or has_good_credit:
    print('Eligible for a loans')

# AND: both true
# OR: aleast one true

#NOT:if true converts to false & the reverse is true

'''
if applicant has enough credit and doesn',t have a criminal record 
Eligible for a loan
'''
has_enough_credit = True
has_criminal_record = False

if has_enough_credit and not has_criminal_record:#has_criminal is converted to true
    print('Eligible for both loans')
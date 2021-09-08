phone = input('phone:')

digits__mapping = {
    '1':'One',
    '2': 'Two',
    '3':'Three',
    '4':'Four'
    
}

outPut = ""
for ch in phone:
    outPut += digits__mapping.get(ch, "!") + ' ' #whats not in the dic it puts an !
print(outPut)
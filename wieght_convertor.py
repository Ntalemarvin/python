weight  = int(input('weight: '))
unit = input('(L)bs or (k)kg: ')

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"your are {converted} pounds")
else:
    converted = weight / 0.45
    print(f"your are {converted} kgs")
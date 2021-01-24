number = int(input("Hello input number: "))
resBool = isinstance(number / 2, int)

if number > 0:
    revs_number = 0   
    while(number > 0):
        revs_number = (revs_number * 10) + (number % 10)
        number = number // 10 
    number = revs_number

print(f'The result of my magic is this: {number}')
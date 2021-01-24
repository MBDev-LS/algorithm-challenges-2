number = int(input("Hello input number: ")) #This asks the user for a number.
resBool = isinstance(number / 2, int) #This checks if the number is an integer.

if number > 0: #If the number is bigger than 0 then:
    revs_number = 0   #Set a new temporary variable which is called revs_number
    while(number > 0): #While the number is more than 0
        revs_number = (revs_number * 10) + (number % 10) #It multiplies "revs_number" by 10 and adds the remainder of "number" when divided by 10.
        number = number // 10 #It divides the variable by 10.
    number = revs_number #Takes the content of the temporary variable and puts it in the variable called "number"

print(f'The result of my magic is this: {number}') #Prints the result of the algorithm to the user.
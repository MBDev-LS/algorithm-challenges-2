# Gets the users 
str1 = input("Input the first string: ")
str2 = input("Input the second string: ")

#Sets default value for main boolean 
prefixVeri = False

# Runs through the two strings for the length of the second and checks if each character is equall.
# Then sets the prefixVeri accordingly
if len(str2) <= len(str1):
    for i in range(0,len(str2)):
        if str1[i] == str2[i]:
            prefixVeri = True
        else:
            break

# Prints the result of the algorithm
print(prefixVeri)
str1 = input("Input the first string: ")
str2 = input("Input the second string: ")

prefixVeri = False

for i in range(0,len(str2)):
    if str1[i] == str2[i]:
        prefixVeri = True
    else:
        prefixVeri = False
        break

print(prefixVeri)
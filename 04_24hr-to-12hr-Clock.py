# Takes 24 hour input from the user
hr24Input = int(input('Enter the 24 hour number: '))

# Determines the suffix and has catches for boundary cases.
if hr24Input > 12:
    suffix = 'PM'
    time = hr24Input - 12

elif hr24Input == 12:
    suffix = 'PM'
    time = hr24Input

elif hr24Input == 0:
    suffix = 'AM'
    time = 12

else:
    suffix = 'AM'
    time = hr24Input


# Outputs the result.
print(time, suffix)
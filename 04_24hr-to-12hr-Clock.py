hr24Input = int(input('Enter the 24 hour number: '))

if hr24Input > 12:
    suffix = 'PM'
    time = hr24Input - 12

elif hr24Input == 12:
    suffix = 'PM'
    time = hr24Input


else:
    suffix = 'AM'
    time = hr24Input

print(time, suffix)


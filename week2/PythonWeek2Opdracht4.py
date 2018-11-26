def mybin(n):
    if n < 0:
        return 'Must be a positive int'
    elif n == 0:
        return '0'
    else:
        return mybin(n//2) + str(n%2)


print(mybin(10))

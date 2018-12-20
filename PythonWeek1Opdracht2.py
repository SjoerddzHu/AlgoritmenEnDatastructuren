def getNumbers(s):
    numberlist = []
    last = False
    for i in s:
        if i.isdigit():
            if last:
                numberlist[len(numberlist) - 1] *= 10
                numberlist[len(numberlist) - 1] += int(i)
            else:
                numberlist.append(int(i))
            last = True
        else:
            last = False
    return numberlist

mystring = "1zin8met9getallen2"
print(getNumbers(mystring))


a = '1zin8met9getallen2'
def getNumbers(s):
    l = []
    for x in range(0,len(s)):
        if s[x].isdigit() == True:
            l.append(int(s[x]))
    return l

print(getNumbers(a))



import random


def swap(input, i, j):
    input[i], input[j] = input[j], input[i]


counter = 0


def qsort(input, low=0, high=-1):
    if high == - 1:
        high = len(input) - 1
    if low < high:
        swap(input, low, random.randint(low, high))
        m = low
        for number in range(low + 1, high + 1):
            if input[number] < input[low]:
                m += 1
                swap(input, m, number)
                # print(input)
                global counter
                counter += 1
                # low < i <= m : a[i] < a[low]
                #  i > m       : a[i] >= a[low]
        swap(input, low, m)
        # print(input)
        counter += 1
        # low <= i < m : a[i] < a[m]
        #  i > m       : a[i] >= a[m]
        if m > 0:
            qsort(input, low, m - 1)
        qsort(input, m + 1, high)
        return input, counter


def createRandomList(length, min, max):
    result = []
    for iterations in range(length):
        result.append(random.randint(min, max))
    return result


count = 0
liste = [9, 8, 7, 6, 5, 12, 456, 3, -123, 4, 3, 2, 1, 0]
listeTenK = createRandomList(10000, -100, 100)
print(liste)
listeSorted = qsort(liste)
print(listeSorted)
print('-------------------------------------------------------------------------------')
print(listeTenK)
listeTenKSorted = qsort(listeTenK)
print(listeTenKSorted)

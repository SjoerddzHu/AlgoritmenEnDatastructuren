import random


def DoubleBirthday(n):
    list = [0] * (365 + 1)
    for x in range(0, n):
        list[random.randint(1, 365)] = list[random.randint(1, 365)] + 1
    for x in range(0, 365):
        if list[x] > 1:
            return 1
    return 0


def CalculateAverage(nmb_tests, people, Function):
    answer = 0.0
    for x in range(0, nmb_tests):
        answer += Function(people)
    return 100 * (answer / float(nmb_tests))


print("The double birthday percentage is:", CalculateAverage(101, 24, DoubleBirthday), "%")

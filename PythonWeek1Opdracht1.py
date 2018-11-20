lijstje = [1,10,9]


def mymax(a):
    assert len(a) != 0, "je element moet wel gevuld zijn!"
    assert a != int or a != float, "het moet wel een getal zijn!"
    Max = 0
    for item in a:
        if item > Max:
            Max = item
    return Max


print( str(mymax(lijstje)))

from random import randint


def x(a, b)
    return tuple(randint(a, b) for _ in range(10))


tpl1 = x(0, 5)
print(tpl1)
tpl2 = x(-5, 0)
print(tpl2)

tpl3 = tpl1 + tpl2
print(tpl3)
tpl4 = tpl3.count(0)
print(tpl4)

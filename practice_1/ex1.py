from math import log, sin

def F(x): # математическое выражение
    return 1 - x + sin(x) - log(1+x)

def bisection(l,r,eps): # метод половинного деления
    while r-l > eps:
        middle = l+(r-l)/2

        if F(l)*F(middle)<=0: # проверка существования корней
            r = middle
        else:
            l = middle

    return (r+l)/2


def chord(l,r,eps): # метод хорд
    prev = l

    while True:
        x = l - F(l) * (r-l) / (F(r)-F(l))

        if abs(x-prev) <= eps:
            return x

        if F(x) * F(r) > 0:
            r = x
        else:
            l = x

        prev = x

EPS = 0.001
l = 0
r = 2

if F(l) * F(r) > 0:
    print('Корней на промежутке нет')
else:
    print(bisection(l,r,EPS))
    print(chord(l,r,EPS))
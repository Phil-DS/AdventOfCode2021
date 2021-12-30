from day17_data import *
import math

def qf(a,b,c):
    disc = math.sqrt(b*b - 4*a*c)
    h = (-b + disc)/(2*a)
    l = (-b - disc)/(2*a)
    return [h,l]

last = []
for i in range(0, 100):
    t = math.floor(max(qf(-0.5, i, -yLow)))
    tHigh = math.floor(max(qf(-0.5, i, -yHigh)))

    s = (i*t - 0.5*t*t)
    if s <= yHigh:
        tHigh = math.floor(max(qf(-0.5, i, -yHigh)))

        last.append(i)

print(last[-1])

height = 0.5*(last[-1]*(last[-1] +1))
print(height)
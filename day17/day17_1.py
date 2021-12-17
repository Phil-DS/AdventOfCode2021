from day17_data import *
import math

# s = ut + 1/2 at^2

# we know that it decreases by 1 to hit the area. As such, we need to know the nearest triangle number to the  

# We assume that its the positive
# xMinLow = -0.5 + math.sqrt(0.5*0.5 - 4*0.5*xHigh)
xMinLow = -0.5 + math.sqrt(0.5*0.5 - 4*0.5*(-xLow))

# # We shall only use the ceil of the low. This gets us the 
# t = math.ceil(tLow)
def qf(a,b,c):
    disc = math.sqrt(b*b - 4*a*c)
    h = (-b + disc)/(2*a)
    l = (-b - disc)/(2*a)
    return h,l

last = []
for i in range(0, 100):
    t = math.floor(max(list(qf(-0.5, i, -yLow))))
    tHigh = math.floor(max(list(qf(-0.5, i, -yHigh))))

    s = (i*t - 0.5*t*t)
    if s <= yHigh:
        tHigh = math.floor(max(list(qf(-0.5, i, -yHigh))))

        last.append(i)
        print('Valid @ ',i)

print(last[-1])

height = 0.5*(last[-1]*(last[-1] +1))
print(height)
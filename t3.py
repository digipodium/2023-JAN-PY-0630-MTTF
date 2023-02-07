# the power of not repeating
from turtle import *

side = 6
for i in range(side):
    pencolor('blue')
    fd(100)
    lt(360/side)
    pencolor('red')
    dot(30)
    for i in range(side):
        fd(50)
        lt(360/side)
mainloop()
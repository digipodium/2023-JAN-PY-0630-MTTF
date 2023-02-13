from turtle import *

def polygon(side, dis):
    for i in range(side):
        fd(dis)
        lt(360/side)

for i in range(3, 100):
    polygon(3, i*10)

hideturtle()
mainloop()
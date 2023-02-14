from turtle import *
speed(0)
def polygon(side, dis):
    for i in range(side):
        fd(dis)
        lt(360/side)

for i in range(100):
    polygon(6, 100)
    lt(25)


hideturtle()
mainloop()
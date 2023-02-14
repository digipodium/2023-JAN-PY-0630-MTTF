from turtle import *
speed('fastest')
pencolor('#8989ff')
pensize(5)
side = 6
for i in range(side):
    fd(100)
    for i in range(side):
        fd(50)
        for i in range(side):
            bk(25)
            for i in range(side):
                fd(50)
                rt(360/side)
            rt(360/side)            
        lt(360/side)
    rt(360/side)
hideturtle()
mainloop()
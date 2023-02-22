import pgzrun

WIDTH = 1000
HEIGHT = 800

box = Rect((50,50), (150, 100))
box2 = Rect((600,50), (100,100))
bvx = 4
b2vx = -3

def draw():
    screen.fill('black')
    screen.draw.filled_rect(box, 'yellow')
    screen.draw.filled_rect(box2, 'red')

def update():
    global bvx, b2vx
    box.x += bvx
    box2.x += b2vx
    # check for collision
    if box.colliderect(box2):
        bvx = -bvx
        b2vx = -b2vx
        sounds.hat.play()
    # check for wall collision box
    if box.left < 0:
        bvx = -bvx
        sounds.cling.play()

    # check for wall collision of box2
    if box2.right > 800:
        b2vx = -b2vx
        sounds.hat.play()

    

pgzrun.go()
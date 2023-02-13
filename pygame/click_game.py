from random import randint

white = [255, 255, 255]
red = [255, 0, 0]

astronaut = Actor('astronaut')
astronaut.pos = (20, 20)

coin = Actor('coin')
coin.pos = (30, 30)

WIDTH = 500
HEIGHT = 500
vel = 5

def draw():
    screen.clear()
    screen.fill('black')
    astronaut.draw()
    coin.draw()


def update():
    move_left(2)


def on_mouse_down(pos):
    if astronaut.collidepoint(pos):
        print("Ouch")
    else:
        print("You're bad!")
        quit()


astronaut.x = randint(10, 800)
astronaut.y = randint(10, 800)

def move_right(speed):
    astronaut.left += speed
    if astronaut.left > WIDTH:
        astronaut.right = 0

def move_left(speed):
    astronaut.left += speed
    if astronaut.left > WIDTH:
        astronaut.right = 0


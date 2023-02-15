from random import randint

white = [255, 255, 255]
red = [255, 0, 0]

astronaut = Actor('astronaut')
astronaut.pos = (20, 20)

coin = Actor('coin')
coin.pos = (30, 30)

WIDTH = 1000
HEIGHT = 1000
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

def time_up():
    pass

clock.schedule(time_up, 7.0)


astronaut.x = randint(10, 800)
astronaut.y = randint(10, 800)
coin.x = randint(10, 800)

def move_right(vel):
    astronaut.left += vel
    if astronaut.left > WIDTH:
        astronaut.right = 0

def move_left(vel):
    astronaut.left += vel
    if astronaut.left > WIDTH:
        astronaut.right = 0


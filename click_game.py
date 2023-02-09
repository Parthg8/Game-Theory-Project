from random import randint
Astronaut = Actor('astronaut')

WIDTH = 300
HEIGHT = 300

def draw():
    screen.fill((128, 0, 0))
    screen.clear()
    Astronaut.draw()

Astronaut.pos = 100, 100

WIDTH = 500
HEIGHT = Astronaut.height + 400


Astronaut.topright = 0, 10


def update():
    Astronaut.left += 2
    if Astronaut.left > WIDTH:
        Astronaut.right = 0

def on_mouse_down(pos):
    if Astronaut.collidepoint(pos):
        print("Ouch")
    else:
        print("You're bad!")
        quit()


Astronaut.x = randint(10, 800)
Astronaut.y = randint(10, 600)

from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 799), 599
        self.speed = random.randint(6, 10)
        self.image = load_image('ball21x21.png')

    def update(self):
        self.y = self.y - self.speed
        if self.y <= 60:
            self.y = 60

    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

boy = Boy()
grass = Grass()
ball = Ball()

team = [Boy() for i in range(11)]
ballrange = [Ball() for j in range(20)]

running = True
# game main loop code
while running:
    handle_events()

    for boy in team:
        boy.update()

    for ball in ballrange:
        ball.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()

    for ball in ballrange:
        ball.draw()

    update_canvas()

    delay(0.05)
# finalization code
close_canvas()
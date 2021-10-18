from pico2d import *
import random
open_canvas()
# Game object class here
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.image = load_image('run_animation.png')
        self.frame = random.randint(0,7)

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        
    def update(self):
        self.x += 3
        self.frame = (self.frame + 1) % 8
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Ball:
    def __init__(self, isbig):
        if isbig == 0:
            self.xs = 41
            self.ys = 41
            self.img = load_image('ball41x41.png')
        else:
            self.xs = 21
            self.ys = 21
            self.img = load_image('ball21x21.png')
        self.xpos = random.randint(0,799)
        self.ypos = 599 - self.ys / 2
        self.ydown = random.randint(2,15)
    def draw(self):
        self.img.draw_to_origin(self.xpos, self.ypos)
    def fall(self):
        if self.ypos - self.ydown <= 48:
            self.ypos = 48
        else:
            self.ypos -= self.ydown


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
running = True
grass = Grass() # initialize
team = [Boy() for i in range(11)]
balls = [Ball(random.randint(0,1)) for i in range(20)]
# game main loop code
while(running):    
    handle_events()

    # game logic
    for boy in team:
        boy.update()
    for ball in balls:
        ball.fall()
    # game drawing
    clear_canvas()
    for boy in team:
        boy.draw()

    for ball in balls:
        ball.draw()
    grass.draw()
    update_canvas()
    delay(0.05)
# finalization code
close_canvas()
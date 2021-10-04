from pico2d import *


KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dirx
    global viewdir
    global destx, desty, x, y
    global clickmove
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            destx = event.x
            desty = KPU_HEIGHT - event.y
            if destx > x:
                viewdir = 1
            else:
                viewdir = -1
            clickmove = True
        if event.type == SDL_QUIT:
            running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
cursor = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')
running = True
destx = 0
desty = 0
clickmove = False

x = 800 // 2
y = 90
frame = 0
frate = 0
dirx = 0 # -1 left, +1 right
diry = 0
viewdir = 1 # -1 left, +1 right
hide_cursor()
while running:
    clear_canvas()
    if clickmove:
        dirx = (destx - x) / 20
        diry = (desty - y) / 20
        if dirx < 0.1 and dirx > -0.1 and diry < 0.1 and diry > -0.1:
            clickmove = False
            dirx = 0
            diry = 0

    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursor.draw(destx, desty)
    if dirx>0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif dirx<0: 
        character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)
    else:
        if viewdir == 1:
           character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)
        elif viewdir == -1:
             character.clip_composite_draw(frame * 100, 100 * 3, 100, 100, 0, 'h', x, y, 100, 100)


    update_canvas()

    handle_events()
    frate += 1
    if frate==3:
        frame = (frame + 1) % 8
        frate=0
    x += dirx
    y += diry
    delay(0.01)

close_canvas()


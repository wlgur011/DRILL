from pico2d import *


def handle_events():
    global running
    global dir
    global viewdir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        if event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                viewdir = 1
            elif event.key == SDLK_LEFT:
                dir += 1
                viewdir = -1


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
character_stop = load_image('character.png')
running = True
x = 800 // 2
frame = 0
dir = 0 # -1 left, +1 right
viewdir = 1 # -1 left, +1 right
while running:
    clear_canvas()
    grass.draw(400, 30)
    if dir>0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, 90)
    elif dir<0: 
        character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, 90, 100, 100)
    else:
        if viewdir == 1:
            character_stop.draw(x,90)
        elif viewdir == -1:
             character_stop.composite_draw(0,'h', x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dir * 5
    delay(0.01)

close_canvas()


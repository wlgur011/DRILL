from pico2d import *

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, DASH, DASH_DONE = range(7)
# fill here

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_RSHIFT): DASH,
    (SDL_KEYDOWN, SDLK_LSHIFT): DASH,
    (SDL_KEYUP, SDLK_RSHIFT): DASH_DONE,
    (SDL_KEYUP, SDLK_LSHIFT): DASH_DONE
}



# Boy States
class IdleState:
    def enter(boy, event):
        
        
        boy.timer = 1000
    def exit(boy, event):
        pass
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        if boy.timer == 0:
            boy.add_event(SLEEP_TIMER)
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)

class RunState:
    def enter(boy, event):
        if boy.velocity == 2 or boy.velocity == -2:
            boy.velocity /= 2
        if event == RIGHT_DOWN:
            boy.velocity = 1
            boy.dir = boy.velocity
        elif event == LEFT_DOWN:
            boy.velocity = -1
            boy.dir = boy.velocity
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        
    def exit(boy, event):
        pass
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 800 - 25)
        
    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)

class SleepState:

    def enter(boy, event):
        boy.frame = 0
    def exit(boy, event):
        pass
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(boy.frame * 100, 200, 100, 100, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)

class DashState:
    def enter(boy, event):
        boy.stamina = 100
        if(boy.velocity==1 or boy.velocity==-1):
            boy.velocity *= 2
        
    def exit(boy, event):
        pass
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 800 - 25)
        boy.stamina -= 1
        if boy.stamina == 0:
            boy.add_event(DASH_DONE)
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)

# fill here

next_state_table = {
    IdleState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
    RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
    SLEEP_TIMER: SleepState, DASH: IdleState, DASH_DONE: IdleState},

    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
    LEFT_DOWN: RunState, RIGHT_DOWN: RunState, DASH: DashState, DASH_DONE: RunState},

    SleepState: {RIGHT_UP: RunState, LEFT_UP: RunState,
    LEFT_DOWN: RunState, RIGHT_DOWN: RunState, DASH: SleepState, DASH_DONE: SleepState},

    DashState: {
        RIGHT_UP: IdleState, LEFT_UP: IdleState,
    LEFT_DOWN: DashState, RIGHT_DOWN: DashState, DASH: DashState, DASH_DONE: RunState
    }
}







class Boy:
    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.timer = 0
        self.stamina = 0
        self.event_queue = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        pass


    def change_state(self,  state):
        # fill here
        pass


    def add_event(self, event):
            self.event_queue.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_queue) > 0:
            event = self.event_queue.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)


    def draw(self):
        self.cur_state.draw(self)
        debug_print('Velocity :' + str(self.velocity) + ' Dir:' + str(self.dir))
        pass


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        pass


from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def road_resources():
    global TUK_ground, character
    global arrow

    arrow= load_image('hand_arrow.png')
    TUK_ground = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


def reset_world():
    global running, x, y, frame
    global hx, hy
    running = True
    x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
    frame = 0

    hx, hy = random.randint(0, TUK_WIDTH - 1), random.randint(0, TUK_HEIGHT - 1)
    # hx, hy = TUK_WIDTH - 50, TUK_HEIGHT - 50

def render_world():
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    arrow.draw(hx, hy)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()


def update_world():
    global frame
    frame = (frame + 1) % 8


open_canvas(TUK_WIDTH, TUK_HEIGHT)
hide_cursor()
road_resources()
reset_world()

while running:
    render_world()
    handle_events()
    update_world()

close_canvas()

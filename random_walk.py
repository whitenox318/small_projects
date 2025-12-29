from sys import argv
from random import randint, choice

from sdl2 import *


WIDTH = 900
HEIGHT = 600
RECT_SIZE = 3
MOVEMENT_SCALE = 3


class Walker:
    def __init__(self, color):
        self.color = color

    x = WIDTH//2
    y = HEIGHT//2


def get_random_v():
    choice = randint(0, 3)
    match choice:
        case 0:
            return 0, RECT_SIZE
        case 1:
            return 0, -RECT_SIZE
        case 2:
            return RECT_SIZE, 0
        case 3:
            return -RECT_SIZE, 0


def get_random_color() -> int:
    choices = ['0', 'F']
    res = '0x'
    for i in range(6):
        res += choice(choices)
    if res.count('F') < 2:
        return get_random_color()
    return int(res, 16)


def move_walker(surface: SDL_Surface, walker: Walker):
    random_vector = get_random_v()
    for i in range(MOVEMENT_SCALE):
        walker.x += random_vector[0]
        walker.y += random_vector[1]
        rect = SDL_Rect(walker.x, walker.y, RECT_SIZE, RECT_SIZE)
        SDL_FillRect(surface, rect, walker.color)


def main(argc: int, argv: list[str]) -> int:
    walkers_num = 4
    if argc == 1:
        walkers_num = 4
    elif argc == 2:
        walkers_num = int(argv[1])
    else:
        print(f'Usage: {argv[0]} <walkers_num>')

    window = SDL_CreateWindow(bytes('Random Walk', 'utf-8'), SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, WIDTH, HEIGHT, 0)
    surface = SDL_GetWindowSurface(window)
    walkers = [Walker(get_random_color()) for _ in range(walkers_num)]

    app_running = True
    event = SDL_Event()
    while app_running:
        while SDL_PollEvent(event):
            if event.type == SDL_QUIT:
                app_running = False

        for walker in walkers:
            move_walker(surface, walker)
        SDL_UpdateWindowSurface(window)
        SDL_Delay(20)


if __name__ == '__main__':
    main(len(argv), argv)

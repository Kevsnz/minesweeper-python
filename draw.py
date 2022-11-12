import pygame
import pygame.image
from pygame import Surface

import field

border_tl: Surface
border_tr: Surface
border_tm: Surface
border_tf: Surface
border_l: Surface
border_r: Surface
border_bl: Surface
border_b: Surface
border_br: Surface

face_normal: Surface
face_cool: Surface
face_oh: Surface
face_dead: Surface

numbers: list[pygame.Surface]
tile_hidden: Surface
tile_flag: Surface
tiles: list[pygame.Surface]


def load_assets():
    global border_tl, border_tr, border_tm, border_tf, border_l, border_r, border_bl, border_b, border_br
    border_tl = pygame.image.load('assets/border_top_left.png')
    border_tr = pygame.image.load('assets/border_top_right.png')
    border_tm = pygame.image.load('assets/border_top_mid.png')
    border_tf = pygame.image.load('assets/border_top_fill.png')

    border_l = pygame.image.load('assets/border_left.png')
    border_r = pygame.image.load('assets/border_right.png')
    border_bl = pygame.image.load('assets/border_bottom_left.png')
    border_b = pygame.image.load('assets/border_bottom.png')
    border_br = pygame.image.load('assets/border_bottom_right.png')

    global face_normal, face_cool, face_oh, face_dead
    face_normal = pygame.image.load('assets/face_n.png')
    face_cool = pygame.image.load('assets/face_c.png')
    face_oh = pygame.image.load('assets/face_o.png')
    face_dead = pygame.image.load('assets/face_x.png')

    global numbers
    numbers = [
        pygame.image.load('assets/number_0.png'),
        pygame.image.load('assets/number_1.png'),
        pygame.image.load('assets/number_2.png'),
        pygame.image.load('assets/number_3.png'),
        pygame.image.load('assets/number_4.png'),
        pygame.image.load('assets/number_5.png'),
        pygame.image.load('assets/number_6.png'),
        pygame.image.load('assets/number_7.png'),
        pygame.image.load('assets/number_8.png'),
        pygame.image.load('assets/number_9.png'),
    ]

    global tile_hidden, tile_flag, tiles
    tile_hidden = pygame.image.load('assets/tile_hidden.png')
    tile_flag = pygame.image.load('assets/tile_flag.png')
    tiles = [
        pygame.image.load('assets/tile_0.png'),
        pygame.image.load('assets/tile_1.png'),
        pygame.image.load('assets/tile_2.png'),
        pygame.image.load('assets/tile_3.png'),
        pygame.image.load('assets/tile_4.png'),
        pygame.image.load('assets/tile_5.png'),
        pygame.image.load('assets/tile_6.png'),
        pygame.image.load('assets/tile_7.png'),
        pygame.image.load('assets/tile_8.png'),
        pygame.image.load('assets/tile_boom.png'),
        pygame.image.load('assets/tile_mine.png'),
    ]


_screen: pygame.Surface = None


def set_screen(field_width: int, field_height: int):
    global _screen
    scr_w, scr_h = field_width * 16 + 4 * 2, field_height * 16 + 4 + 40
    _screen = pygame.display.set_mode((scr_w, scr_h), pygame.SCALED | pygame.RESIZABLE)


def draw_screen():
    draw_borders(_screen)
    draw_field(_screen)
    draw_mine_count(_screen)
    draw_timer(_screen)


def draw_borders(screen: pygame.Surface):
    w, h = field.get_field_width(), field.get_field_height()
    scr_w, scr_h = screen.get_size()

    # draw corners
    screen.blit(border_tl, (0, 0))
    screen.blit(border_tr, (scr_w - 52, 0))
    screen.blit(border_bl, (0, scr_h - 4))
    screen.blit(border_br, (scr_w - 4, scr_h - 4))

    for y in range(h):
        screen.blit(border_l, (0, y * 16 + 40))
        screen.blit(border_r, (scr_w - 4, y * 16 + 40))

    for x in range(w):
        screen.blit(border_b, (x * 16 + 4, scr_h - 4))
        if 3 <= x < w - 3:
            screen.blit(border_tf, (x * 16 + 4, 0))

    screen.blit(border_tm, (scr_w // 2 - 16, 0))


def draw_field(screen: pygame.Surface):
    ...


def draw_mine_count(screen: pygame.Surface):
    ...


def draw_timer(screen: pygame.Surface):
    ...


def draw_number(screen: pygame.Surface, number: int, x: int, y: int):
    ...
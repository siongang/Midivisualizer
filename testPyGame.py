import pygame as pg
from midiParser import instruments



pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True
dt = 0

player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pg.draw.circle(screen, "red", player_pos, 40)

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        player_pos.y -= 5
    if keys[pg.K_s]:
        player_pos.y += 300 * dt
    if keys[pg.K_a]:
        player_pos.x -= 300 * dt
    if keys[pg.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pg.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(120) / 1000
    print(dt)

pg.quit()
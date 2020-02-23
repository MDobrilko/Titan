import pygame as pg

pg.init()
win = pg.display.set_mode((500, 500))

pg.display.set_caption('Cubes Game')

x = 50
y = 50
width = 40
height = 60
speed = 20

run = True

while run:
    pg.time.delay(50)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    keys = pg.key.get_pressed()
    if keys[pg.K_s] and y < 500 - height - speed:
        y += speed
    if keys[pg.K_a] and x > speed:
        x -= speed
    if keys[pg.K_d] and x < 500 - width - speed:
        x += speed
    if keys[pg.K_w] and y > speed:
        y -= speed


    win.fill((0, 0 ,0))
    pg.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pg.display.update()

pg.quit()
import pygame as pg
import random
import sys

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60

pg.init()
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

GRAVITY = 0.5
JUMP = -1
PLATFORM_WIDTH = 105
MIN_GAP = 90
MAX_GAP = 180
pg.display.set_caption("Nya")
font_xl = pg.font.Font(None, 96)

class BasicSprite(pg.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.image = pg.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))

class Sprite(pg.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pg.image.load(image_path)
        self.rect = self.image.get_rect(center=(x, y))
        self.dead = False
    def update(self):
        super().update()
    def draw(self):
        screen.blit(self.image, self.rect)
    def kill(self):
        self.dead = True
        super().kill()


class Cat(Sprite):
    def __init__(self):
        super().__init__(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 'cat.bmp')
        self.image = pg.image.load('cat.bmp')
        self.image = pg.transform.scale(self.image, (150, 150))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(150, 500))
        self.speed = 0

    def update(self):
        if self.dead:
            return
        JUMP = -0.75
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.speed += JUMP
        if keys[pg.K_e]:
            new_fish = Fish(self.rect.y)
            new_fish.add()
        self.speed += GRAVITY
        self.rect.y += self.speed
        JUMP = -0.8
        if self.rect.y >= 455:
            self.speed += JUMP

    def draw(self):
        screen.blit(self.image, self.rect)

cat = Cat()
ycoord = cat.rect.y
class Fish(Sprite):
    def __init__(self, ycoord):
        super().__init__(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 'fish.bmp')
        self.image = pg.image.load('fish.bmp')
        self.image = pg.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect(center=(150, ycoord))
        self.speed = 12
    def update(self):
        self.update()
        if pg.key.get_pressed()[pg.K_e]:
            self.add()

    def draw(self):
        self.draw()
        screen.blit(self.image, self.rect)
    def on_collision(self, cube):
        self.kill()

fish = Fish(ycoord=cat.rect.y)
class Cube():
    def __init__(self, sprite):
        self.sprites = pg.sprite.Group()
        for _ in range(5):
            sprite = BasicSprite('black', random.randint(500, 800), random.randint(0, 600), 70, 70)
            self.sprites.add(sprite)
    def on_collision(self):
        pg.mixer.Sound('bruh-sound-effect-2.mp3')
        self.kill

cube = Cube(pg.sprite.Group)


def main():
    while True:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                return

        if cube.sprites == 0:
            cube.sprites.add()
        cat.update()
        cube.sprites.update()


        screen.fill('white')
        cat.draw()
        cube.sprites.draw(screen)


        pg.display.update()

        pg.time.delay(1000 // FPS)

if __name__ == '__main__':
    main()
    pg.quit()
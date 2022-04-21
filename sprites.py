from pygame import *
from settings import *
import sys, math
init()

class Player(sprite.Sprite):

    def __init__(self, game, pos, vel, mass, color, radius):
        self.groups = game.all_sprites, game.players
        sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = Surface([radius*2,radius*2])
        self.rect = self.image.get_rect()
        self.color = color
        self.x = pos[0]
        self.y = pos[1]
        self.mass = mass
        self.radius = radius
        self.image.fill(grey)
        draw.circle(self.image, self.color, self.rect.center, self.radius)
        self.velocity = vel


    def move(self):
        self.gravity()
        self.collide()
        self.x += self.velocity[0]
        self.y += self.velocity[1]


    def collide(self):
        for s in self.game.players:
            if s != self:
                if sprite.collide_circle(self,s):
                    return True
            else:
                return False

    def gravity(self):
        for sprite in self.game.players:
            if sprite != self:
                difX = self.x - sprite.x
                difY = self.y - sprite.y
                distance = math.sqrt(difX**2 + difY**2)
                forceMag = (sprite.mass * self.mass * 384) / (distance ** 2)
                angle = (math.degrees(math.atan2(difY,difX)) - 180) * -1
                accX = int(forceMag * math.cos(math.radians(angle)) / self.mass)
                accY = int(forceMag * math.sin(math.radians(angle)) / self.mass) * -1
                self.accelerate(accX,accY)

    def accelerate(self, ddx=0, ddy=0):
        self.velocity[0] += ddx / 240
        self.velocity[1] += ddy / 240


    def checkWall(self):
        if self.x + self.radius + self.velocity[0] > width or self.x - self.radius + self.velocity[0] < 0:
            self.velocity[0]  *= -1
        elif self.y + self.radius + self.velocity[1] > height or self.y - self.radius + self.velocity[1] < 0:
            self.velocity[1] *= -1

    def update(self):
        if self.collide():
            self.kill()
        self.move()
        self.rect.center = [self.x, self.y]

class Button(sprite.Sprite):
    def __init__(self, game, pos):
        self.groups = game.buttons, game.all_sprites
        sprite.Sprite.__init__(self, self.groups)

        self.image = Surface((100,80))
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.image.fill(white)
        draw.rect(self.image, red, self.rect, 5)

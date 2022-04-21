from pygame import *
from sprites import *
from settings import *
import sys

class Game:
    def __init__(self):
        init()
        self.window = display.set_mode((width,height))
        display.set_caption(title)
        self.clock = time.Clock()
        self.load_data()
        key.set_repeat(10,10)

    def load_data(self):
        pass

    def new(self):
        self.all_sprites = sprite.Group()
        self.players = sprite.Group()
        self.buttons = sprite.Group()
        self.p = Player(self, [500,450], [0,0], 25000, red, 40)
        self.q = Player(self, [100,450], [0,10], 100, blue, 20)
        self.h = Player(self, [700, 450], [0,-15], 100, green, 10)
        self.j = Player(self, [600,450], [0,-20], 50, magenta, 12)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def quit(self):
        quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.window.fill(grey)
        self.all_sprites.draw(self.window)
        display.flip()

    def events(self):
        for e in event.get():
            if e.type == QUIT:
                self.quit()

            '''
                if e.type == KEYDOWN:
                    if e.key == K_w:
                        self.p.move(dx=0,dy=-5)
                    if e.key == K_s:
                        self.p.move(dx=0,dy=5)
                    if e.key == K_d:
                        self.p.move(dx=5,dy=0)
                    if e.key == K_a:
                        self.p.move(dx=-5,dy=0)

                    '''


    def show_start_screen(self):
        pass



g = Game()
g.show_start_screen()
g.new()
g.run()

#!/usr/bin/env python3

#imports
import random, os.path, pygame
from pygame.locals import *

#game constants
MAX_SHOTS = 3 #max player shots allowed on screen at once
ENEMY_ODDS = 22 #chances of spawning a new enemy
BOMB_ODDS = 60 #chances of dropping a new bomb
SCREEN_RECT = Rect(0, 0, 640, 480)
GROUND_HEIGHT = 470
SCORE = 0
PAUSED = False

#main directory filepath
main_dir = os.path.split(os.path.abspath(__file__))[0]

#loads image resources
def load_image(file):
    file = os.path.join(main_dir, 'data', file)
    try:
        surface = pygame.image.load(file)
        return surface.convert_alpha()
    except pygame.error:
        raise SystemExit('Could not load image: "%s" %s' % (file,
        pygame.get_error()))

#loads sound resources
def load_sound(file):
    file = os.path.join(main_dir, 'data', file)
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        raise SystemExit('Could not load sound: "%s" %s' % (file,
        pygame.get_error()))

#pauses game
def pause(screen, background):
    pause_text = pygame.font.SysFont(None, 85)
    text_surface = pause_text.render('Paused', True, (10, 10, 10))
    text_rect = text_surface.get_rect()
    text_rect.center = ((SCREEN_RECT.width / 2), (SCREEN_RECT.height / 2))
    screen.fill((160, 160, 160))
    screen.blit(text_surface, text_rect)
    while PAUSED:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN
            and event.key == K_ESCAPE):
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_p:
                screen.blit(background, (0, 0))
                unpause()
        pygame.display.update()

#unpauses game
def unpause():
    global PAUSED
    PAUSED = False

#player class
class Player(pygame.sprite.Sprite):

    #player class variables
    speed = 8
    bounce = 24
    gun_offset = 12
    images = []

    #player initializer
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=SCREEN_RECT.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = 1

    def move(self, direction):
        if direction: self.facing = direction
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(SCREEN_RECT)
        if direction > 0:
            self.image = self.images[0]
        elif direction < 0:
            self.image = self.images[1]
        self.rect.top = self.origtop - (self.rect.left // self.bounce % 2)

    def gun_position(self):
        position = self.facing * self.gun_offset + self.rect.centerx
        return position, self.rect.top

#enemy class
class Enemy(pygame.sprite.Sprite):

    #enemy class variables
    speed = 12
    cycle = 8
    images = []

    #enemy initializer
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.facing = random.choice((-1, 1)) * Enemy.speed
        self.frame = 0
        if self.facing < 0:
            self.rect.right = SCREEN_RECT.right

    def update(self):
        self.rect.move_ip(self.facing, 0)
        if not SCREEN_RECT.contains(self.rect):
            self.facing = -self.facing
            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(SCREEN_RECT)
        self.frame = self.frame + 1
        self.image = self.images[self.frame // self.cycle % 3]

#explosion class
class Explosion(pygame.sprite.Sprite):

    #explosion class variables
    defaultLife = 12
    cycle = 3
    images = []

    #explosion initializer
    def __init__(self, actor):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life = self.defaultLife

    def update(self):
        self.life = self.life - 1
        self.image = self.images[self.life // self.cycle % 2]
        if self.life <= 0: self.kill()

#shot class
class Shot(pygame.sprite.Sprite):

    #shot class variables
    speed = -10
    images = []

    #shot initializer
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=position)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0:
            self.kill()

#bomb class
class Bomb(pygame.sprite.Sprite):

    #bomb class variables
    speed = 6
    images = []

    def __init__(self, enemy):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=
        enemy.rect.move(0, 5).midbottom)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= GROUND_HEIGHT:
            Explosion(self)
            self.kill()

#score class
class Score(pygame.sprite.Sprite):

    #score initializer
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 20)
        self.font.set_bold(1)
        self.color = Color('#383838')
        self.lastscore = -1
        self.update()
        self.rect= self.image.get_rect().move(10, GROUND_HEIGHT - 20)

    def update(self):
        if SCORE != self.lastscore:
            self.lastscore = SCORE
            message = 'Score: %d' % SCORE
            self.image = self.font.render(message, 0, self.color)

#main game function
def main(windowstyle=0):

    #initialize pygame
    pygame.init()

    #set display
    fullscreen = False
    windowstyle = 0
    bestdepth = pygame.display.mode_ok(SCREEN_RECT.size, windowstyle, 32)
    screen = pygame.display.set_mode(SCREEN_RECT.size, windowstyle, bestdepth)

    #load images
    img = load_image('player.png')
    Player.images = [img, pygame.transform.flip(img, 1, 0)]
    img = load_image('explosion.png')
    Explosion.images = [img, pygame.transform.flip(img, 1, 1)]
    Enemy.images = [load_image('enemy1.png'), load_image('enemy2.png'),
    load_image('enemy3.png')]
    Bomb.images = [load_image('bomb.png')]
    Shot.images = [load_image('shot.png')]

    #customize game window
    icon = pygame.transform.scale(Enemy.images[1], (32, 32))
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Alien Blaster')
    pygame.mouse.set_visible(0)

    #create background
    backgroundimg = load_image('background.png')
    background = pygame.Surface(SCREEN_RECT.size)
    for i in range(0, SCREEN_RECT.width, backgroundimg.get_width()):
        background.blit(backgroundimg, (i, 0))
    screen.blit(background, (0, 0))
    pygame.display.flip()

    #load sounds
    bomb_sound = load_sound('bomb.wav')
    shot_sound = load_sound('shot.wav')

    #create game groups
    enemies = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    bombs = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()
    lastenemy = pygame.sprite.GroupSingle()

    #set default groups for sprite classes
    Player.containers = all
    Enemy.containers = enemies, all, lastenemy
    Shot.containers = shots, all
    Bomb.containers = bombs, all
    Explosion.containers = all
    Score.containers = all

    #starting values
    global PAUSED
    global score
    enemyreload = 20
    kills = 0
    clock = pygame.time.Clock()

    #starting sprites
    global SCORE
    player = Player()
    Enemy()
    if pygame.font:
        all.add(Score())

    #main game loop
    while player.alive():

        #increase difficulty after certain score
        if SCORE >= 30:
            Enemy.speed = 15
            Bomb.speed = 7
        if SCORE >= 50:
            Enemy.speed = 18
            Bomb.speed = 8
        if SCORE >= 75:
            Enemy.speed = 20
            Bomb.speed = 9
        if SCORE >= 100:
            Enemy.speed = 22
            Bomb.speed = 10

        #consume input events
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN
            and event.key == K_ESCAPE):
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_p:
                PAUSED = True
                pause(screen, background)

        #clear and update sprites
        all.clear(screen, background)
        all.update()

        #handle player movement input
        keystate = pygame.key.get_pressed()
        direction = keystate[K_RIGHT] - keystate[K_LEFT]
        player.move(direction)
        firing = keystate[K_SPACE]
        if not player.reloading and firing and len(shots) < MAX_SHOTS:
            Shot(player.gun_position())
            shot_sound.play()
        player.reloading = firing

        #create new enemy
        if enemyreload:
            enemyreload = enemyreload - 1
        elif not int(random.random() * ENEMY_ODDS):
            Enemy()
            enemyreload = 20
            if SCORE >= 20:
                enemyreload -= 3
            if SCORE >= 30:
                enemyreload -= 3
            if SCORE >= 50:
                enemyreload -= 3
            if SCORE >= 75:
                enemyreload -= 2
            if SCORE >= 100:
                enemyreload -= 2

        #drop bombs
        if lastenemy and not int(random.random() * BOMB_ODDS):
            Bomb(lastenemy.sprite)

        #detect collisions
        for enemy in pygame.sprite.spritecollide(player, enemies, 1):
            bomb_sound.play()
            Explosion(enemy)
            Explosion(player)
            SCORE = SCORE + 1
            player.kill()
        for enemy in pygame.sprite.groupcollide(shots, enemies, 1, 1).keys():
            bomb_sound.play()
            Explosion(enemy)
            SCORE = SCORE + 1
        for bomb in pygame.sprite.spritecollide(player, bombs, 1):
            bomb_sound.play()
            Explosion(player)
            Explosion(bomb)
            player.kill()

        #draw the scene
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        #set framerate cap
        clock.tick(40)

    #close game
    pygame.time.wait(1000)
    pygame.quit()

#call the main function when run
if __name__ == '__main__': main()

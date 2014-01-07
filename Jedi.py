import random, pygame, sys, time, math
from pygame.locals import *

pygame.display.set_caption('Return of the Jedi')
pygame.font.init()
pygame.mixer.init()
sfx = pygame.mixer.Sound('boom.wav')
pygame.mixer.music.load('Infinity.ogg')
pygame.mixer.music.play(-1, 0.0)
screen_font = pygame.font.Font(None, 40)

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
GRAY =  (128, 128, 128)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
FPS = 60
level = 1
score = 1500

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Return of the Jedi')
    while True:
        runGame()

class Background_1(object):

    def __init__(self, coords = (0,0,0,0)):
        self.death_star = pygame.image.load('Death_star.png')
        self.death_star.set_colorkey(WHITE)
        self.field_up = False
        self.hole_up = False
        self.gameover = False
        self.win = False
        self.hole_coords = coords
        self.font_obj1 = screen_font.render('You win!', True, BLACK)
        self.font_obj2 = screen_font.render('You suck. Loser.', True, BLACK)
        self.font_rect1 = self.font_obj1.get_rect(center = DISPLAYSURF.get_rect().center)
        self.font_rect1.move_ip(0,-25)
        self.font_rect2 = self.font_obj2.get_rect(center = DISPLAYSURF.get_rect().center)

    def draw(self):
        if self.gameover:
            if self.win:
                DISPLAYSURF.fill(GREEN)
                DISPLAYSURF.blit(self.font_obj1, self.font_rect1)
                temp = screen_font.render('Score: ' + str(score), True, BLACK)
                temp_rect = temp.get_rect(center = DISPLAYSURF.get_rect().center)
                DISPLAYSURF.blit(temp, temp_rect.move(0,25))
            else:
                DISPLAYSURF.fill(RED)
                DISPLAYSURF.blit(self.font_obj2, self.font_rect2)
        else:
            pygame.draw.rect(DISPLAYSURF, BLACK, (0, 195, 800, 405))
            pygame.draw.rect(DISPLAYSURF, GRAY, (0, 50, 800, 145))
            pygame.draw.rect(DISPLAYSURF, (50,50,50), (0, 188, 800, 7))

            pygame.draw.line(DISPLAYSURF, BLACK, (0, 60), (800,60), 2)
            pygame.draw.line(DISPLAYSURF, BLACK, (0, 80), (800,80), 3)
            pygame.draw.line(DISPLAYSURF, BLACK, (0, 105), (800,105), 4)
            pygame.draw.line(DISPLAYSURF, BLACK, (0, 130), (800,130), 5)
            pygame.draw.line(DISPLAYSURF, BLACK, (0, 160), (800,160), 5)

            pygame.draw.line(DISPLAYSURF, BLACK, (-355, 195), (400, -50), 3)
            pygame.draw.line(DISPLAYSURF, BLACK, (-225, 195), (400, -50), 3)
            pygame.draw.line(DISPLAYSURF, BLACK, (-100, 195), (400, -50), 3)
            pygame.draw.line(DISPLAYSURF, BLACK, (25, 195), (400, -50), 3)
            pygame.draw.line(DISPLAYSURF, BLACK, (150, 195), (400, -50), 3)
            pygame.draw.line(DISPLAYSURF, BLACK, (275, 195), (400, -50), 3)
            pygame.draw.line(DISPLAYSURF, BLACK, (400, 195), (400, -50), 3)
            pygame.draw.line(DISPLAYSURF, BLACK, (525, 195), (400, -50), 3)
            pygame.draw.line(DISPLAYSURF, BLACK, (650, 195), (400, -50), 3)
            pygame.draw.line(DISPLAYSURF, BLACK, (775, 195), (400, -50), 3)
            pygame.draw.line(DISPLAYSURF, BLACK, (900, 195), (400, -50), 3)
            pygame.draw.line(DISPLAYSURF, BLACK, (1025, 195), (400, -50), 3)
            pygame.draw.line(DISPLAYSURF, BLACK, (1150, 195), (400, -50), 3)

            if self.field_up:
                pygame.draw.line(DISPLAYSURF, BLUE, (0, 200), (800,200), random.randrange(4)+6)
            if self.hole_up:
                pygame.draw.ellipse(DISPLAYSURF, BLACK, self.hole_coords)

            DISPLAYSURF.blit(self.death_star, (600,10))
            DISPLAYSURF.blit(screen_font.render('Score: ' + str(score), True, WHITE), (600, 550))

    def gamelose(self):
        self.gameover = True        

    def gamewin(self):
        self.gameover = True
        self.win = True

class Background_2(object):
    def __init__(self, coords = (0,0,0,0)):
        global score
        score = score*10
        self.gameover = False
        self.win = False
        self.font_obj1 = screen_font.render('You win!', True, BLACK)
        self.font_obj2 = screen_font.render('You suck. Loser.', True, BLACK)
        self.font_rect1 = self.font_obj1.get_rect(center = DISPLAYSURF.get_rect().center)
        self.font_rect1.move_ip(0,-25)
        self.font_rect2 = self.font_obj2.get_rect(center = DISPLAYSURF.get_rect().center)
        self.stars = list()

    def draw(self, Falcon):
        if self.gameover:
            if self.win:
                DISPLAYSURF.fill(GREEN)
                DISPLAYSURF.blit(self.font_obj1, self.font_rect1)
                temp = screen_font.render('Score: ' + str(score), True, BLACK)
                temp_rect = temp.get_rect(center = DISPLAYSURF.get_rect().center)
                DISPLAYSURF.blit(temp, temp_rect.move(0,25))
            else:
                DISPLAYSURF.fill(RED)
                DISPLAYSURF.blit(self.font_obj2, self.font_rect2)
        else:
            pygame.draw.rect(DISPLAYSURF, BLACK, (0, 0, 800, 600))
            for star in self.stars:
                pygame.draw.circle(DISPLAYSURF, WHITE, star, 2)
            DISPLAYSURF.blit(screen_font.render('Score: ' + str(score), True, WHITE), (600, 550))
            DISPLAYSURF.blit(screen_font.render('Accuracy: ' + str(100*(Falcon.accuracy)) + "%", True, WHITE), (10, 10))
            
    def gamelose(self):
        self.gameover = True

    def gamewin(self):
        self.gameover = True
        self.win = True

    def createstar(self):
        self.stars.append([810, random.randrange(600)])

    def update(self):
        for star in self.stars:
            star[0] -= 5
        
class Bullet(pygame.sprite.Sprite):

    def __init__(self, coord = (0,0), direct = 0, allied = True):
        pygame.sprite.Sprite.__init__(self)
        if allied:
            self.image = pygame.image.load('Falc_Bullet.png')
        else:
            self.image = pygame.image.load('Enemy_Bullet.png')
        self.image.set_colorkey(WHITE)
        self.veloc = 10
        self.direc = direct
        self.xcoord = coord[0]
        self.ycoord = coord[1]
        self.rect = self.image.get_rect(center = (self.xcoord, self.ycoord))
        self.image = pygame.transform.rotate(self.image, self.direc+90)

    def move(self):
        self.xcoord -= self.veloc*math.sin(math.radians(self.direc))
        self.ycoord -= self.veloc*math.cos(math.radians(self.direc))

    def update(self):
        self.move()
        if self.xcoord <= -5:
            self.kill()
        if self.xcoord >= 805:
            self.kill()
        if self.ycoord >= 605:
            self.kill()
        if self.ycoord <= 200 and level == 1:
            self.kill()
        elif self.ycoord <= 000 and level == 2:
            self.kill()
        self.rect = self.image.get_rect(center = (self.xcoord, self.ycoord))

class Falcon_1(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Falcon.png')
        self.Const_img = pygame.image.load('Falcon.png')
        self.image.set_colorkey(WHITE)
        self.direc = 0
        self.veloc = 0
        self.xcoord = 300
        self.ycoord = 475
        self.rect = self.image.get_rect(center = (self.xcoord, self.ycoord))
        self.Const_rect = self.image.get_rect(center = (self.xcoord, self.ycoord))

    def move(self):
        self.xcoord -= self.veloc*math.sin(math.radians(self.direc))
        self.ycoord -= self.veloc*math.cos(math.radians(self.direc))

    def rotate(self, img, rect, direc):
        self.image = pygame.transform.rotate(img, direc)
        self.rect = self.image.get_rect(center = rect.center)
        self.image.set_colorkey(WHITE)
    
    def update(self, background):
        self.rotate(self.Const_img, self.rect, self.direc)
        if self.veloc >= 6:
            self.veloc = 6
        if self.veloc <= 0:
            self.veloc = 0
        self.move()
        if self.ycoord > 575:
            self.ycoord = 575
        if self.xcoord < -15:
            self.xcoord = 815
        elif self.xcoord > 815:
            self.xcoord = -15
        if self.direc < 0:
            self.direc = 360 + self.direc
        if self.direc >= 360:
            self.direc = self.direc - 360
        if self.ycoord < 225:
            if background.field_up:
                self.ycoord = 225
            elif not background.field_up:
                if (background.hole_up and background.hole_coords[0] < self.xcoord) and (background.hole_coords[0] + background.hole_coords[2] > self.xcoord):
                    background.gamewin()
                else:
                    background.gamelose()
        self.rect = self.image.get_rect(center = (self.xcoord, self.ycoord))
        self.Const_rect = self.rect.copy()
        self.rect.inflate_ip(-6*(5*math.fabs(math.cos(math.radians(self.direc)))+5*math.fabs(math.sin(math.radians(self.direc)))-4),-6*(5*math.fabs(math.cos(math.radians(self.direc)))+5*math.fabs(math.sin(math.radians(self.direc)))-4))

class Falcon_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Falcon2.png')
        self.image.set_colorkey(WHITE)
        self.xcoord = 100
        self.ycoord = 300
        self.direc = 0
        self.veloc = 0
        self.fired = 0
        self.hits = 0
        self.accuracy = 0
        self.shield = 100
        self.rect = self.image.get_rect(center = (self.xcoord, self.ycoord))

    def update(self, background):
        if self.ycoord < 25:
            self.ycoord = 25
        elif self.ycoord > 575:
            self.ycoord = 575
        if self.xcoord < 25:
            self.xcoord = 25
        elif self.xcoord > 775:
            self.xcoord = 775
        if self.fired == 0:
            self.accuracy = 0
        else:
            self.accuracy = round(self.hits*1.0/self.fired,4)
        if self.shield < 0:
            self.shield = 0
            background.gamelose()
        self.shield += 1
        if self.shield > 100:
            self.shield = 100
        self.rect = self.image.get_rect(center = (self.xcoord, self.ycoord))

class TiFighter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Unknown.png')
        self.image.set_colorkey(WHITE)
        self.veloc = 2 + random.randrange(5)
        self.rand = random.randrange(2)
        self.direc = 270 - 180*self.rand
        self.xcoord = -50 + self.rand*900
        self.ycoord = random.randrange(300) + 250
        self.rect = self.image.get_rect(center = (self.xcoord, self.ycoord))
        self.image = pygame.transform.rotate(self.image, self.direc)

    def move(self):
        self.xcoord -= self.veloc*math.sin(math.radians(self.direc))
        self.ycoord -= self.veloc*math.cos(math.radians(self.direc))
        self.rect.center = (self.xcoord, self.ycoord)

    def update(self):
        self.move()
        if self.xcoord <= -55:
            self.kill()
        if self.xcoord >= 855:
            self.kill()

class Boss_body(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Boss_body.png')
        self.image.set_colorkey(WHITE)
        self.veloc = 1.5
        self.direc = 0
        self.xcoord = 700
        self.ycoord = 300
        self.health = 6
        self.active = False
        self.rect = self.image.get_rect(center = (self.xcoord, self.ycoord))

    def move(self):
        self.xcoord -= self.veloc*math.sin(math.radians(self.direc))
        self.ycoord -= self.veloc*math.cos(math.radians(self.direc))
        self.rect.center = (self.xcoord, self.ycoord)

    def update(self):
        self.move()
        if self.ycoord <= 200:
            self.direc = 180
        if self.ycoord >= 400:
            self.direc = 0
        if self.health == 0:
            self.kill()

class Boss_topfin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Boss_fintop.png')
        self.image.set_colorkey(WHITE)
        self.veloc = 1.5
        self.direc = 0
        self.xcoord = 700
        self.ycoord = 255
        self.health = 6
        self.active = False
        self.rect = self.image.get_rect(center = (self.xcoord, self.ycoord))

    def move(self):
        self.xcoord -= self.veloc*math.sin(math.radians(self.direc))
        self.ycoord -= self.veloc*math.cos(math.radians(self.direc))
        self.rect.center = (self.xcoord, self.ycoord)

    def update(self):
        self.move()
        if self.ycoord <= 155:
            self.direc = 180
        if self.ycoord >= 355:
            self.direc = 0
        if self.health == 0:
            self.kill()

class Boss_botfin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Boss_finbot.png')
        self.image.set_colorkey(WHITE)
        self.veloc = 1.5
        self.direc = 0
        self.xcoord = 700
        self.ycoord = 345
        self.health = 6
        self.active = False
        self.rect = self.image.get_rect(center = (self.xcoord, self.ycoord))

    def move(self):
        self.xcoord -= self.veloc*math.sin(math.radians(self.direc))
        self.ycoord -= self.veloc*math.cos(math.radians(self.direc))
        self.rect.center = (self.xcoord, self.ycoord)

    def update(self):
        self.move()
        if self.ycoord <= 245:
            self.direc = 180
        if self.ycoord >= 445:
            self.direc = 0
        if self.health == 0:
            self.kill()

def terminate():
    pygame.mixer.music.stop()
    pygame.quit()
    sys.exit()

def runGame():
    global score, level
    Falcon_obj = Falcon_1()
    Backgrd = Background_1()
    DISPLAYSURF.fill(BLACK)
    pygame.key.set_repeat(5)
    last_created = 0
    last_up = 0
    last_fired = 0
    last_spawn = 0
    last_enemy_fired = 1000
    bullet_list = pygame.sprite.Group()
    enemy_list = pygame.sprite.Group()
    enemy_bullet_list = pygame.sprite.Group()
    while level == 1:
        Backgrd.draw()
        if not Backgrd.gameover:
            if pygame.time.get_ticks() - last_fired > 200:
                bullet_list.add(Bullet(Falcon_obj.rect.center, Falcon_obj.direc, True))
                last_fired = pygame.time.get_ticks()
            if pygame.time.get_ticks() - last_created > 3000:
                Backgrd.hole_up = False
                if pygame.time.get_ticks() - last_created > 5000:
                    Backgrd.hole_up = True
                    Backgrd.hole_coords = (random.randrange(700) + 10, random.randrange(90) + 60,
                                         random.randrange(20) + 75, random.randrange(15) + 35)
                    last_created = pygame.time.get_ticks()
            if pygame.time.get_ticks() - last_up > 4000:
                Backgrd.field_up = True
                if pygame.time.get_ticks() - last_up > 7000:
                    Backgrd.field_up = False
                    last_up = pygame.time.get_ticks()
            if (pygame.time.get_ticks() - last_spawn > 1000) and len(enemy_list) < 2: #EASY MODE
                enemy_list.add(TiFighter())
                last_spawn = pygame.time.get_ticks()
            if pygame.time.get_ticks() - last_enemy_fired > 2000:
                for enemy in enemy_list:
                    enemy_bullet_list.add(Bullet(enemy.rect.center, enemy.direc, False))
                last_enemy_fired = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if (event.key == K_LEFT or event.key == K_a):
                        Falcon_obj.direc += 10
                    elif (event.key == K_RIGHT or event.key == K_d):
                        Falcon_obj.direc -= 10
                    elif (event.key == K_UP or event.key == K_w):
                        Falcon_obj.veloc += 1
                    elif (event.key == K_DOWN or event.key == K_s):
                        Falcon_obj.veloc -= 1
            bullet_list.update()
            bullet_list.draw(DISPLAYSURF)
            enemy_list.update()
            enemy_list.draw(DISPLAYSURF)
            enemy_bullet_list.update()
            enemy_bullet_list.draw(DISPLAYSURF)
            Falcon_obj.update(Backgrd)
            DISPLAYSURF.blit(Falcon_obj.image, Falcon_obj.Const_rect)
            #pygame.draw.rect(DISPLAYSURF, BLUE, Falcon_obj.rect, 1)
            for hit in pygame.sprite.groupcollide(bullet_list, enemy_list, True, True):
                sfx.play()
                score += 50
            if pygame.sprite.spritecollideany(Falcon_obj, enemy_bullet_list):
                Backgrd.gamelose()
            pygame.display.update()
            FPSCLOCK.tick(FPS)
            score -= 1
            if score == 0:
                Backgrd.gamelose()
        else:
            pygame.display.update()
            pygame.time.delay(500)
            if Backgrd.win:
                level = 2
            else:
                terminate()
    DISPLAYSURF.fill(BLACK)
    temp = screen_font.render('USE MOUSE!!!', True, WHITE)
    temp_rect = temp.get_rect(center = DISPLAYSURF.get_rect().center)
    DISPLAYSURF.blit(temp, temp_rect)
    pygame.display.update()
    pygame.time.delay(1500)
    Falcon_obj = Falcon_2()
    Backgrd = Background_2()
    bullet_list = pygame.sprite.Group()
    enemy_list = pygame.sprite.Group()
    enemy_bullet_list = pygame.sprite.Group()
    last_fired = pygame.time.get_ticks()
    last_enemy_fired = pygame.time.get_ticks()
    last_star = pygame.time.get_ticks()
    Body = Boss_body()
    Topfin = Boss_topfin()
    Botfin = Boss_botfin()
    enemy_list.add(Topfin)
    enemy_list.add(Botfin)
    enemy_list.add(Body)
    while level == 2:
        pygame.mouse.set_visible(False)
        Backgrd.draw(Falcon_obj)
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        if not Backgrd.gameover:
            if pygame.time.get_ticks() - last_enemy_fired > 500:
                for enemy in enemy_list:
                    enemy_bullet_list.add(Bullet(enemy.rect.center, 90, False))
                    last_enemy_fired = pygame.time.get_ticks()
            if pygame.mouse.get_pressed()[0] and pygame.time.get_ticks() - last_fired >= 250:
                bullet_list.add(Bullet(Falcon_obj.rect.center, 270, True))
                last_fired = pygame.time.get_ticks()
                Falcon_obj.fired += 1
            if pygame.time.get_ticks() - last_star > 100:
                Backgrd.createstar()
                last_star = pygame.time.get_ticks()
            Falcon_obj.xcoord = pygame.mouse.get_pos()[0]
            Falcon_obj.ycoord = pygame.mouse.get_pos()[1]
            for hit in pygame.sprite.groupcollide(enemy_list, bullet_list, False, True):
                if hit.active:
                    hit.health -= 1
                    Falcon_obj.hits += 1
            Backgrd.update()
            bullet_list.update()
            bullet_list.draw(DISPLAYSURF)
            Falcon_obj.update(Backgrd)
            enemy_bullet_list.update()
            enemy_bullet_list.draw(DISPLAYSURF)
            DISPLAYSURF.blit(Falcon_obj.image, Falcon_obj.rect)
            pygame.draw.ellipse(DISPLAYSURF, (200-2*Falcon_obj.shield, 0, 2*Falcon_obj.shield), Falcon_obj.rect.inflate(15, 15), 2)
            enemy_list.update()
            enemy_list.draw(DISPLAYSURF)
            score -= 1
            if score == 0:
                Backgrd.gamelose()
            temp = pygame.sprite.spritecollideany(Falcon_obj, enemy_bullet_list)
            if temp:
                Falcon_obj.shield -= 100
                temp.kill()
            if pygame.sprite.spritecollideany(Falcon_obj, enemy_list):
                Backgrd.gamelose()
            if len(enemy_list) == 3:
                Topfin.active = True
                pygame.draw.rect(DISPLAYSURF, BLUE, Topfin.rect, 1)
            elif len(enemy_list) == 2:
                Botfin.active = True
                pygame.draw.rect(DISPLAYSURF, BLUE, Botfin.rect, 1)
            elif len(enemy_list) == 1:
                Body.active = True
                pygame.draw.rect(DISPLAYSURF, BLUE, Body.rect, 1)
            elif len(enemy_list) == 0:
                Backgrd.gamewin()
                score = int(score*Falcon_obj.accuracy)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()

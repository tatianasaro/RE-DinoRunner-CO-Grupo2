import pygame
import os
import random
pygame.init()

# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND = pygame.image.load(os.path.join("chrome-dinosaur\Assets\Other/background.jpg"))

HEART = pygame.image.load(os.path.join("chrome-dinosaur\Assets\Other\Heart.png"))

RUNNING = [pygame.image.load(os.path.join("chrome-dinosaur\Assets\Dino\DinoRun1.png")),
           pygame.image.load(os.path.join("chrome-dinosaur\Assets\Dino\DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("chrome-dinosaur\Assets\Dino\DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join("chrome-dinosaur\Assets\Dino\DinoDuck1.png")),
           pygame.image.load(os.path.join("chrome-dinosaur\Assets\Dino\DinoDuck2.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("chrome-dinosaur\Assets\Cactus\SmallCactus1.png")),
                pygame.image.load(os.path.join("chrome-dinosaur\Assets\Cactus\LargeCactus2.png")),
                pygame.image.load(os.path.join("chrome-dinosaur\Assets\Cactus\LargeCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("chrome-dinosaur\Assets\Cactus\LargeCactus1.png")),
                pygame.image.load(os.path.join("chrome-dinosaur\Assets\Cactus\LargeCactus2.png")),
                pygame.image.load(os.path.join("chrome-dinosaur\Assets\Cactus\LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("chrome-dinosaur\Assets\Bird\Bird1.png")),
        pygame.image.load(os.path.join("chrome-dinosaur\Assets\Bird\Bird2.png"))]


BG = pygame.image.load(os.path.join("chrome-dinosaur\Assets\Other\Track.png"))


pygame.mixer.music.load("chrome-dinosaur\Assets\Other/fondo.mp3")
pygame.mixer.music.play()
HEART_COUNT = 5 


class Dinosaur:
    HX_POS = 20
    HY_POS = 10
    X_POS = 80
    Y_POS = 302
    Y_POS_DUCK = 335
    JUMP_VEL = 8.5

    def __init__(self):
        self.sonido_salto = pygame.mixer.Sound("chrome-dinosaur\Assets\Other\salto.wav")
        self.sonido_choque = pygame.mixer.Sound("chrome-dinosaur\Assets\Other/277.mp3")
      
        self.heart_count = HEART_COUNT
        self.heart_img = HEART
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.heart_rect = self.heart_img.get_rect()
        self.heart_rect.x = self.HX_POS
        self.heart_rect.y = self.HY_POS

    def update(self, userInput):
        
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.sonido_salto.play()
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False
    
        

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(BACKGROUND, [0,0])
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        if HEART_COUNT == 5:
            SCREEN.blit(self.heart_img, (140, 10))
            SCREEN.blit(self.heart_img, (110, 10))
            SCREEN.blit(self.heart_img, (80, 10))
            SCREEN.blit(self.heart_img, (50, 10))
            SCREEN.blit(self.heart_img, (20, 10))
        if HEART_COUNT == 4:
            SCREEN.blit(self.heart_img, (110, 10))
            SCREEN.blit(self.heart_img, (80, 10))
            SCREEN.blit(self.heart_img, (50, 10))
            SCREEN.blit(self.heart_img, (20, 10))
        if HEART_COUNT == 3:
            SCREEN.blit(self.heart_img, (80, 10))
            SCREEN.blit(self.heart_img, (50, 10))
            SCREEN.blit(self.heart_img, (20, 10))
        if HEART_COUNT == 2:
            SCREEN.blit(self.heart_img, (50, 10))
            SCREEN.blit(self.heart_img, (20, 10))
            
        if HEART_COUNT == 1:
            SCREEN.blit(self.heart_img, (20, 10))
       

     
            


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 302
        
        


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1
        
class Shield:
    def __init__(self):
        self.image = SHIELD
        self.type = SHIELD_TYPE
        super().__init__(self.image, self.type)

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.points = 0

    def update(self, points, game_speed, player):
        self.generate_power_ups(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if (player.dino_rect.colliderect(power_up.rect)):
               power_up.start_time = pygame.time.get_ticks() # inicio con el escudo
               player.shield = True
               player.type = power_up.type
               power_up.start_time = pygame.time.get_ticks() # termina el uso del escudo
               time_random = random.randrange(5,8)
               player.shield_time_up = power_up.start_time + (time_random * 1000)

               self.power_ups.remove(power_up)

    def generate_power_ups(self, points):
        self.points = points
        if len(self.power_ups) == 0:
            if self.when_appears == self.points:
                self.when_appears = random.randint(self.when_appears + 200, self.when_appears + 500)
                self.power_ups.append(Shield())
        # return self.power_ups

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self, points):
        self.power_ups = []
        self.points = points
        self.when_appears = random.randint(200,300) + self.points


def main():
    sonido_choque = pygame.mixer.Sound("chrome-dinosaur\Assets\Other/277.mp3")
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                sonido_choque.play()
                HEART_COUNT = 1
                pygame.time.delay(200)
                death_count += 1
                menu(death_count)
            
            

        background()

        score()

        clock.tick(30)
        pygame.display.update()


def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((255, 165, 0))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()


menu(death_count=0)

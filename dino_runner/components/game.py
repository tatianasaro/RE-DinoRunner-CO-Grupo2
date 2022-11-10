import pygame
from dino_runner.components import text_utils
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager
from dino_runner.utils.constants import  BACKGROUND, BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        pygame.mixer.music.load("dino_runner/assets\Other\out-run-125180.mp3")
        pygame.mixer.music.play()
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        
        
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.player_heart_manager = PlayerHeartManager()
        

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()
        

    def events(self):
        user_input = pygame.key.get_pressed()
        self.player.event(user_input)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False    
        self.screen.fill((255, 255, 255))
       
        
    def update(self):
        self.player.update()
        self.obstacle_manager.update(self)

    def draw(self):
        self.draw
        self.clock.tick(FPS)
        #self.screen.fill((255, 255, 255))
        self.draw_background()
        
        
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.player_heart_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        #self.screen.blit(BACKGROUND, [0,0])
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
    def draw_score(self):
        self.points +=1
        
        if self.points %100 == 0:
            self.game_speed += 2
        text, text_rect = text_utils.get_score_element(self.points)
        self.screen.blit(text,text_rect)
        
    
        
        
    

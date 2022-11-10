import random
import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import(LARGE_CACTUS, SMALL_CACTUS)


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        
    def update(self, game):   
        if len (self.obstacles) == 0:
            cactus_size = random.randint(0,1)
            if cactus_size == 0:
                largeCactus = Cactus(LARGE_CACTUS)
                largeCactus.rect.y -= 30
                self.obstacles.append(largeCactus)
            else:
                self.obstacles.append(Cactus(SMALL_CACTUS))
                
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
        
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.player_heart_manager.reduce_heart()
                pygame.time.delay(100)
                if game.player_heart_manager.heart_count > 0:
                    self.obstacles.pop()
                    game.player.has_lives = True
                    start_time = pygame.time.get_ticks()
                    game.player.time_up = start_time + 1000
                
                
                else:
                    pygame.time.delay(500)
                    game.playing = False
                    break
            
    def draw(self, screen):
        
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        
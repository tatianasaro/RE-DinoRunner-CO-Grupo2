
import pygame

FONT_STYLE = 'freesansbold.ttf'
def get_score_elements(points):
    font = pygame.font.Font(FONT_STYLE, 20)
    
    text = font.render('points: ' + str(points), True, (0,0,0))
    text_rect = text.get_rect()
    text_rect.center = (1000, 50)
    
    return (text, text_rect)
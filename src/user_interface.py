import pygame
from src.config import TARGET_SIZE, CURSOR_SIZE

class UserInterface:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.cursor = pygame.image.load('assets/images/cursor.png')
        self.target = pygame.image.load('assets/images/target.png')
        self.cursor = pygame.transform.scale(self.cursor, (CURSOR_SIZE, CURSOR_SIZE))
        self.target = pygame.transform.scale(self.target, (TARGET_SIZE, TARGET_SIZE))
        self.font = pygame.font.Font(None, 36)

    def display_ui(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.target, (400, 300))
        pygame.display.update()

    def handle_user_interaction(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if self.target.get_rect().collidepoint(x, y):
                    pygame.mixer.Sound('assets/sounds/success.wav').play()
                else:
                    pygame.mixer.Sound('assets/sounds/failure.wav').play()
        return True

    def update_cursor_position(self, x, y):
        self.screen.blit(self.cursor, (x, y))
        pygame.display.update()

    def display_results(self, hits, misses, accuracy):
        result_text = self.font.render(f"Hits: {hits} Misses: {misses} Accuracy: {accuracy}%", True, (0, 0, 0))
        self.screen.blit(result_text, (10, 10))
        pygame.display.update()
import pygame
from src.config import TARGET_SIZE, TEST_DURATION, CURSOR_SIZE
from src.results import Results

class MouseTest:
    def __init__(self):
        self.results = Results()
        self.start_time = None
        self.end_time = None

    def start_test(self):
        pygame.mouse.set_visible(False)
        self.start_time = pygame.time.get_ticks()

    def track_mouse(self):
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            self.results.add_click(pos)

    def end_test(self):
        self.end_time = pygame.time.get_ticks()
        self.results.calculate_results(self.start_time, self.end_time)

    def hit_target(self, target_pos):
        mouse_pos = pygame.mouse.get_pos()
        distance = ((mouse_pos[0] - target_pos[0]) ** 2 + (mouse_pos[1] - target_pos[1]) ** 2) ** 0.5
        if distance <= TARGET_SIZE / 2:
            pygame.mixer.Sound('assets/sounds/success.wav').play()
            self.results.add_hit()
        else:
            pygame.mixer.Sound('assets/sounds/failure.wav').play()
            self.results.add_miss()

    def check_end_condition(self):
        if pygame.time.get_ticks() - self.start_time >= TEST_DURATION:
            self.end_test()
            return True
        return False
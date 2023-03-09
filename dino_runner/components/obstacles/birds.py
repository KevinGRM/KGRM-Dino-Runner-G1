
import random
from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self):
        image = BIRD[0]
        super().__init__(image)
        positions = [170, 320, 220] ##100 250 150
        self.rect.y = random.choice(positions)
        self.step = 0

    def update(self, game_speed, obstacles):
        super().update(game_speed, obstacles)
        self.image = BIRD[self.step // 10]
        self.step += 1
        if self.step >= 20:
            self.step = 0
            
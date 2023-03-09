
import random

from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS


class Cactus(Obstacle):
    def __init__(self):
        cactus = [SMALL_CACTUS, LARGE_CACTUS]
        cactus_var = random.randint(0, 4)
        cactus_type = random.choice(cactus)
        image = cactus_type[cactus_var]
        super().__init__(image)
        if cactus_type == SMALL_CACTUS:
            self.rect.y = 405   ##325
        else:
            self.rect.y = 385   ##300
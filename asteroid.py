import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
       super().__init__(x, y, radius)

    def draw(self, screen):
         pygame.draw.circle(screen, "white", self.position, self.radius, 0 )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        split_angle = random.uniform(20, 50)
        split_radius = self.radius -  ASTEROID_MIN_RADIUS
        roid_one_vector = self.velocity.rotate(split_angle)
        roid_two_vector = self.velocity.rotate(-split_angle)


        new_roid_one = Asteroid(*self.position, split_radius)
        new_roid_two = Asteroid(*self.position, split_radius)

        new_roid_one.velocity = roid_one_vector * 1.2
        new_roid_two.velocity = roid_two_vector * 1.2

    
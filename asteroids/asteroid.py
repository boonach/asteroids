from constants import *
import pygame
from circleshape import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt):
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        a1_velocity = self.velocity.rotate(angle)
        a2_velocity = self.velocity.rotate(0-angle)
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, split_radius)
        a2 = Asteroid(self.position.x, self.position.y, split_radius)
        a1.velocity = a1_velocity *1.2
        a2.velocity = a2_velocity *1.2
        
    
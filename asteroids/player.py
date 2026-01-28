from constants import *
from circleshape import *

class Player(CircleShape):
    def __init__(self, x, y):
        self.rotation = 0
        self.velocity = pygame.Vector2(0, 0)
        super().__init__(x, y, PLAYER_RADIUS)
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw (self, screen):
        surface = screen
        color = "white"
        points = self.triangle()
        width = LINE_WIDTH
        pygame.draw.polygon(surface, color, points, width)
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def update(self, dt):
        USE_DRIFT = False  # flip to True only for experiments
        if USE_DRIFT:
            self.update_acceleration(dt)
            return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
    def update_acceleration(self, dt):
        keys = pygame.key.get_pressed()
        # acceleration in the facing direction
        unit_vector = pygame.Vector2(0, 1).rotate(self.rotation)
    
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.velocity += unit_vector * ACCEL * dt
        if keys[pygame.K_s]:
            self.velocity -= unit_vector * ACCEL * dt

        self.velocity *= FRICTION
        # clamp max speed
        if self.velocity.length() > PLAYER_MAX_SPEED:
            self.velocity = self.velocity.normalize() * PLAYER_MAX_SPEED
        self.position += self.velocity * dt
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
            
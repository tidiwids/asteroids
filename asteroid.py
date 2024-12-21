from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        return pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        ricochetAngle = random.uniform(20, 50)
        newVector1 = self.velocity.rotate(ricochetAngle)
        newVector2 = self.velocity.rotate(-ricochetAngle)
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        newAsteroid1 = Asteroid(self.position.x, self.position.y, newRadius)
        newAsteroid2 = Asteroid(self.position.x, self.position.y, newRadius)

        newAsteroid1.velocity = newVector1 * 1.2
        newAsteroid2.velocity = newVector2 * 1.2
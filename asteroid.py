import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.radius = radius
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    
    def update(self,dt):
        self.position += self.velocity *dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")        
        a1 = Asteroid(self.position.x,self.position.y,self.radius-ASTEROID_MIN_RADIUS)
        a2 = Asteroid(self.position.x,self.position.y,self.radius-ASTEROID_MIN_RADIUS)

        ra = random.uniform(20,50)
        a1.velocity = self.velocity.rotate(ra)
        a1.velocity *= 1.2

        ra = random.uniform(-20,-50)
        a2.velocity = self.velocity.rotate(ra)
        a2.velocity *= 1.2
        


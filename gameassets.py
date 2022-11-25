import pygame


#button class
class Button():

    def __init__(self, surface, x, y, image, image_trans, size_x, size_y):
        self.image = pygame.transform.scale(image, (size_x, size_y))
        self.image_trans = pygame.transform.scale(image_trans, (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.above = False
        self.clicked = False
        self.surface = surface

    def draw(self):
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
          self.surface.blit(self.image_trans, (self.rect.x, self.rect.y))
          if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
              action = True
              self.clicked = True
        else:
          #draw button
          self.surface.blit(self.image, (self.rect.x, self.rect.y))
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        return action
class Animation():

    def __init__(
        self,
        image,
        size_x,
        size_y,
        velocity,
        surface,
    ):
        self.image = pygame.transform.scale(image, (size_x, size_y))
        self.velocity = velocity
        self.surface = surface
        self.size_x = size_x
        self.size_y = size_y
        self.rel_width = size_x % image.get_rect().width

    def Paralax(self):
        rel_width = self.size_x % self.image.get_rect().width
        self.surface.blit(self.image,
                          (rel_width - self.image.get_rect().width, 0))
        if rel_width < self.size_x:
            self.surface.blit(self.image, (rel_width, 0))
        self.size_x -= self.velocity

        return print("Funciona" + str(self.velocity))


class Bar():

    def __init__(self, surface, x, y, stts, max_stts, color):
        self.surface = surface
        self.x = x
        self.y = y
        self.stts = stts
        self.max_stts = max_stts
        self.color = color

    def Draw(self, stts):
        self.stts = stts
        raio = self.stts / self.max_stts
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, 150, 20))
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, 150 * raio, 20))



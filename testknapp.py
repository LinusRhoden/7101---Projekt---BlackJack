import pygame
import sys


pygame.init()

clock=pygame.time.Clock()


window_size = (400, 400)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Button Function')

name = "stand"

# Create a font object
font = pygame.font.Font(None, 24)

# Create a surface for the button
button_surface = pygame.Surface((150, 50))

# Render text on the button
text = font.render(str(name), True, (0, 0, 0))
text_rect = text.get_rect(center=(button_surface.get_width()/2, button_surface.get_height()/2))


# Create a pygame.Rect object 
button_rect = pygame.Rect(125, 125, 150, 50)  

while True:
 clock.tick(60)
 

 screen.fill((155, 255, 155))

 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   sys.exit()

  # Check for the mouse button down event
  if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
   # Call the on_mouse_button_down() function
   if button_rect.collidepoint(event.pos):
    print("Button clicked!")

 # Check if the mouse is over the button
 if button_rect.collidepoint(pygame.mouse.get_pos()):
  pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
 else:
  pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
  pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
  pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
  pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)
  
  
 
 button_surface.blit(text, text_rect)
 screen.blit(button_surface, (button_rect.x, button_rect.y))

 pygame.display.update()
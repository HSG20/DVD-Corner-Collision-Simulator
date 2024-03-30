import pygame, random

#Inicializar juego
pygame.init()

#Tamaño pantalla
size = 1920, 1080
screen = pygame.display.set_mode(size)

#Título pantalla
pygame.display.set_caption("DVD LOGO CORNER COLLISION SIMULATOR")

#Inicializar variables
width, height = size
speed = [100, 100]
white = 255, 255, 255
score = 0
corner_touched = False
arial = pygame.font.SysFont("arial", int((width+height)/50))

#Crear objeto imagen, y obtener rectángulo
ball = pygame.image.load("dvd.png")
ballrect = ball.get_rect()

# Create a clock object
clock = pygame.time.Clock()

#Bucle del juego
running = True
while running:
    
    # Set the frame rate to 60 FPS
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #Movimiento pelota
    ballrect = ballrect.move(speed)
    
    #Colisiones pelota-ventana
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        
    # Comprobar si la pelota toca una esquina
    if ballrect.left == 0 and ballrect.top == 0:
        corner_touched = True
    elif ballrect.left == 0 and ballrect.bottom == height:
        corner_touched = True
    elif ballrect.right == width and ballrect.top == 0:
        corner_touched = True
    elif ballrect.right == width and ballrect.bottom == height:
        corner_touched = True
    else:
        corner_touched = False
    
    # Actualizar contador de colisiones
    if corner_touched:
        score += 1/2
        corner_touched = False
    #Texto
    text = arial.render("COLISIONES: " + str(int(score)), True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (width/2, height/13)
    
    #Pintar fondo, actualizar pelota y pantalla
    screen.fill(white)
    screen.blit(text, text_rect)
    screen.blit(ball,ballrect)
    pygame.display.flip()
    
#Cerrar juego
pygame.quit()
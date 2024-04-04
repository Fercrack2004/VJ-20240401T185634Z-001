import pygame
import botones

pygame.init()

pausado = False
cual_menu = "main"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

start_img = pygame.image.load("VJ/assets/start_paint.png").convert_alpha()
lore_img = pygame.image.load("VJ/assets/Lore.png").convert_alpha()
sobrevive_img = pygame.image.load("VJ/assets/sobrevive2.png")
imagen_atras = pygame.image.load("VJ/assets/atras.png").convert_alpha()

sobrevive_rect = sobrevive_img.get_rect(topleft=(0,0))

start_boton = botones.Boton(304,125,start_img,1)
lore_boton = botones.Boton(336,375,lore_img,1)
atras_boton = botones.Boton(336,400,imagen_atras,1)


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Menu")

TEXT_COL = (255,255,255)
font = pygame.font.SysFont("arialblack",40)

def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

run = True
while run:

    screen.fill((52,78,91))

    if pausado == True:
        if cual_menu == "main":

            if start_boton.draw(screen):
                pausado = False
            if lore_boton.draw(screen):
                cual_menu = "lore"

        if cual_menu == "lore":
            screen.blit(sobrevive_img,(sobrevive_rect))
            if atras_boton.draw(screen):
                cual_menu = "main"
            
    else:
        draw_text("Pene",font,TEXT_COL,160,250)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pausado = True
    
        if event.type == pygame.QUIT:
            run = False
    


    pygame.display.update()

pygame.quit()

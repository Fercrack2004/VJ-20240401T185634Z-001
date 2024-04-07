import pygame
import botones

pygame.init()

pausado = False
cual_menu = "main"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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

# Importa el módulo de música de pygame
import pygame.mixer

# Inicializa el módulo de música de pygame
pygame.mixer.init()

# Carga el archivo de música
menu_music = pygame.mixer.Sound("VJ/assets/musicgoofyass/quando.mp3")

# Define una función para reproducir la música del menú
def play_menu_music():
    menu_music.play(-1)  # El argumento -1 indica que la música se reproducirá en bucle infinito

# Define una función para detener la música del menú
def stop_menu_music():
    menu_music.stop()

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

run = True
while run:
    screen.fill((52,78,91))
    if not pausado:
        if music_played:
            music_played = False
            play_menu_music()
            
        if cual_menu == "main":
            if start_boton.draw(screen):
                pausado = False
            if lore_boton.draw(screen):
                cual_menu = "lore"
                
        elif cual_menu == "lore":
            screen.blit(sobrevive_img, sobrevive_rect)
            if atras_boton.draw(screen):
                cual_menu = "main"
    else:
        draw_text("Pene", font, TEXT_COL, 160, 250)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pausado = True
        elif event.type == pygame.QUIT:
            run = False
            stop_menu_music()  # Detener la música del menú al cerrar la ventana

    pygame.display.update()

pygame.quit()
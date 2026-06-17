from pygame import *
init()

# CONSTANTES parametrs de inicio
ANCHO, ALTO = 640, 480
TITULO = 'Proyecto Laberinto'
FPS = 60
BACK_COLOR = (27, 80, 155)
WALL_COLOR = (202, 11, 219)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PLAYER_IMG = 'hero.png'
ENEMY_IMG = 'cyborg.png'
GOAL_IMG = 'trophy-1.png'

# CLASE PRINCIPAL
class GameSprite(sprite.Sprite):
    def __init__(self, img_file, cor_x, cor_y, speed=0):
        super().__init__()
        self.image = transform.scale(image.load(img_file), (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = cor_x
        self.rect.y = cor_y
        self.speed = speed

    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= ALTO - self.rect.height:
            self.rect.y += self.speed
        if keys[K_d] and self.rect.x <= ANCHO - self.rect.width:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x >= 0:
            self.rect.x -= self.speed

class Enemy(GameSprite):
    def __init__(self, img_file, cor_x, cor_y, speed):
        super().__init__(img_file, cor_x, cor_y, speed)
        self.move_right = True # Estado inicial (flag)
        self.original_img = self.image

    def update(self):
        if self.move_right:
            self.rect.x += self.speed
            if self.rect.x >= ANCHO - 60:
                self.move_right = False
        else:
            self.rect.x -= self.speed
            if self.rect.x <= 0:
                self.move_right = True


class Wall(sprite.Sprite):
    def __init__(self, color, x, y, w, h):
        super().__init__()
        self.color = color
        self.width = w
        self.height = h
        self.image = Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw_wall(self):
        draw.rect(screen, self.color, self.rect)

# PANTALLA (superficie principal)
screen = display.set_mode((ANCHO, ALTO))
display.set_caption(TITULO)
clock = time.Clock()

# OBJETOS
player = Player(PLAYER_IMG, 20, 350, 5)
enemy = Enemy(ENEMY_IMG, 20, 20, 5)
goal = GameSprite(GOAL_IMG, ANCHO - 60, ALTO - 60)
# CREANDO PAREDES
wall_1 = Wall(WALL_COLOR, 200, 200, 200, 10)

# GAME LOOP
run = True # variable de estado
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    screen.fill(BACK_COLOR)
    player.reset() # Metodo para renderizar la imagen
    player.update() # METODO DE MOVIMIENTO

    enemy.reset()
    enemy.update()

    goal.reset()
    goal.update()

    wall_1.draw_wall()

    display.update()
    clock.tick(FPS) # Establecer fotogramas por segundos
quit()

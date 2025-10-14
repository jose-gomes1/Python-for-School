import pygame as game
import sys

# === Inicialização ===
game.init()

# === Constantes ===
width, height = 1920, 1080
ACC = 0.5       # aceleração normal
ACC2 = 1.0      # aceleração com boost
FRIC = -0.12
FPS = 60

FramePerSec = game.time.Clock()

# === Janela ===
janela = game.display.set_mode((width, height))
game.display.set_caption("Exemplo de Pygame - Shift Boost Limitado")

# === Cores ===
cor_fundo = (0, 150, 10)
cor_personagem = (255, 255, 255)
cor_boost = (255, 200, 0)
cor_barra_fundo = (50, 50, 50)
cor_barra_progresso = (0, 255, 0)

# === Classe do jogador ===
class Jogador(game.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = game.Surface((50, 50))
        self.surf.fill(cor_personagem)
        self.rect = self.surf.get_rect(center=(width//2, height//2))
        self.vel = game.math.Vector2(0, 0)
        self.pos = game.math.Vector2(width//2, height//2)
        self.acc = game.math.Vector2(0, 0)

        self.shift_start_time = None    
        self.shift_duration = 5000  # tempo máximo de boost (ms)
        self.boost_ativo = False

    def move(self):
        self.acc = game.math.Vector2(0, 0)
        teclas = game.key.get_pressed()
        now = game.time.get_ticks()

        # === Controle de Shift ===
        if teclas[game.K_LSHIFT]:
            # Se acabou de apertar o Shift
            if self.shift_start_time is None:
                self.shift_start_time = now
                self.boost_ativo = True

            # Verifica se o tempo de boost já passou
            elif now - self.shift_start_time >= self.shift_duration:
                self.boost_ativo = False  # tempo acabou

        else:
            # Soltou o Shift → reset
            self.shift_start_time = None
            self.boost_ativo = False

        # === Movimento ===
        acc_value = ACC2 if self.boost_ativo else ACC

        if teclas[game.K_LEFT]:
            self.acc.x = -acc_value
        elif teclas[game.K_RIGHT]:
            self.acc.x = acc_value

        if teclas[game.K_UP]:
            self.acc.y = -acc_value
        elif teclas[game.K_DOWN]:
            self.acc.y = acc_value

        # === Física ===
        self.acc += self.vel * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # === Limites da tela ===
        if self.pos.x < 0: self.pos.x = 0
        if self.pos.x > width - self.rect.width: self.pos.x = width - self.rect.width
        if self.pos.y < 0: self.pos.y = 0
        if self.pos.y > height - self.rect.height: self.pos.y = height - self.rect.height

        self.rect.center = self.pos

        # === Muda cor quando boost ativo ===
        if self.boost_ativo:
            self.surf.fill(cor_boost)
        else:
            self.surf.fill(cor_personagem)

    def draw_boost_bar(self, surface):
        """Desenha barra de tempo restante do boost"""
        bar_width = 300
        bar_height = 20
        x, y = 50, 50

        # Fundo da barra
        game.draw.rect(surface, cor_barra_fundo, (x, y, bar_width, bar_height))

        if self.shift_start_time:
            now = game.time.get_ticks()
            tempo_usado = now - self.shift_start_time
            progresso = 1 - min(tempo_usado / self.shift_duration, 1)
            game.draw.rect(surface, cor_barra_progresso, (x, y, bar_width * progresso, bar_height))

        # Borda
        game.draw.rect(surface, (255, 255, 255), (x, y, bar_width, bar_height), 2)


# === Instancia o jogador ===
player = Jogador()

# === Loop principal ===
while True:
    for evento in game.event.get():
        if evento.type == game.QUIT:
            game.quit()
            sys.exit()

    # Atualiza o jogador
    player.move()

    # === Desenho ===
    janela.fill(cor_fundo)
    janela.blit(player.surf, player.rect)
    player.draw_boost_bar(janela)

    game.display.flip()
    FramePerSec.tick(FPS)

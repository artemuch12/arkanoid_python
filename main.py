import pygame
import random
import time
from setting import *
from stones import *
from boll import *
from player import *
from os import path

sndDir = path.join(path.dirname(__file__), 'snd')

def renderLine(screen):
    """Функция для отрисовки рамок """
    pygame.draw.line(screen,
    BLACK, [4, 10], [WIDTH-200, 10], 4)
    pygame.draw.line(screen, BLACK,
    [4, 10], [4, HEIGHT-25], 4)
    pygame.draw.line(screen, BLACK,
    [4, HEIGHT-25], [WIDTH-200, HEIGHT-25], 4)
    pygame.draw.line(screen, BLACK,
    [WIDTH-200, 10], [WIDTH-200, HEIGHT-25], 4)
    pygame.draw.line(screen, RED,
    [7, HEIGHT-85], [WIDTH-202, HEIGHT-85], 1)

def levelUp(player, boll, level):
    if level%3 == 2:
        player.speed += 1
        boll.speedx += 1
    if level%2 == 1:
        boll.speedy += 1


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Arkanoid")
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    sprites_player = pygame.sprite.Group()
    sprites_stones = pygame.sprite.Group()
    player = Player()
    boll = Boll()
    score = 0
    level = 0
    gameOver = False

    flagOne = True
    flagBridges = True
    all_sprites.add(player)
    all_sprites.add(boll)
    sprites_player.add(player)
    # Текстовые поля
    fontScore = pygame.font.Font(None, 24)
    fontEnd = pygame.font.Font(None, 48)
    textScoreOne = fontScore.render('Очки:', 1, (0, 0, 0))
    textLevelOne = fontScore.render('Уровень:', 1, (0, 0, 0))

    screen.fill(WHITE)
    textStart = fontEnd.render("Я хочу сыграть с тобой в игру!", 1, BLACK)
    screen.blit(textStart, (50, 200))
    pygame.display.flip()
    time.sleep(2)
    running = True
    while running:
        clock.tick(FPS)
        if flagBridges:
            flagBridges = False
            coor_x = BRIDGES_POZX
            coor_y = BRIDGES_POZY
            for brick in range(random.randint(BRIDGES_MIN, BRIDGES_MAX)):
                stone = Stones(coor_x, coor_y)
                all_sprites.add(stone)
                sprites_stones.add(stone)
                if coor_x + 53 < HEIGHT-270:
                    coor_x += 53
                elif coor_x + 53 > HEIGHT-270 and flagOne == True:
                    coor_x = 70
                    coor_y += 25
                    flagOne = False
                elif coor_x + 53 > HEIGHT-270 and flagOne == False:
                    coor_x = 40
                    coor_y += 25
                    flagOne = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        # Обновление
        all_sprites.update()

        # Проверка на соударение шарика и дорожки
        hits = pygame.sprite.spritecollide(boll, sprites_player, False)
        if hits:
            boll.speedy = -boll.speedy
            #playerSound.play()
        # Проверка на пролет шарика красной линии
        if boll.rect.y > WIDTH-85:
            running = False
        # Проверка на соприкосновение с кирпичем
        hits = pygame.sprite.spritecollide(boll, sprites_stones, True)
        if hits:
            boll.speedy = -boll.speedy
            score += 20
        # Проверка
        if not sprites_stones.sprites():
            level += 1
            # Возвращаем шарик на начальную координату
            boll.rect.x = BOLL_POZX
            boll.rect.y = BOLL_POZY
            boll.speedx = 0
            boll.speedy = 0
            boll.flag = False
            # Возвращаем на начальную позицию платформу
            player.rect.center = (PLAT_POZX, PLAT_POZY)
            flagBridges = True
            levelUp(player, boll, level)


        # Рендеринг
        screen.fill(WHITE)
        all_sprites.draw(screen)
        screen.blit(textScoreOne, (450, 50))
        textScoreTwo = fontScore.render(str(score), 1, (0, 0, 0))
        screen.blit(textScoreTwo, (450, 80))
        screen.blit(textLevelOne, (450, 120))
        textLevelTwo = fontScore.render(str(level), 1, (0, 0, 0))
        screen.blit(textLevelTwo, (450, 150))

        renderLine(screen)

        pygame.display.flip()
    time.sleep(1)
    screen.fill(WHITE)
    textEndOne = fontEnd.render('Ваш счёт: '+str(score), 1, BLACK)
    textEndTwo = fontEnd.render("Ваш уровень: "+str(level), 1, BLACK)
    fontEnd = pygame.font.Font(None, 60)
    textEndThree = fontEnd.render("Игра окончена!", 1, RED)
    screen.blit(textEndOne, (120, 80))
    screen.blit(textEndTwo, (120, 130))
    screen.blit(textEndThree, (120, 250))
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()

if __name__ == "__main__":
    main()

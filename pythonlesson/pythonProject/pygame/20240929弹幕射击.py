import pygame
import random

# 初始化 pygame
pygame.init()

# 设置窗口
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("弹幕射击游戏")

# 颜色定义
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 玩家类
class Player:
    def __init__(self):
        self.image = pygame.Surface((50, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))
        self.speed = 5

    def move(self, dx):
        self.rect.x += dx
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WIDTH - self.rect.width:
            self.rect.x = WIDTH - self.rect.width

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# 子弹类
class Bullet:
    def __init__(self, x, y):
        self.image = pygame.Surface((5, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 7

    def move(self):
        self.rect.y -= self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# 敌人类
class Enemy:
    def __init__(self):
        self.image = pygame.Surface((50, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(x=random.randint(0, WIDTH - 50), y=0)
        self.speed = 3

    def move(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# 游戏主循环
def main():
    clock = pygame.time.Clock()
    player = Player()
    bullets = []
    enemies = []
    running = True

    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-player.speed)
        if keys[pygame.K_RIGHT]:
            player.move(player.speed)
        if keys[pygame.K_SPACE]:
            bullets.append(Bullet(player.rect.centerx, player.rect.top))

        # 移动子弹
        for bullet in bullets[:]:
            bullet.move()
            if bullet.rect.y < 0:
                bullets.remove(bullet)

        # 生成敌人
        if random.randint(1, 30) == 1:
            enemies.append(Enemy())

        # 移动敌人并检测碰撞
        for enemy in enemies[:]:
            enemy.move()
            if enemy.rect.y > HEIGHT:
                enemies.remove(enemy)
            for bullet in bullets[:]:
                if bullet.rect.colliderect(enemy.rect):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    break

        # 绘制
        screen.fill(WHITE)
        player.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

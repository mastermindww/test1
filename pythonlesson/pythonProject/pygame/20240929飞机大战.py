import pygame
import random

# 初始化 pygame
pygame.init()

# 设置窗口
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("飞机大战")

# 颜色定义
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# 飞机类
class Plane:
    def __init__(self):
        self.image = pygame.Surface((50, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))

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
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(x, y))

    def move(self):
        self.rect.y -= 5

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# 敌机类
class Enemy:
    def __init__(self):
        self.image = pygame.Surface((50, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(random.randint(0, WIDTH - 50), 0))

    def move(self):
        self.rect.y += 3

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# 游戏主循环
def main():
    clock = pygame.time.Clock()
    plane = Plane()
    bullets = []
    enemies = []
    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            plane.move(-5)
        if keys[pygame.K_RIGHT]:
            plane.move(5)
        if keys[pygame.K_SPACE]:
            bullets.append(Bullet(plane.rect.centerx, plane.rect.top))

        # 更新子弹和敌机
        for bullet in bullets[:]:
            bullet.move()
            if bullet.rect.y < 0:
                bullets.remove(bullet)

        if random.randint(1, 20) == 1:  # 敌机生成概率
            enemies.append(Enemy())

        for enemy in enemies[:]:
            enemy.move()
            if enemy.rect.y > HEIGHT:
                enemies.remove(enemy)
            # 碰撞检测
            if enemy.rect.colliderect(plane.rect):
                running = False  # 碰撞后结束游戏
            for bullet in bullets[:]:
                if bullet.rect.colliderect(enemy.rect):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1  # 得分增加
                    break

        # 绘制
        screen.fill((0, 0, 0))
        plane.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

        # 绘制得分
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {score}', True, GREEN)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

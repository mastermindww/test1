import pygame
import random

# 初始化 pygame
pygame.init()

# 设置窗口
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("打砖块游戏")

# 颜色定义
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 球类
class Ball:
    def __init__(self):
        self.radius = 10
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed_x = random.choice([-4, 4])
        self.speed_y = -4

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # 碰撞边界
        if self.x <= self.radius or self.x >= WIDTH - self.radius:
            self.speed_x *= -1
        if self.y <= self.radius:
            self.speed_y *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, BLUE, (self.x, self.y), self.radius)

# 球拍类
class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 10
        self.x = (WIDTH - self.width) // 2
        self.y = HEIGHT - self.height - 10
        self.speed = 10

    def move(self, dx):
        self.x += dx
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH - self.width:
            self.x = WIDTH - self.width

    def draw(self, surface):
        pygame.draw.rect(surface, GREEN, (self.x, self.y, self.width, self.height))

# 砖块类
class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 60, 20)
        self.color = RED

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

# 游戏主循环
def main():
    clock = pygame.time.Clock()
    ball = Ball()
    paddle = Paddle()
    bricks = [Brick(x * 70 + 30, y * 30 + 30) for y in range(5) for x in range(8)]
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move(-paddle.speed)
        if keys[pygame.K_RIGHT]:
            paddle.move(paddle.speed)

        ball.move()

        # 检查球与球拍碰撞
        if (paddle.x < ball.x < paddle.x + paddle.width and
                ball.y + ball.radius >= paddle.y):
            ball.speed_y *= -1

        # 检查球与砖块碰撞
        for brick in bricks[:]:
            if brick.rect.collidepoint(ball.x, ball.y):
                ball.speed_y *= -1
                bricks.remove(brick)
                break

        # 检查游戏结束
        if ball.y >= HEIGHT:
            running = False

        # 绘制
        screen.fill(WHITE)
        ball.draw(screen)
        paddle.draw(screen)
        for brick in bricks:
            brick.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

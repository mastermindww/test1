import pygame
import random

# 初始化 pygame
pygame.init()

# 设置窗口
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("接球游戏")

# 颜色定义
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 球类
class Ball:
    def __init__(self):
        self.radius = 15
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = 0
        self.speed = random.randint(2, 5)

    def fall(self):
        self.y += self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, BLUE, (self.x, self.y), self.radius)

# 接球器类
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

# 游戏主循环
def main():
    clock = pygame.time.Clock()
    paddle = Paddle()
    balls = []
    score = 0
    running = True

    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move(-paddle.speed)
        if keys[pygame.K_RIGHT]:
            paddle.move(paddle.speed)

        # 随机生成球
        if random.randint(1, 20) == 1:
            balls.append(Ball())

        # 更新球位置
        for ball in balls[:]:
            ball.fall()
            # 检测球是否接住
            if ball.y > HEIGHT:
                balls.remove(ball)
            elif (paddle.x < ball.x < paddle.x + paddle.width and
                  ball.y + ball.radius >= paddle.y):
                balls.remove(ball)
                score += 1

        # 绘制接球器和球
        paddle.draw(screen)
        for ball in balls:
            ball.draw(screen)

        # 显示得分
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {score}', True, (0, 0, 0))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()

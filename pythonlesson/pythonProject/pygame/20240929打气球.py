import pygame
import random

# 初始化 pygame
pygame.init()

# 设置窗口
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("打气球")

# 颜色定义
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# 气球类
class Balloon:
    def __init__(self):
        self.color = random.choice([RED, BLUE, GREEN])
        self.radius = random.randint(15, 30)
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = HEIGHT + self.radius
        self.speed = random.randint(1, 5)

    def move(self):
        self.y -= self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def is_clicked(self, pos):
        return (pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2 < self.radius ** 2

# 游戏主循环
def main():
    clock = pygame.time.Clock()
    balloons = []
    score = 0
    running = True

    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for balloon in balloons[:]:
                    if balloon.is_clicked(mouse_pos):
                        balloons.remove(balloon)
                        score += 1
                        break

        # 生成气球
        if random.randint(1, 20) == 1:
            balloons.append(Balloon())

        # 更新气球位置
        for balloon in balloons[:]:
            balloon.move()
            if balloon.y < -balloon.radius:
                balloons.remove(balloon)

        # 绘制气球
        for balloon in balloons:
            balloon.draw(screen)

        # 显示得分
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {score}', True, (0, 0, 0))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()

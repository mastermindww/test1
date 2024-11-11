import pygame
import random

# 初始化 pygame
pygame.init()

# 设置窗口
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("跳跃游戏")

# 颜色定义
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 玩家类
class Player:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT - 60
        self.width = 40
        self.height = 60
        self.vel = 5
        self.is_jumping = False
        self.jump_count = 10

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, (self.x, self.y, self.width, self.height))

    def jump(self):
        if self.is_jumping:
            if self.jump_count >= -10:
                neg = 1 if self.jump_count >= 0 else -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = 10

# 障碍物类
class Obstacle:
    def __init__(self):
        self.x = WIDTH
        self.y = HEIGHT - 60
        self.width = 40
        self.height = 60
        self.vel = 7

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.x, self.y, self.width, self.height))

    def move(self):
        self.x -= self.vel

# 游戏主循环
def main():
    clock = pygame.time.Clock()
    player = Player()
    obstacles = []
    score = 0
    running = True

    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if not player.is_jumping:
                player.is_jumping = True

        player.jump()

        # 生成障碍物
        if random.randint(1, 30) == 1:
            obstacles.append(Obstacle())

        # 移动障碍物
        for obstacle in obstacles[:]:
            obstacle.move()
            if obstacle.x < 0:
                obstacles.remove(obstacle)
                score += 1  # 增加得分

            # 检测碰撞
            if (player.x < obstacle.x + obstacle.width and
                player.x + player.width > obstacle.x and
                player.y < obstacle.y + obstacle.height and
                player.y + player.height > obstacle.y):
                running = False  # 游戏结束

        screen.fill(WHITE)
        player.draw(screen)
        for obstacle in obstacles:
            obstacle.draw(screen)

        pygame.display.flip()

    print(f"游戏结束! 得分: {score}")
    pygame.quit()

if __name__ == "__main__":
    main()

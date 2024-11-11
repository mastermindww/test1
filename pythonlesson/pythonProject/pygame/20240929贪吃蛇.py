import pygame
import time
import random

# 初始化 pygame
pygame.init()

# 设置窗口
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇")

# 颜色定义
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 蛇类
class Snake:
    def __init__(self):
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = 'RIGHT'

    def move(self):
        head = self.body[0][:]
        if self.direction == 'UP':
            head[1] -= 10
        elif self.direction == 'DOWN':
            head[1] += 10
        elif self.direction == 'LEFT':
            head[0] -= 10
        elif self.direction == 'RIGHT':
            head[0] += 10
        self.body.insert(0, head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1][:])

    def change_direction(self, new_direction):
        if (new_direction == 'UP' and self.direction != 'DOWN') or \
           (new_direction == 'DOWN' and self.direction != 'UP') or \
           (new_direction == 'LEFT' and self.direction != 'RIGHT') or \
           (new_direction == 'RIGHT' and self.direction != 'LEFT'):
            self.direction = new_direction

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, (segment[0], segment[1], 10, 10))

# 食物类
class Food:
    def __init__(self):
        self.position = [random.randint(0, (WIDTH-10)//10)*10, random.randint(0, (HEIGHT-10)//10)*10]

    def spawn(self):
        self.position = [random.randint(0, (WIDTH-10)//10)*10, random.randint(0, (HEIGHT-10)//10)*10]

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.position[0], self.position[1], 10, 10))

# 游戏主循环
def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction('UP')
                elif event.key == pygame.K_DOWN:
                    snake.change_direction('DOWN')
                elif event.key == pygame.K_LEFT:
                    snake.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction('RIGHT')

        snake.move()

        # 碰撞检测
        if snake.body[0] == food.position:
            snake.grow()
            food.spawn()
            score += 1

        # 检查边界和自撞
        if (snake.body[0][0] < 0 or snake.body[0][0] >= WIDTH or
            snake.body[0][1] < 0 or snake.body[0][1] >= HEIGHT or
            snake.body[0] in snake.body[1:]):
            running = False

        # 绘制
        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)

        # 显示得分
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(15)

    pygame.quit()

if __name__ == "__main__":
    main()

from snake import Snake
import pygame, random

def draw_snake(s):
    pygame.draw.rect(screen, (255, 255, 255), (s.pos[0], s.pos[1], 10, 10))
    if s.point is not None:
        draw_snake(s.point)
def draw_food(f):
    pygame.draw.rect(screen, (255, 0, 0), (f[0], f[1], 10, 10))

pygame.init()
info = pygame.display.Info()
screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
snake = Snake()
snake.add_head()
is_running = True
food = (random.randint(0, 71) * 10, random.randint(0, 47) * 10)
screen.fill((0, 0, 0))

while is_running:
    is_running = not snake.is_dead()
    if snake.read_head()[0] < 0 or snake.read_head()[0] >= 720 or snake.read_head()[1] < 0 or snake.read_head()[1] >= 480:
        is_running = False
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.read_to() != "bottom":
                snake.handle_to("top")
            elif event.key == pygame.K_DOWN and snake.read_to() != "top":
                snake.handle_to("bottom")
            elif event.key == pygame.K_LEFT and snake.read_to() != "right":
                snake.handle_to("left")
            elif event.key == pygame.K_RIGHT and snake.read_to() != "left":
                snake.handle_to("right")
            elif event.key == pygame.K_ESCAPE:
                is_running = False
                break
    if snake.is_in_snake(snake.read_head(), snake.read_pos().point):
        is_running = False
        break
    if food == snake.read_head():
        food = (random.randint(0, 71) * 10, random.randint(0, 47) * 10)
        snake.add_head()
    snake.add_head()
    snake.cut_tail()
    screen.fill((0, 0, 0))
    clock.tick(10)
    draw_snake(snake.read_pos())
    draw_food(food)
    pygame.display.update()

import pygame
import colors
from random import randint

window_height = 840
window_width = 800
window_dimensions = window_width, window_height

segment_size = 20

key_map = {
    273: "Up",
    274: "Down",
    275: "Right",
    276: "Left"
}

pygame.init()
pygame.display.set_caption("Snake")


clock = pygame.time.Clock()
screen = pygame.display.set_mode(window_dimensions)


def check_collisions(snake_position):
    head_x_position, head_y_position = snake_position[0]

    return (
        head_x_position in (-20, window_width) or head_y_position in (20, window_height) or (head_x_position, head_y_position in snake_position[1:])
    )


def check_food_collision(snake_position, food_position):
    if snake_position[0] == food_position:
        snake_position.append(snake_position[-1])

        return True


def draw_objects(snake_position, food_position):
    pygame.draw.rect(screen, colors.food, [food_position, (segment_size, segment_size)])

    for x, y in snake_position:
        pygame.draw.rect(screen, colors.snake, [x, y, segment_size, segment_size])


def move_snake(snake_position, direction):
    head_x_position, head_y_positon = snake_position[0]
    
    if direction == "Left":
        new_head_position = (head_x_position - segment_size, head_y_positon)
    elif direction == "Right":
        new_head_position = (head_x_position + segment_size, head_y_positon)
    elif direction == "Down":
        new_head_position = (head_x_position, head_y_positon + segment_size)
    elif direction == "Up":
        new_head_position = (head_x_position, head_y_positon - segment_size)

    snake_position.insert(0, new_head_position)
    del snake_position[-1]



def on_key_press(event , current_direction):
    
    key = event.__dict__["key"]
    new_direction = key_map.get(key)

    all_directions = ("Up", "Down", "Left", "Right")
    opposite_direction = ({"Up", "Down"}, {"Left", "Right"})

    if (new_direction in all_directions and {new_direction, current_direction} not in opposite_direction):
        return new_direction
    
    return current_direction


def set_new_food_position(snake_position):
    while True:
        x_position = randint(0, 39) * segment_size
        y_position = randint(2, 41) * segment_size

        food_position = (x_position, y_position)

        if food_position not in snake_position:
            return food_position



def play_game():
    score = 0

    current_direction = "Right"
    snake_position = [(100,100), (80,100), (60,100)]
    food_position = set_new_food_position(snake_position)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                current_direction = on_key_press(event, current_direction)

        screen.fill(colors.background)
        draw_objects(snake_position, food_position)

        font = pygame.font.Font(None, 28)
        text = font.render(f"score: {score}", True, colors.text)
        screen.blit(text, (10, 10))

        pygame.display.update()

        move_snake(snake_position, current_direction)

        if check_collisions(snake_position):
            return    
        
        if check_food_collision(snake_position, food_position):
            food_position = set_new_food_position(snake_position)

            score += 1

        clock.tick(10)

play_game()

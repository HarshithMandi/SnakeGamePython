import random
from tkinter import *

# Constants for game configuration
GAME_WIDTH = 500
GAME_HEIGHT = 500
SPEED = 100  
SPACE_SIZE = 25
BODY_PARTS = 1  
SNAKE_COLOUR = '#26719E'
FOOD_COLOUR = "#4CE70F"
BG_COLOUR = "#c4c4c4"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # Initialize the snake's body
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        # Create rectangles for each part of the snake's body
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        # Randomly place the food within the boundaries of the game area
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]

        # Draw the food on the canvas
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOUR, tag="food")

def next_turn(snake, food):
    # Get the current head coordinates of the snake
    x, y = snake.coordinates[0]

    # Move the snake in the current direction
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Add new coordinates for the snake's head
    snake.coordinates.insert(0, (x, y))

    # Check if the snake eats the food
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score

        score += 1
        label.config(text=f"Score: {score}")

        # Remove the old food and create a new one
        canvas.delete("food")
        food = Food()
    else:
        # Remove the last segment of the snake if no food is eaten
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # Create a new head for the snake
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR, tag="snake")
    snake.squares.insert(0, square)

    # Check for collisions
    if check_collisions(snake):
        game_over()
    else:
        # Schedule the next turn
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction

    # Prevent the snake from reversing its direction directly
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]

    # Check if the snake collides with the boundaries of the game area
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    # Check if the snake collides with itself
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():
    # Display a game over message
    canvas.delete(ALL)
    canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2, font=('Helvetica', 50), text="GAME OVER", fill="red", tag="gameover")

window = Tk()
window.title("SNAKE")
window.resizable(False, False)

# Initialize the score and direction
score = 0
direction = 'down'

# Create a label for displaying the score
label = Label(window, text=f"Score: {score}", font=('Helvetica', 20))
label.pack()

# Create a canvas for the game
canvas = Canvas(window, bg=BG_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

# Calculate the center of the screen to place the game window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create the snake and food objects
snake = Snake()
food = Food()

# Bind the arrow keys to change the snake's direction
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# Start the game
next_turn(snake, food)

window.mainloop()

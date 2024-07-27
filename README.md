### Snake Game Documentation

#### Overview

This Snake game is implemented using Python's `tkinter` library. It provides a graphical interface where a player controls a snake that moves around the canvas to eat food, which causes the snake to grow. The game ends if the snake collides with itself or the boundaries of the game area. The player can restart the game after it ends.

#### Constants

- `GAME_WIDTH` (int): Width of the game canvas (500 pixels).
- `GAME_HEIGHT` (int): Height of the game canvas (500 pixels).
- `SPEED` (int): Speed of the snake movement (100 milliseconds per move).
- `SPACE_SIZE` (int): Size of each square or cell on the canvas (25 pixels).
- `BODY_PARTS` (int): Initial number of segments in the snake's body (1).
- `SNAKE_COLOUR` (str): Color of the snake (`'#26719E'`).
- `FOOD_COLOUR` (str): Color of the food (`'#4CE70F'`).
- `BG_COLOUR` (str): Background color of the canvas (`'#c4c4c4'`).

#### Classes

1. **`Snake` Class**
   - **Attributes**:
     - `body_size`: Number of segments in the snake's body.
     - `coordinates`: List of tuples representing the positions of each segment.
     - `squares`: List of canvas rectangle IDs representing the snake's segments.
   - **Methods**:
     - `__init__()`: Initializes the snake with its starting position and draws it on the canvas.

2. **`Food` Class**
   - **Attributes**:
     - `coordinates`: Tuple representing the position of the food.
   - **Methods**:
     - `__init__()`: Randomly places food on the canvas and draws it.

#### Functions

- **`next_turn(snake, food)`**
  - Updates the snake's position based on its direction.
  - Checks if the snake has eaten the food or collided with itself or the boundaries.
  - Schedules the next turn of the game.

- **`change_direction(new_direction)`**
  - Changes the direction of the snake based on user input.
  - Prevents the snake from reversing directly.

- **`check_collisions(snake)`**
  - Checks if the snake has collided with the canvas boundaries or itself.

- **`game_over()`**
  - Displays a "GAME OVER" message on the canvas.
  - Optionally, a restart button could be added here for functionality enhancement.

#### Game Initialization and Main Loop

- **`window` (Tk)**: The main application window.
- **`score` (int)**: Player's score, initialized to 0.
- **`direction` (str)**: Initial direction of the snake, set to 'down'.
- **`label` (Label)**: Displays the current score.
- **`canvas` (Canvas)**: The game area where the snake and food are drawn.

#### Key Bindings

- **Arrow Keys**: Change the direction of the snake (`<Left>`, `<Right>`, `<Up>`, `<Down>`).

#### Start the Game

- The `next_turn` function is called to start the game loop.
- The `window.mainloop()` function keeps the game window open and responsive.

#### Notes

- The `game_over()` function displays a message but does not include functionality to restart the game. To add a restart button, you can modify the `game_over()` function accordingly.

This documentation covers the essential components and functionality of the Snake game implemented in Python using `tkinter`. Adjustments or enhancements can be made to fit specific requirements or to add additional features like a restart option.

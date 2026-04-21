import tkinter as tk
import random

WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20
BACKGROUND = "#111111"
SNAKE_COLOR = "#39ff14"
FOOD_COLOR = "#ff4d4d"
TEXT_COLOR = "#ffffff"
SPEED = 120

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BACKGROUND, highlightthickness=0)
        self.canvas.pack()

        self.score = 0
        self.direction = "Right"
        self.game_over = False

        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.create_food()

        self.root.bind("<Up>", lambda event: self.change_direction("Up"))
        self.root.bind("<Down>", lambda event: self.change_direction("Down"))
        self.root.bind("<Left>", lambda event: self.change_direction("Left"))
        self.root.bind("<Right>", lambda event: self.change_direction("Right"))
        self.root.bind("w", lambda event: self.change_direction("Up"))
        self.root.bind("s", lambda event: self.change_direction("Down"))
        self.root.bind("a", lambda event: self.change_direction("Left"))
        self.root.bind("d", lambda event: self.change_direction("Right"))
        self.root.bind("r", lambda event: self.restart_game())

        self.update()

    def create_food(self):
        while True:
            x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, new_direction):
        opposite = {
            "Up": "Down",
            "Down": "Up",
            "Left": "Right",
            "Right": "Left"
        }
        if not self.game_over and opposite[new_direction] != self.direction:
            self.direction = new_direction

    def move_snake(self):
        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            head_y -= CELL_SIZE
        elif self.direction == "Down":
            head_y += CELL_SIZE
        elif self.direction == "Left":
            head_x -= CELL_SIZE
        elif self.direction == "Right":
            head_x += CELL_SIZE

        new_head = (head_x, head_y)

        if (
            head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT or
            new_head in self.snake
        ):
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self.create_food()
        else:
            self.snake.pop()

    def draw(self):
        self.canvas.delete("all")

        self.canvas.create_text(
            10, 10,
            anchor="nw",
            text=f"Score: {self.score}",
            fill=TEXT_COLOR,
            font=("Arial", 16, "bold")
        )

        fx, fy = self.food
        self.canvas.create_oval(
            fx + 2, fy + 2,
            fx + CELL_SIZE - 2, fy + CELL_SIZE - 2,
            fill=FOOD_COLOR,
            outline=""
        )

        for i, (x, y) in enumerate(self.snake):
            color = SNAKE_COLOR if i == 0 else "#2ecc71"
            self.canvas.create_rectangle(
                x + 1, y + 1,
                x + CELL_SIZE - 1, y + CELL_SIZE - 1,
                fill=color,
                outline=""
            )

        if self.game_over:
            self.canvas.create_rectangle(80, 220, 520, 380, fill="#000000", outline="#ffffff")
            self.canvas.create_text(
                WIDTH // 2, 270,
                text="GAME OVER",
                fill="#ff4d4d",
                font=("Arial", 28, "bold")
            )
            self.canvas.create_text(
                WIDTH // 2, 315,
                text=f"Final Score: {self.score}",
                fill=TEXT_COLOR,
                font=("Arial", 18)
            )
            self.canvas.create_text(
                WIDTH // 2, 350,
                text="Press R to Restart",
                fill=TEXT_COLOR,
                font=("Arial", 16)
            )

    def update(self):
        if not self.game_over:
            self.move_snake()
        self.draw()
        self.root.after(SPEED, self.update)

    def restart_game(self):
        self.score = 0
        self.direction = "Right"
        self.game_over = False
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.create_food()

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
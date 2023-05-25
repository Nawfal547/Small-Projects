from tkinter import *
import random 

# These are all controls that do not change in the game 
GAME_WIDTH = 700
GAME_HEIGHT = 500
SPEED = 70
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#FFFFFF"
FOOD_COLOR = "#13294B"
BACKGROUND_COLOR = "#4B9CD3"

class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # This for loop will be creating a list of coordinates
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag = "Snake")
            self.squares.append(square)

class Food:
    # The init is what constructs the object
    def __init__(self):

        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE) - 1) * SPACE_SIZE
        # This X and Y give random cordinates within the space of the game
        self.coordinates = [x,y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tag = "food")
        # This creates the actual oval that the snake eats.

def next_turn(snake, food):
    
    x, y = snake.coordinates[0] # the head of the snake. and coordiantes stored in x, y

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0,(x, y))

    square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        # If the snake touches the food in the food coordinates then the score goes up and new food is spawned
        global score

        score += 1

        label.config(text = "Score {}".format(score))

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]
    
    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)
    

def change_direction(new_direction):
    
# This allows the snake to change direction. So if it goes left it does not go right and so on
    global direction 

    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction


def check_collisions(snake):
    

    x, y = snake.coordinates[0]
    # If the snake hits the sides
    if x < 0 or x >= GAME_WIDTH:
        return True  
    # If it hits the up and down area
    elif y < 0 or y >= GAME_HEIGHT:
        return True  
    # If the snake hits itself 
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
        
    return False
    

def game_over():
    
    canvas.delete(ALL) # Deletes everything that was there previously
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font =("consolas", 70), text = "GAME OVER", fill = "white", tag = "gameover") #game over text


window = Tk()
window.title("Snake Game")
window.resizable(False, False)
# Creates the window the game will be in 

score = 0
direction = "down"

label = Label(window, text = "Score: {}".format(score), font = ("consolas", 40))
label.pack()
# This creates the score that you see at the top of the game 

canvas = Canvas(window, bg= BACKGROUND_COLOR, height = GAME_HEIGHT, width = GAME_WIDTH )
canvas.pack()
# Creates the canvas the game will be on 

# all of the lines below to the main loop were made to center the game window
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))


window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction("left"))
window.bind('<Right>', lambda event: change_direction("right"))
window.bind('<Up>', lambda event: change_direction("up"))
window.bind('<Down>', lambda event: change_direction("down"))


snake = Snake()
food = Food()


next_turn(snake, food)

window.mainloop()

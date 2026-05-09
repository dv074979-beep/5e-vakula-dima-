from turtle import *

speed(0)
pensize(2)
color("black")

step = 20

def move_forward():
    forward(step)

def move_backward():
    backward(step)

def turn_left():
    left(15)

def turn_right():
    right(15)

def pen_up_toggle():
    if isdown():
        penup()
        color("gray")
    else:
        pendown()
        color("black")

def clear_screen():
    clear()
    home()
    pendown()
    color("black")

def increase_step():
    global step
    step = min(step + 5, 100)

def decrease_step():
    global step
    step = max(step - 5, 5)

def change_color_red():
    color("red")

def change_color_blue():
    color("blue")

def change_color_green():
    color("green")

def change_color_black():
    color("black")

screen = Screen()
screen.title("Черепашья графика — управление с клавиатуры")
screen.bgcolor("white")
screen.setup(width=800, height=600)

screen.listen()
screen.onkey(move_forward,    "Up")
screen.onkey(move_backward,   "Down")
screen.onkey(turn_left,       "Left")
screen.onkey(turn_right,      "Right")
screen.onkey(pen_up_toggle,   "space")
screen.onkey(clear_screen,    "c")
screen.onkey(increase_step,   "plus")
screen.onkey(decrease_step,   "minus")
screen.onkey(change_color_red,   "r")
screen.onkey(change_color_blue,  "b")
screen.onkey(change_color_green, "g")
screen.onkey(change_color_black, "k")

print("=== Управление черепашкой ===")
print("Стрелки       — движение и поворот")
print("Пробел        — поднять/опустить перо")
print("C             — очистить экран")
print("+/-           — увеличить/уменьшить шаг")
print("R/B/G/K       — цвет: красный/синий/зелёный/чёрный")

mainloop()

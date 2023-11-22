import turtle

# scriem toate comenzile de la taste

def draw_forward():
    turtle.forward(10)
    with open ("keys.txt", "a") as file:
        file.write("w")


def draw_backward():
    turtle.backward(10)
    with open ("keys.txt", "a") as file:
        file.write("s")

def turn_right():
    turtle.right(45)
    with open ("keys.txt", "a") as file:
        file.write("d")

def turn_left():
    turtle.left(45)
    with open ("keys.txt", "a") as file:
        file.write("a")

def pick_up():
    turtle.up()
    with open ("keys.txt", "a") as file:
        file.write("f")

def turn_down():
    turtle.down()
    with open("keys.txt","a") as file:
        file.write("g")

#fiecare tasta este apelata
def keys():
    turtle.onkey(draw_forward, 'w')
    turtle.onkey(draw_backward, 's')
    turtle.onkey(turn_right, 'd')
    turtle.onkey(turn_left, 'a')
    turtle.onkey(pick_up, 'f')
    turtle.onkey(turn_down, 'g')
    turtle.onkey(exit, 'e')
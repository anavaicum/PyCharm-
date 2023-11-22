import turtle

def deseneaza_dreptunghiuri():
    t = turtle.Pen()
    t.speed("slow")
    t.up()
    t.goto(-50,50)
    t.down()
    for _ in range(2):
        t.forward(200)
        t.left(90)
        t.forward(100)
        t.left(90)

    t.up()
    t.goto(25, 90)
    t.down()
    for _ in range(2):
      t.forward(50)
      t.left(90)
      t.forward(25)
      t.left(90)
    t.reset()
def deseneaza_inimioara():
    t = turtle.Pen()
    t.speed("slow")
    t.color("red", "pink")
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.setheading(60)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()
    t.reset()
    turtle.done()



def deseneaza_casute():
    t = turtle.Pen()
    s = turtle.Pen()
    t.speed("slow")
    s.speed("slow")
    #casa1
    t.up()
    t.goto(-250, -100)
    t.down()

    t.color("yellow", "yellow")
    t.begin_fill()
    for _ in range(4):  #patratul casei (peretii)
        t.forward(200)
        t.left(90)
    t.end_fill()

    t.up()              #pozitionez turtle pentru a face usa la mijlocul segmentului de 200
    t.goto(-190, -100)
    t.down()

    t.color("black", "black")
    t.begin_fill()
    for _ in range(2):  #usa
        t.forward(75)
        t.left(90)
        t.forward(80)
        t.left(90)
    t.end_fill()

    t.color("blue", "blue")
    t.begin_fill()
    t.up()              #geam rotund
    t.goto(-155, 10)
    t.down()
    t.circle(35)
    t.end_fill()

    t.color("red", "red")
    t.begin_fill()
    t.up()              #acoperis (facem un triunghi echilateral)
    t.goto(-250, 100)
    t.down()
    for _ in range(3):
        t.forward(200)
        t.left(120)
    t.end_fill()

    #casa2
    s.up()
    s.goto(0, -100)
    s.down()

    s.color("beige", "beige")
    s.begin_fill()
    for _ in range(4):
        s.forward(200)
        s.left(90)
    s.end_fill()

    s.up()
    s.goto(60, -100)
    s.down()

    s.color("brown", "brown")
    s.begin_fill()
    for _ in range(2):
        s.forward(75)
        s.left(90)
        s.forward(80)
        s.left(90)
    s.end_fill()

    s.color("cyan", "cyan")
    s.begin_fill()
    # geam
    s.up()
    s.goto(95, 10)
    s.down()
    s.circle(35)
    s.end_fill()

    s.color("red", "red")
    s.begin_fill()
    s.up()                         # acoperis
    s.goto(0, 100)
    s.down()
    for _ in range(3):
       s.forward(200)
       s.left(120)

    s.end_fill()

    t.reset()
    s.reset()



while True:
    alegere = input("Alege o cifra: ")

    if alegere == "1":
        deseneaza_dreptunghiuri()
    elif alegere == "2":
        deseneaza_inimioara()
    elif alegere == "3":
        deseneaza_casute()
    else:
        break

from alfabet import *
from key_taste import *
import turtle



def desen_automat():
    word = input("Cuvantul sau prpopzitia ta este:")
    for ch in word:
        if ch in dictionar:
            dictionar[ch]()
        else:
            for ch in dic[ch]:
                if ch == 'w':
                    draw_forward()
                if ch == 's':
                    draw_backward()
                if ch == 'd':
                    turn_right()
                if ch == 'a':
                    turn_left()
                if ch == 'f':
                    pick_up()
                if ch == 'g':
                    turn_down()


    turtle.done()


# turtle.done: ne asiguram ca pornim ferestrele doar daca vrem

def desen_manual():
    newchar = input("new char: ")
    with open("keys.txt", "a") as file:
        file.write(f"{newchar} : ")
    keys()
    turtle.listen()
    turtle.done()


def main():
    with open("keys.txt", "a") as file:  # append mode
        file.write("\n")
    print('''
    Alege:
    1.desen manual
    2.desen automat

    ''')

    optiune = int(input())
    if optiune == 2:
        desen_automat()
    else:
        if optiune == 1:
            desen_manual()

main()
import random

def alegere_computer():
    variante=["Schere", "Stein", "Papier"]
    return random.choice(variante)


def alegere_om():
    print("1. Schere")
    print("2. Stein")
    print("3. Papier")

    while True:
        alegere = input("Alege: ")

        if alegere == "1":
            return "Schere"
        elif alegere == "2":
            return "Stein"
        elif alegere == "3":
            return "Papier"
        else:
            break

def determinare_castigator(om, computer):
    if om == computer:
        return "Unentschieden"
    elif (om == "Schere" and computer == "Papier") or (om == "Stein" and computer == "Schere") or (om == "Papier" and computer == "Stein"):
        return "Benutzer gewinnt"
    else:
        return "Computer gewinnt"


def play_game():
    # Jocul principal care gestionează 3 runde și determină un câștigător final.
    om_score = 0
    computer_score = 0

    for runda in range(1, 4):
        print(f"Runde {runda}:")
        om = alegere_om()
        computer = alegere_computer()
        print(f"Computer wählt: {computer}")
        result = determinare_castigator(om, computer)
        print(f"{result} in dieser Runde.\n")

        if result == "Benutzer gewinnt":
            om_score += 1
        elif result == "Computer gewinnt":
            computer_score += 1

    if om_score > computer_score:
        print("Benutzer gewinnt das Spiel!")
    elif computer_score > om_score:
        print("Computer gewinnt das Spiel!")
    else:
        print("Das Spiel endet unentschieden!")


if __name__ == "__main__":
    play_game()
import random
import time
import sys

from matplotlib.pyplot import switch_backend


def main():
    print("\nWelcome to Wordle!\n\nRules:")

    print("1. You have 6 attempts to guess the word of the day.")
    print("2. The word is a 5 letter word.")
    print("3. Letters guessed correctly will be shown")
    print("4. Letters guessed correctly but in the wrong position will be shown in curly brackets.")
    print("5. Letters not guessed will be shown as underscores.\n\nLet's play!\n")

    print(" _   _   _   _   _ ")
    print(" _   _   _   _   _ ")
    print(" _   _   _   _   _ ")
    print(" _   _   _   _   _ ")
    print(" _   _   _   _   _ \n")

    # Move the cursor up one line and clear the line

    w = random.choice(wordOfTheDay())
    game = wordle(w)
    if game[0]:
        if game[1] == 1:
            print(
                f"\nCongratulations! You guessed the word in {game[1]} attempt. You're a Wordle Master!")
        elif game[1] == 2:
            print(
                f"\nCongratulations! You guessed the word in {game[1]} attempts. That was quick!")
        elif game[1] == 3:
            print(
                f"\nCongratulations! You guessed the word in {game[1]} attempts. Not bad!")
        elif game[1] == 4:
            print(
                f"\nCongratulations! You guessed the word in {game[1]} attempts. You're getting there!")
        elif game[1] == 5:
            print(
                f"\nCongratulations! You guessed the word in {game[1]} attempts. That was close!")

    else:
        print(f"\nYou ran out of attempts. The word was: {w}\n")


def wordle(w):
    cont = 1
    aux = 6
    comp = ""

    while (cont <= 5 and comp != w):
        comp = str(
            input(f"[{cont}] Enter a 5 letter word: ")).upper()

        # Check if the input is a 5 letter word and if it is in the list
        aux, comp = check(comp, aux)

        if comp == w:  # If the word is guessed correctly
            return (True, cont)

        else:
            sys.stdout.write('\x1b[s')
            time.sleep(2)
            sys.stdout.write(f'\x1b[{cont + aux}A')  # Move up one line
            sys.stdout.write('\x1b[2K')  # Clear the line
            compareWords(w, comp)
            sys.stdout.write('\x1b[u')

        cont += 1
        print(" ")

    return (False, cont)


def check(comp, aux):
    while ((len(comp) != 5) or (comp not in wordOfTheDay()) or (comp.isalpha() == False)):
        if comp not in wordOfTheDay():
            comp = str(
                input("The word is not in the list. Please try again: ")).upper()
            aux += 1
        elif comp.isalpha() == False:
            comp = str(
                input("Please enter a valid 5 letter word: ")).upper()
            aux += 1
        else:
            comp = str(input("Please enter a 5 letter word: ")).upper()
            aux += 1
    return aux, comp


def compareWords(w, comp):
    for i in range(len(comp)):
        if comp[i] == w[i]:
            print(f" {comp[i]}", end="  ")
        elif (comp[i] in w) and (comp[i] not in comp[:i]):
            print("{"+comp[i]+"}", end=" ")
        else:
            print(" _", end="  ")


def wordOfTheDay():
    l = open("./sgb-words.txt", "r")
    l1 = []
    words = l.readlines()
    l.close()
    for i in words:
        l1.append(i[:-1].upper())

    return l1


main()

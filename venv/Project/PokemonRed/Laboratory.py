import time #This allows us to pause between sentences
import sys #This helps with emulating the typing effect

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
def print_fast(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.5)

print_fast("\n\n" + rivalName + ": Gramps! I'm fed up with waiting!")
print_slow("\nOak: " + rivalName + "? Let me think... Oh, that's right. I told you to come! Just wait!")
print_slow("\nHere, " + name + "! There are 3 POKEMON here! Haha! They are inside the POKE BALLS. When I was young, I was a serious POKEMON trainer. In my old age, I have only 3 left, but you can have one! Choose!")
print_fast("\n" + rivalName + ": Hey! Gramps! What about me?")
print_slow("\nOak: Be patient! " + rivalName + ", you can have one too!")

while true:
    pokemon = input("Do you want the plant POKEMON, Bulbasaur?\nThe fire POKEMON, Charmander?\nOr the water POKEMON, Squirtle?\n")
    if (pokemon == Charmander | pokemon == charmander):
        print("\nYou have chosen Charmander!")
        print_fast("\n" + rivalName + ": I'll take Squirtle then!")
    elif (pokemon == Bulbasaur | pokemon == bulbasaur):
        print("\nYou have chosen Bulbasaur!")
        print_fast("\n" + rivalName + ": I'll take Charmander then!")
    elif (pokemon == Squirtle | pokemon == squirtle):
        print("\nYou have chosen Squirtle!")
        print_fast("\n" + rivalName + ": I'll take Bulbasaur then!")
print_slow("\n\nOak: If a wild POKEMON appears, your POKEMON can fight against it!")

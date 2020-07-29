'''Hello!! This is our text-based game!! The game uses the higher/lower mechanics of Top Trumps, placed inside the world of Pokemon Blue/Red/Yellow!
All text is taken from the game (so might be unnatural) and the storyline follows the story of Pokemon Red.

The functions are in almost reverse order, so they can call one another...

Future goals include:
- adding in the EXP system.
- items (currently buying potions and the Pokes system is pretty useless...) We want the player to be able to uses potions in battle and go to Pokemon Centers to heal
  this would involve passing the HP variable through
- multiple Pokemon and catching Pokemon...?
- More gyms and battles, of course!
- More descriptions of the routes and towns, whilst still being in the style of the games themselves.

Made by Mia Coupland and Rhea Kamath for Code First Girls' Introduction to Python.'''

import time #This allows us to pause between sentences
import sys #This helps with emulating the typing effect
import requests #This is for the API

#Here are the default variables
name = "Red" #This is your default name
rivalName = "Blue" #This is the default rival name
pokes = 0 #This is the integer to set the money that the player has
rivalPoke = 7 #Rival Pokemon's default is Squirtle
pokemon = 4 #Your default Pokemon is Charmander
win = False #Default win is... lose

#Code for the very end of the program, where we say thanks for playing and stuff...
def end(rivalName, name, pokemon, pokes, win):
    print_fast("\n\n\nTHE END\n")
    print_fast("\nThank you for completing our game, " + name + "!\nWe have worked hard over a week to produce this project for the Code First Girls Introduction to Python course.")
    print_fast("\nIt's not perfect but we are proud of our knock off Pokemon game and hope that you had fun!! <3\n\n")

#Determines what text appears when you win
#Added win and lose because I struggled to get the win variable to pass through functions otherwise!!
def win(rivalName, name, pokemon, pokes, win):
    pokes = pokes + 500
    if rivalName == "Quinn":
        print_slow("\nQuinn: You're strong. You obviously must have trained hard.")
        time.sleep(2)
        viridianCity(rivalName, name, pokemon, pokes, win)
    elif rivalName == "JRTRAINER":
        print_fast("\nJR.TRAINER: Darn! Light years isn't time! It measures distance!")
        print_fast("\nJR.TRAINER: You're pretty hot, but not as hot as BROCK!")
        time.sleep(1)
        brockLeader(rivalName, name, pokemon, pokes, win)
    elif rivalName == "BROCK":
        print_fast("\nBROCK: I took you for granted. As proof of your victory, here's the BOULDERBADGE! That's an official POKEMON LEAGUE BADGE!\nIts bearer's POKEMON become more powerful!")
        print_fast("\nThere are all kinds of trainers in the world! You appear to be very gifted as a POKEMON trainer! Go to the GYM in CERULEAN and test your abilities!")
        end()
    elif rivalName == "BUG CATCHER":
        print_fast("\nBUG CATCHER: No! CATERPIE can't cut it!")
        time.sleep(1)
        print_fast("\nBUG CATCHER: Ssh! You'll scare the bugs away!")
        time.sleep(2)
        pewterCity(rivalName, name, pokemon, pokes, win)
    else:
        print_fast("\n\n" + rivalName + ": WHAT? Unbelievable! I picked the wrong POKEMON!")
        print_fast("\n" + rivalName + ": Okay! I'll make my POKEMON fight to toughen it up!")
        print_fast("\n" + rivalName + ": " + name + "! Gramps! Smell you later!\n\n")
        palletTown(rivalName, name, pokemon, pokes, win)

#Determines what text appears when you lose
def lose(rivalName, name, pokemon, pokes, win):
    pokes = 0
    if rivalName == "Quinn":
        print_fast("\nCOOLTRAINER QUINN: Down and out...")
        print_fast("\n" + name + " is out of useable POKEMON!")
        print_fast("\n" + name + " blacked out!")
        time.sleep(1)
        routeOne(rivalName, name, pokemon, pokes, win)
    elif rivalName == "JRTRAINER":
        print_fast("\n" + name + " is out of useable POKEMON!")
        print_fast("\n" + name + " blacked out!")
        time.sleep(1)
        brockGym(rivalName, name, pokemon, pokes, win)
    elif rivalName == "BROCK":
        print_fast("\n" + name + " is out of useable POKEMON!")
        print_fast("\n" + name + " blacked out!")
        time.sleep(1)
        brockGym(rivalName, name, pokemon, pokes, win)
    elif rivalName == "BUG CATCHER":
        print_fast("\n" + name + " is out of useable POKEMON!")
        print_fast("\n" + name + " blacked out!")
        time.sleep(1)
        viridianForest(rivalName, name, pokemon, pokes, win)
    else:
        print_fast("\n\n" + rivalName + ": Yeah! Am I great or what?")
        print_fast("\n" + rivalName + ": Okay! I'll make my POKEMON fight to toughen it up!")
        print_fast("\n" + rivalName + ": " + name + "! Gramps! Smell you later!\n\n")
        palletTown(rivalName, name, pokemon, pokes, win)

#Assigns stats to your Pokemon from PokeAPI
def assignYourPokemon(pokemon):
    pokemonNumber = pokemon
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemonNumber)
    response = requests.get(url)
    pokemon = response.json()
    #declare variables for each nested stat
    hp = pokemon['stats'][0]['base_stat']
    attack = pokemon['stats'][1]['base_stat']
    defence = pokemon['stats'][2]['base_stat']
    specialAttack = pokemon['stats'][3]['base_stat']
    specialDefence = pokemon['stats'][4]['base_stat']

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'hp': hp,
        'attack': attack,
        'defence': defence,
        'special attack': specialAttack,
        'special defence': specialDefence,
    }

#Assigns stats to the rival Pokemon from PokeAPI
def assignRivalPokemon(rivalPoke):
    pokemonNumber = rivalPoke
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemonNumber)
    response = requests.get(url)
    pokemon = response.json()
    #declare variables for each nested stat
    hp = pokemon['stats'][0]['base_stat']
    attack = pokemon['stats'][1]['base_stat']
    defence = pokemon['stats'][2]['base_stat']
    specialAttack = pokemon['stats'][3]['base_stat']
    specialDefence = pokemon['stats'][4]['base_stat']

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'hp': hp,
        'attack': attack,
        'defence': defence,
        'special attack': specialAttack,
        'special defence': specialDefence,
    }

#Battle function. The core 'Top Trumps' style game.
def battle(rivalName, name, rivalPoke, pokemon, pokes, win):
    myPokemon = assignYourPokemon(pokemon)
    myPokemonName = myPokemon['name']
    print_fast('\n' + name + ' sent out {}!'.format(myPokemonName))

    rivalPokemon = assignRivalPokemon(rivalPoke)
    rivalPokemonName = rivalPokemon['name']
    print_fast("\n" + rivalName + ": Go, {}!".format(rivalPokemon['name']))

    myPokemonsHP = myPokemon['hp']
    rivalPokemonsHP = rivalPokemon['hp']

    #Runs until one Pokemon has fainted
    while myPokemon['hp'] > 0 or rivalPokemon['hp'] > 0:
        if rivalPokemonsHP <= 0:
            print_fast('\n' + name + ' wins the battle!')
            print_fast('\nYou got 500 poke for winning.')
            win(rivalName, name, pokemon, pokes, win)
        elif myPokemonsHP <= 0:
            lose(rivalName, name, pokemon, pokes, win)

        #Created stat choice and implemented a while loop so any typos are ignored and the program doesn't break out in confusion!!
        statChoice = ""
        while statChoice != "id" or statChoice != "height" or statChoice != "weight" or statChoice != "attack" or statChoice != "defence" or statChoice != "special attack" or statChoice != "special defence":
            statChoice = input("\n\nWhich stat do you want to use? (id, height, weight, attack, defence, special attack, or special defence?)\n")
            if statChoice == "id" or statChoice == "height" or statChoice == "weight" or statChoice == "attack" or statChoice == "defence" or statChoice == "special attack" or statChoice == "special defence":
                myStat = myPokemon[statChoice]
                rivalStat = rivalPokemon[statChoice]
                break
            else:
                continue


        if myStat > rivalStat:
            print_fast('\n{} lost 10HP!'.format(rivalPokemonName))
            rivalPokemonsHP -= 10
            print_fast("\nNow {} has {} remaining HP.".format(myPokemonName,myPokemonsHP))
            print_fast("\n{} has {} remaining HP.".format(rivalPokemonName,rivalPokemonsHP))
        elif myStat < rivalStat:
            print_fast('\n{} lost 10HP!'.format(myPokemonName))
            myPokemonsHP -= 10
            print_fast("\nNow {} has {} remaining HP.".format(myPokemonName,myPokemonsHP))
            print_fast("\n{} has {} remaining HP.".format(rivalPokemonName,rivalPokemonsHP))

#Prints text slower, and letter by letter(ish) to emulate video game text. Used mainly for Prof oak!
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.08)

#Prints text faster, and letter by letter(ish) to emulate video game text. Used for most characters.
def print_fast(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)

#If you choose to enter your house, the code is here
def yourHouse(rivalName, name, pokemon, pokes, win):
    print_fast("\n\nYOUR HOUSE!\n")
    time.sleep(2)
    print_slow("\nMother: Right. All boys leave home some day. It said so on TV. PROF.OAK, next door, is looking for you.")
    time.sleep(2)
    print("\nSNES: " + name + " is playing the SNES!")
    time.sleep(3)
    print("\n...Okay! It's time to go!")
    time.sleep(1)
    palletTown(rivalName, name, pokemon, pokes, win)

#If you choose to enter your rival's house, the code is here
def rivalHouse(rivalName, name, pokemon, pokes, win):
    print_fast("\n\n" + rivalName + "'s HOUSE!\n")
    time.sleep(2)
    print_fast("\n" + rivalName + "'s Sis: Hi " + name + "! " + rivalName + " is out at Grandpa's lab.\n")
    time.sleep(2)
    #Text is kinda unnatural, but we are working off the actual script for Red and Blue, so this is the best we have
    print("\nMAP: It's a big map! This is useful!")
    time.sleep(2)
    palletTown(rivalName, name, pokemon, pokes, win)

#If you choose to walk around the lab, the code is here
def researchLab(rivalName, name, pokemon, pokes, win):
    print_fast("\n\nRESEARCH LAB!\n")
    time.sleep(2)
    #No Prof Oak here. We removed the fetch quest in the games for simplicity and to make the game less long-winded.
    print_fast("\nSCIENTIST: I study POKEMON as PROF.OAK'S AIDE.")
    print_fast("\nSCIENTIST: PROF.OAK is the authority on POKEMON! Many POKEMON trainers hold him in high regard!\n")
    time.sleep(2)
    palletTown(rivalName, name, pokemon, pokes, win)

#This is the Pokemon Center for Viridian City
def pkmnCenter(rivalName, name, pokemon, pokes, win):
    print_fast("\n\nViridian City Pokemon Center!")
    time.sleep(1)
    print_fast("\nSTRANGER: There's a POKEMON CENTER in every town ahead. They don't charge any money either!")
    time.sleep(1)
    print_fast("\nSTRANGER: POKEMON CENTERS heal your tired, hurt or fainted POKEMON!")
    time.sleep(1)
    print_fast("\nSTRANGER: You can use that PC in the corner. The receptionist told me. So kind!")
    time.sleep(2)
    viridianCity(rivalName, name, pokemon, pokes, win)

#This is the Pokemon Mart for Viridian City. Need to add the money functionality
def pkmnMart(rivalName, name, pokemon, pokes, win):
    print_fast("\n\nViridian City Pokemon Mart!\n")
    time.sleep(1)
    print_fast("\nSTRANGER: This shop sells many ANTIDOTEs.")
    print_fast("\nSTRANGER: No! Potions are all sold out!")
    time.sleep(2)
    #User is expected to type either poke ball or antidote
    product = input("\n\nCLERK: How can I help you? We have POKE BALLs and ANTIDOTEs.\n")
    if product == "POKE BALL" or product == "poke ball" or product == "p" and pokes > 200:
        print_fast("\nCLERK: Right, P200! Thank you!")
    elif product == "ANTIDOTE" or product == "antidote" or product == "a" and pokes > 200:
        print_fast("\nCLERK: Right, P200! Thank you!")
    else:
        print_fast("\nClERK: Nevermind, you don't have enough.\n")
    viridianCity(rivalName, name, pokemon, pokes, win)

#This is for the pewter museum
def museum(rivalName, name, pokemon, pokes, win):
    print_fast("\n\nPewter City Museum!\n\n")
    enter = input("\nSCIENTIST: It's P50 for a child's ticket. Would you like to come in?")
    if enter == "yes" and pokes >= 50:
        print_slow("\nSCIENTIST: Right, P50! Thank you! Take plenty of time to look!")
        pokes = pokes - 50
    else:
        print_slow("\nSCIENTIST: Come again!")
        pewterCity(rivalName, name, pokemon, pokes, win)
    print("\nEXHIBIT A: AERODACTYL Fossil\nA primitive and rare POKEMON.")
    time.sleep(1)
    print("\nKABUTOPS Fossil\nA primitve and rare POKEMON.")
    time.sleep(1)
    print("\nEXHIBIT C: Meteorite that fell on MT.MOON. (MOON STONE?)")
    time.sleep(1)
    print("\nEXHIBIT D: SPACE SHUTTLE COLUMBIA")
    time.sleep(2)
    print_slow("\nSCIENTIST: We have a space exhibit now.")
    print_fast("\nSTRANGER: MOON STONE? What's so special about it?")
    time.sleep(2)
    print_fast("\nSTRANGER: July 20, 1969! The 1st lunar landing! I bought a color TV to watch it!")
    time.sleep(2)
    print_fast("\nSTRANGER: I want a PIKACHU! It's so cute! I asked my Daddy to catch me one!")
    print_fast("\nSTRANGER: Yeah, a PIKACHU soon, I promise!")
    time.sleep(2)
    pewterCity(rivalName, name, pokemon, pokes, win)

#Code for Brock's gym and the gym battles there. NUMBER EIGHT
def brockGym(rivalName, name, pokemon, pokes, win):
    print("\n\nPokemon Gym\n")
    print_fast("\nJR.TRAINER: Stop right there, kid! You're still light years from facing BROCK!")
    battle('JRTRAINER', name, 74, pokemon, pokes, win) #pokemon 074 is geodude
    brockGym()

def brockLeader(rivalName, name, pokemon, pokes, win):
    time.sleep(1)
    print_fast("\n\n\nBROCK: I'm BROCK! I'm PEWTER's GYM LEADER! I believe in rock hard defense and determination! That's why my POKEMON are all the rock-type!\nDo you still want to challenge me?\nFine then! Show me your best!")
    result = battle('BROCK', name, 95, pokemon, pokes, win) #pokemon 95 is Onix

#Code to navigate Pewter city's buildings. NUMBER SEVEN
def pewterCity(rivalName, name, pokemon, pokes, win):
    print("\n\nPewter City\n")
    time.sleep(1)
    print_fast("\nSTRANGER: You're a trainer right? BROCK's looking for new challengers!\nFollow me!")
    time.sleep(1)
    print_fast("\nIf you have the right stuff, go take on BROCK!")
    time.sleep(1)
    #direction variable created and while loop used so the user must pick one of these four places
    direction = ""
    while (direction != 1 or direction != 2 or direction != 3 or direction != 4):
        direction = input("\nWhere would you like to go now? Pick one:\nPokemon Center (1)\nPokemon Mart(2)\nMuseum (3)\nPokemon Gym(4)\n")
        if direction == "1":
            time.sleep(1)
            pokemonCenter(rivalName, name, pokemon, pokes, win)
        elif direction == "2":
            time.sleep(1)
            pokemonMart(rivalName, name, pokemon, pokes, win)
        elif direction == "3":
            time.sleep(1)
            museum(rivalName, name, pokemon, pokes, win)
        elif direction == "4":
            time.sleep(1)
            brockGym(rivalName, name, pokemon, pokes, win)
        else:
            continue

#This is the code for entering Viridian Forest, and a battle there. NUMBER SIX
def viridianForest(rivalName, name, pokemon, pokes, win):
    print("\n\nViridian Forest\n")
    time.sleep(2)
    print_fast("\nBUG CATCHER: Hey! You have POKEMON! Come on! Let's battle'em!")

    battle('BUG CATCHER', name, 10, pokemon, pokes, win) #pokemon 10 is caterpie

#This is for Pewter City's pokemon center
def pokemonCenter(rivalName, name, pokemon, pokes, win):
    print("\n\nPewter City Pokemon Center!\n")
    time.sleep(1)
    print_fast("\nJIGGLYPUFF: Puu pupuu!")
    time.sleep(2)
    print_slow("\nSTRANGER: Yawn! when JIGGLYPUFF sings, POKEMON get drowsy...\n\n\n...Me too...\n\nSnore...")
    time.sleep(2)
    print_fast("\nSTRANGER: What!? TEAM ROCKET is at MT.MOON? Huh? I'm on the phone! Scram!")
    time.sleep(2)
    pewterCity(rivalName, name, pokemon, pokes, win)

#This is for Pewter City's pokemon mart
def pokemonMart(rivalName, name, pokemon, pokes, win):
    print("\n\nPewter City Pokemon Mart!\n")
    time.sleep(1)
    print_fast("\nSTRANGER: Good things can happen if you raise POKEMON diligently, even the weak ones!")
    time.sleep(1)
    print_fast("\nSTRANGER: A shady, old man got me to buy this really weird fish POKEMON! It's totally weak and it cost P500!")
    time.sleep(2)
    print_fast("\nNIDORAN: Bowbow!")
    print_fast("\nSTRANGER: NIDORAN sit!\n\nOur POKEMON's an outsider, so it's hard to handle. An outsider if a POKEMON you get in a trade. It grows fast, but it may ignore an unskilled trainer in battle! If only we had some BADGEs...")
    time.sleep(2)
    product = input("\n\nCLERK: How can I help you? We have POTIONs and ANTIDOTEs.\n")
    if product == "POKE BALL" or product == "poke ball" and pokes > 200:
        print_fast("\nCLERK: Right, P200! Thank you!")
    elif product == "ANTIDOTE" and pokes > 200:
        print_fast("\nCLERK: Right, P200! Thank you!")
    else:
        print_fast("\nClERK: Nevermind, you don't have enough.\n")
    pewterCity(rivalName, name, pokemon, pokes, win)

#Code to navigate Viridian City. NUMBER FIVE
def viridianCity(rivalName, name, pokemon, pokes, win):
    print("\n\nViridian City\n")
    print_slow("\nThe Eternally Green Paradise\n")
    time.sleep(1)
    direction = ""
    while direction != "1" or direction != "2" or direction != "3":
        direction = input("\nWhere would you like to go now? Pick one:\nPokemon Center? (1)\nPokemon Mart? (2)\nViridian Forest?(3)\n")
        if direction == "1":
            pkmnCenter(rivalName, name, pokemon, pokes, win)
        elif direction == "2":
            pkmnMart(rivalName, name, pokemon, pokes, win)
        elif direction == "3":
            viridianForest(rivalName, name, pokemon, pokes, win)
        else:
            continue

#Code for route one and the battle there. NUMBER FOUR
def routeOne(rivalName, name, pokemon, pokes, win):
    print("\n\nOUTSIDE...\n")
    print_fast("\nRoute 1\n")

    print_fast("\n\nCOOLTRAINER QUINN: You there! Want to battle?")

    battle('Quinn', name, 120, pokemon, pokes, win) #pokemon 120 is Staryu

#Pick where to go in Pallet Town. NUMBER THREE
def palletTown(rivalName, name, pokemon, pokes, win):
    direction = ""
    while direction != "1" or direction != "2" or direction != "3" or direction != "4":
        direction = input("\nWhere would you like to go now? Pick one:\nYour house? (1)\n" + rivalName + "'s house? (2)\nResearch lab? (3)\nRoute One (4)\n")
        if direction == "1":
            yourHouse(rivalName, name, pokemon, pokes, win)
        elif direction == "2":
            rivalHouse(rivalName, name, pokemon, pokes, win)
        elif direction == "3":
            researchLab(rivalName, name, pokemon, pokes, win)
        elif direction =="4":
            routeOne(rivalName, name, pokemon, pokes, win)
        else:
            continue

#LABORATORY AND POKEMON SELECTION SCENE. NUMBER TWO
def laboratory(rivalName, name, pokes, win):
    time.sleep(2)
    print_fast("\n\n" + rivalName + ": Gramps! I'm fed up with waiting!")
    print_slow("\nOak: " + rivalName + "? Let me think... Oh, that's right. I told you to come! Just wait!")
    print_slow("\nHere, " + name + "! There are 3 POKEMON here! Haha! They are inside the POKE BALLS. When I was young, I was a serious POKEMON trainer. In my old age, I have only 3 left, but you can have one! Choose!")
    print_fast("\n" + rivalName + ": Hey! Gramps! What about me?")
    print_slow("\nOak: Be patient! " + name + ", you can have one too!")
    pokemon = input("\n\nDo you want the plant POKEMON, Bulbasaur?\nThe fire POKEMON, Charmander?\nOr the water POKEMON, Squirtle?\n")
    rivalPoke = 0
    while pokemon != 'Charmander' or pokemon != 'charmander' or pokemon != 'Bulbasaur' or pokemon != 'bulbasaur' or pokemon != 'squirtle' or pokemon != 'Squirtle':
        #Expand these for giant ASCII... don't... Maybe they are too big for the screen but it's hard to find smaller ones
        if pokemon == 'Charmander' or pokemon == 'charmander':
            print("\nYou have chosen Charmander!")
            print_fast('''              
                          _.--""`-..
                        ,'          `.
                      ,'          __  `.
                     /|          " __   |
                    , |           / |.   .
                    |,'          !_.'|   |
                  ,'             '   |   |
                 /              |`--'|   |
                |                `---'   |
                 .   ,                   |                       ,".
                  ._     '           _'  |                    , ' \ `
              `.. `.`-...___,...---""    |       __,.        ,`"   L,|
              |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    |
            -:..     `. `-..--_.,.<       `"      / `.        `-/ |   .
              `,         """"'     `.              ,'         |   |  ',,
                `.      '            '            /          '    |'. |/
                  `.   |              \       _,-'           |       ''
                    `._'               \   '"\                .      |
                       |                '     \                `._  ,'
                       |                 '     \                 .'|
                       |                 .      \                | |
                       |                 |       L              ,' |
                       `                 |       |             /   '
                        \                |       |           ,'   /
                      ,' \               |  _.._ ,-..___,..-'    ,'
                     /     .             .      `!             ,j'
                    /       `.          /        .           .'/
                   .          `.       /         |        _.'.'
                    `.          7`'---'          |------"'_.'
                   _,.`,_     _'                ,''-----"'
               _,-_    '       `.     .'      ,/
               -" /`.         _,'     | _  _  _.|
                ""--'---"""""'        `' '! |! /
                                        `" " -' 
                                ''')
            print_fast("\n" + rivalName + ": I'll take Squirtle then!")
            pokemon = 4
            rivalPoke = 7
            break
        elif (pokemon == 'Bulbasaur' or pokemon == 'bulbasaur'):
            print("\nYou have chosen Bulbasaur!")
            print_fast('''             
                                                    `;,;.;,;.;.'
                                                      ..:;:;::;: 
                                                ..--''' '' ' ' '''--.  
                                              /' .   .'        '.   .`
                                             | /    /            \   '.|
                                             | |   :             :    :|
                                           .'| |   :             :    :|
                                         ,: /\ \.._\ __..===..__/_../ /`.
                                        |'' |  :.|  `'          `'  |.'  ::.
                                        |   |  ''|    :'';          | ,  `''
                                        |.:  \/  | /'-.`'   ':'.-'\ |  \,   |
                                        | '  /  /  | / |...   | \ |  |  |';'|
                                         \ _ |:.|  |_\_|`.'   |_/_|  |.:| _ |
                                        /,.,.|' \__       . .      __/ '|.,.,
                                             | ':`.`----._____.---'.'   |
                                              \   `:"""-------'""' |   |
                                                ---------------------
                                ''')
            print_fast("\n" + rivalName + ": I'll take Charmander then!")
            pokemon = 1
            rivalPoke = 4
            break
        elif (pokemon == 'Squirtle' or pokemon == 'squirtle'):
            print("\nYou have chosen Squirtle!")
            # ascii squirtle
            print_fast('''               
                           _,........__
                        ,-'            "`-.
                      ,'                   `-.
                    ,'                        |
                  ,'                           .
                  .'\               ,"".       `
                 ._.'|             / |  `       |
                 |   |            `-.'  ||       `.
                 |   |            '-._,'||       | |
                 .`.,'             `..,'.'       , |`-.
                 l                       .'`.  _/  |   `.
                 `-.._'-   ,          _ _'   -" \  .     `
            `."""""'-.`-...,---------','         `. `....__.
            .'        `"-..___      __,'\          \  \     |
            \_ .          |   `""""'    `.           . \     |
              `.          |              `.          |  .     L
                `.        |`--...________.'.        j   |     |
                  `._    .'      |          `.     .|   ,     |
                     `--,\       .            `7""' |  ,      |
                        ` `      `            /     |  |      |    _,-'"""`-.
                         \ `.     .          /      |  '      |  ,'          `.
                          \  v.__  .        '       .   \    /| /              |
                           \/    `"""""""""`.       \   \  /.''                |
                            `        .        `._ ___,j.  `/ .-       ,---.     |
                            ,`-.      \         ."     `.  |/        j     `    |
                           /    `.     \       /         \ /         |     /    j
                          |       `-.   7-.._ .          |"          '         /
                          |          `./_    `|          |            .     _,'
                          `.           / `----|          |-............`---'
                            \          \      |          |
                           ,'           )     `.         |
                            7____,,..--'      /          |
                                              `---.__,--.'
                                ''')
            print_fast("\n" + rivalName + ": I'll take Bulbasaur then!")
            pokemon = 7
            rivalPoke = 1
            break
    print_slow("\n\nOak: If a wild POKEMON appears, your POKEMON can fight against it!")
    print_fast("\n" + rivalName + ": My POKEMON looks a lot stronger.")
    time.sleep(1)
    print_fast("\n" + rivalName + ": Wait " + name + "! Let's check out our POKEMON! Come on, I'll take you on!")

    result = battle(rivalName,name,rivalPoke,pokemon,pokes, win)

#This is the opening to the game. Input your name and your rival's name here. NUMBER ONE
def opening(pokes, win):
    #OPENING SCENE
    print_slow("\nHello there! Welcome to the world of POKEMON! My name is Oak! People call me the POKEMON PROF!")
    time.sleep(1)
    print_slow("\nThis world is inhabited by creatures called POKEMON! For some people, POKEMON are pets. Others use them for fights. Myself...\n I study POKEMON as a profession.")
    time.sleep(1)
    print_slow("\nFirst, what is your name")
    name = input("?\n")
    print_slow("Right! So your name is " + name + "!\n")
    print_slow("This is my grandson. He's been your rival since you were a baby.")
    print_slow("\n...Erm, what is his name again")
    rivalName = input("?\n")
    print_slow("That's right! His name is " + rivalName + "!\n")
    print_slow(name + "! Your very own POKEMON legend is about to unfold! A world of dreams and adventures with POKEMON awaits! Let's go!")
    laboratory(rivalName, name, pokes, win)


print('''               


                                  ,'|
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|

                    ''')
print("Pokemon Red & Blue")
opening(pokes, win)

import random  # for random functions
import time  # for time.sleep

print("Welcome to Pokemon Choose Your Own Adventure!")
time.sleep(1)
print("\nRULES:\n\nAt each choice either press 1,2,3, or 4.And most of all HAVE FUN")
time.sleep(1)

name = input("\nWhat is your name?")  # user inputs string for  name
print("\nHey", name, "good luck on your adventure trainer. Try to catch em' all")
time.sleep(2)

print("\nYou walk down the stairs to the kitchen and your mom greets you on your tenth birthday. The day you go out on your pokemon adventure.")
breakfast = int(input("\nYour mom gives you a big hug and asks you what you want for breakfast. Press 1 for cereal or Press 2 for a PB&J sandwich."))  # asks for an input to teach you how to play
if breakfast == 1:  # if the input is 1 then it runs this code
    print("\nYou eat your delicious bowl of cereal. Then you leave your house and head down the street\nto Professor Oak's lab to pick your first ever pokemon.")
elif breakfast == 2:  # if the input is 1 then it runs this code
    print("\nYou eat your delicious PB&J sandwich. Then you leave your house and head down the street\nto Professor Oak's lab to pick your first ever pokemon.")
time.sleep(3)

print("\nHi Professor Oak\nHey", name, "are you ready to pick your pokemon. Now each pokemon has their own strengths and\nweaknesses so make sure you choose wisely.")
time.sleep(4)

running = 0
while running == 0:  # creates a loop that only stops from a certain input in this case 4
    poke_info = int(input("\nPress 1 if you want to see Bulbasaur's stats\nPress 2 if you want to see Squirtle's stats\nPress 3 if you want to see Charmander's stats\nPress 4 to pick your pokemon"))
    if poke_info == 1:
        print("\nBulbasaur is a grass type pokemon he is strong against Ground, Rock, and Water.\nBut he is weak against Flying, Poison, Bug, Steel, Fire, Grass, and Dragon.")
    elif poke_info == 2:
        print("\nSquirtle is a water type pokemon he is strong against Ground, Rock, and Fire.\nBut he is weak against Water, Grass, and Dragon.")
    elif poke_info == 3:
        print("\nCharmander is a fire type pokemon he is strong against Bug, Steel, Grass, and Ice.\nBut he is weak against Rock, Fire, Water, and Dragon.")
    elif poke_info == 4:
        running = 1

time.sleep(2)
starter = int(input("\nWhat Pokemon do you want to choose?\n\nPress 1 for Bulbasaur\n\nPress 2 for Squirtle\n\nPress 3 for Charmander"))  # user inputs which pokemon is wanted  via integer
pokemon_1 = 0
if starter == 1:
    pokemon_1 = "Bulbasaur"
    print("\nCongratulations you picked", pokemon_1)
elif starter == 2:
    pokemon_1 = "Squirtle"
    print("\nCongratulations you picked", pokemon_1)
elif starter == 3:
    pokemon_1 = "Charmander"
    print("\nCongratulations you picked", pokemon_1)
time.sleep(1)
pokemon_holder = pokemon_1  # the variable pokemon_holder is used later

nickname = int(input("\nDo you want to give your pokemon a nickname? Press 1 for yes or 2 for no"))  # allows to change the str of the pokemon name that is why pokemon_holder is needed
if nickname == 1:
    pokemon_1 = input("\nWhat do you want your pokemon's nickname to be?")
    print("\nYour pokemon's name is", pokemon_1)
elif nickname == 2:
    pokemon_1 = pokemon_1

print("You leave professor Oak's Lab and travel to catch more pokemon and while going through a bush you find a wild Rattata.")
running = 0
while running == 0:  # another while loop
    rattata_catch = int(input("\nDo you want to see Rattata info press 1, if you want to try and catch Rattata press 2."))
    if rattata_catch == 1:
        print("\nRattata is a normal type pokemon he is strong against nothing.\nBut he is weak against fighting types.\nRattata can evolve into Raticate.")
    elif rattata_catch == 2:
        pokemon_2 = str("Rattata")
        print("\nCongratulations you caught", pokemon_2)
        running = 1
        nickname = int(input("\nDo you want to give your new pokemon a nickname? Press 1 for yes or 2 for no"))
        if nickname == 1:
            pokemon_2 = input("\nWhat do you want your pokemon's nickname to be?")
            print("\nYour pokemon's name is", pokemon_2)
        elif nickname == 2:
            pokemon_2 = pokemon_2

time.sleep(3)

print("\nYou just caught your second pokemon now are on your way further though Kanto and you stumble across another trainer, Brock!\nBrock challenges you to a battle using only your starter pokemon.")
time.sleep(2)
brock = 0
brock_move = 0
if pokemon_holder == str("Bulbasaur"):  # this is where pokemon_holder comes into play because it used to determine the pokemon of brock adn the move that he uses
    brock = str("Squirtle")
    print("\nBrock's pokemon is", brock, "which means", pokemon_1, "is super effective!")
elif pokemon_holder == str("Squirtle"):
    brock = str("Charmander")
    print("\nBrock's pokemon is", brock, "which means", pokemon_1, "is super effective!")
elif pokemon_holder == str("Charmander"):
    brock = str("Bulbasaur")
    print("\nBrock's pokemon is", brock, "which means", pokemon_1, "is super effective!")
if pokemon_holder == "Bulbasaur":  # determines the brocks pokemon move depending on the pokemon_holder
    brock_move = "Water Gun"
elif pokemon_holder == "Squirtle":
    brock_move = "Flamethrower"
elif pokemon_holder == "Charmander":
    brock_move = "Leaf Swarm"
print("\nBrock uses", brock_move, "and is not effective and deals 10 damage so ", pokemon_1, "now has 90 HP")

running = 0
counter = 0  # adds the ability to have a while loop the only repeats a couple times for the a  certain elif statement
move = 0
if pokemon_holder == "Bulbasaur":
    move = "Leaf Swarm"
elif pokemon_holder == "Squirtle":
    move = "Water Gun"
elif pokemon_holder == "Charmander":
    move = "Flamethrower"
while running == 0:
    attack = int(input("It is your turn to attack do you want to use " + move + " press 1 or Tackle press 2"))
    if attack == 1:
        print("\nIT IS SUPEREFFECTIVE and you have defeated", brock)
        running = 1
    elif attack == 2:
        print("\nTackle did 50 damage to", brock, )
        if counter == 1:
            print("\nCongratulations you defeated your first ever trainer.")
            running = 1
    counter += 1
time.sleep(1)
print("\nYou come to crossroads and you see a snake on the right but the path is more interesting or you can go left and not deal with the snake.")
time.sleep(5)
snake_choice = random.randint(1, 2)  # random function to determine path
if snake_choice == 1:
    print("\nYou decide to go right and the snake hisses at you so you pee yourself and go left.")
elif snake_choice == 2:
    print("\nYou decide to go left and then the snake dies and you wish you went that way but you didn't.")
time.sleep(5)

print("\nYou see a pokemon gym and and Good Life Fitness. You so see if you should get some gains or try your luck a gym.")
time.sleep(5)
gym_gains = random.randint(1, 2)  # random function to determine path
if gym_gains == 1:
    print("\nYou decide to go to the Good Life Fitness and buy a membership and get some gains.")
    time.sleep(2)
    print("\nYou then go to the pokemon gym now that you are the most buff pokemon trainer around.")
elif gym_gains == 2:
    print("\nYou decide to go to the pokemon gym and you continue to be the lankiest pokemon trainer around.")
time.sleep(5)

print("\nYou walk into the pokemon gym and it is all overgrown and you your first challenge, a maze.")
running = 0
while running == 0:
    maze = 0
    for i in range(0, 3):
        maze_input = int(input("\nDo you go left or right, press 1 for left or press 2 for right."))
        maze = maze_input + maze
    if maze == 4:  # the input consists of lefts and rights so 1's and 2's so depending on the directions you choose you can get out or not so for example two lefts and right is  the way out
        print("\nCongrats you made it out of the maze.")
        running = 1
    if maze == 5:
        print("\nCongrats you made it out of the maze.")
        running = 1
    if maze == 3:
        print("\nYou get lost you you retrace your steps and try again.")
    if maze == 6:
        print("\nYou get lost you you retrace your steps and try again.")

pokemon_3 = 0
if pokemon_holder == "Bulbasaur":
    pokemon_3 = "Psyduck"
elif pokemon_holder == "Squirtle":
    pokemon_3 = "Vulpix"
elif pokemon_holder == "Charmander":
    pokemon_3 = "Oddish"
pokemon_holder_3 = pokemon_3

print("After getting out of the maze you find a wild", pokemon_3, "which may help you in your fight against the gym leader.")
running = 0
while running == 0:
    pokemon_3_catch = int(input("\nDo you want to see " + pokemon_3 + " info press 1, if you want to try and catch " + pokemon_3 + " press 2."))
    if pokemon_3_catch == 1:
        if pokemon_3 == "Vulpix":
            print("\nVulpix is a fire type pokemon he is strong against Grass, Ice, Bug, and Steel.\nBut he is weak against Water, Ground, and Rock types.\nVulpix can evolve into Ninetales.")
        elif pokemon_3 == "Oddish":
            print("\nOddish is a grass and poison type pokemon he is strong against Grass, Fairy, Water, Ground, and Rock.\nBut he is weak against Ground, Psychic, Flying, Poison, Bug, Steel, Fire, Grass, and Dragon types.\nOddish can "
                  "evolve into Gloom and then Vileplume.")
        elif pokemon_3 == "Psyduck":
            print("\nPsyduck is a water type pokemon he is strong against Fire, Ground, and Rock.\nBut he is weak against Grass and Electric types.\nPsyduck can evolve into Goldduck.")
    elif pokemon_3_catch == 2:
        pokemon_3 = str(pokemon_3)
        print("\nCongratulations you caught", pokemon_3)
        running = 1
        nickname = int(input("\nDo you want to give your new pokemon a nickname? Press 1 for yes or 2 for no"))
        if nickname == 1:
            pokemon_3 = input("\nWhat do you want your pokemon's nickname to be?")
            print("\nYour pokemon's name is", pokemon_3)

print("\nYou have passed through the maze and now you come across the gym leader Misty!\nMisty is a water gym leader. She has two pokemon, PoliWrath and Tentacruel both water types")
time.sleep(2)
print("\nMisty uses PoliWrath and uses Hydropump and deals 100 damage so ", pokemon_3, "now has now fainted you must go revive them at the poke hospital.")
time.sleep(2)
print("\n", pokemon_3, "is really hurt so right as you get to the hospital Nurse Joy is waiting for you.")
coffee = int(input("\nYou go to the waiting room and you don't know what to do, press  1 to go get a coffee, press 2 to walk around the block."))
if coffee == 1:
    print("\nYou go and get some coffee from the shop in the hospital and when you come back", pokemon_3, "is all better and you go on your merry way.\nYou stumble across a shop that looks interesting and you go it and take a book off "
                                                                                                          "the shelf and a secret passage way opens and you enter. You find a secret labyrinth")
elif coffee == 2:
    print("\nWhile on your walk you stumble across a shop that looks interesting and you go it and take a book off the shelf and a secret passage way opens and you enter. You find a secret labyrinth")
time.sleep(5)
print("\nAs you walk down the stairs you trip and fall down the stairs and you look back up the stairs to see what you tripped on and it was a purple pokeball.\nYou go and pick it up and use  your pokedex to scan it and . . .",
      time.sleep(5), "\nbeep boop bop You Have Found A Master Ball, they have an increased chance o catch a legendary pokemon.")
time.sleep(3)
print("\nYou continue through the labyrinth and you see skeletons of different pokemon.")
time.sleep(4)
legend = int(input("You see three tunnels made of stone they say VALOR, MYSTIC, and INSTINCT. Which do you choose press 1 for valor, press 2 for mystic, and press 3 for instinct."))
print("\nYou continue down the tunnel and you enter a giant room and you hear a giant CAW and see a claw pop over the edge of the giant pit and you try to run and the door seals behind you.")
if legend == 1:
    print("\nYou see a giant fireball fly out of the pit and a bird flies out behind it. You pull out your pokedex and scan the pokemon and it is the legendary pokemon Moltres")
    legend_pokemon = "Moltres"
elif legend == 2:
    print("\nYou see a giant wave of water fly out of the pit and a bird flies out behind it. You pull out your pokedex and scan the pokemon and it is the legendary pokemon Articuno")
    legend_pokemon = "Articuno"
elif legend == 3:
    print("\nYou see a giant lighting bolt fly out of the pit and a bird flies out behind it. You pull out your pokedex and scan the pokemon and it is the legendary pokemon Zapdos")
    legend_pokemon = "Zapdos"
time.sleep(4)
running = 0
while running == 0:
    legend_catch = int(input("\nYou stare him in the eyes what do you do, press 1 to use a regular pokeball, press 2 to use your masterball but you only have one"))
    if legend_catch == 1:
        print("\n1")
        time.sleep(1)
        print("\n2")
        time.sleep(1)
        print("\n3")
        time.sleep(1)
        print("\nYour pokeball failed, you might want to try a masterball.")
        time.sleep(1)
    elif legend_catch == 2:
        print("\n1")
        time.sleep(1)
        print("\n2")
        time.sleep(1)
        print("\n3")
        time.sleep(1)
        running = 1
print("\nCongratulations you caught", legend_pokemon, "and you have completed the game feel free to play again")

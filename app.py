from pkg.functions import *


# TODO  error handling for bad inputs
# TODO  OPTIONAL - use some switch statements instead of if/else
# TODO  game balance - add character buffs when beating dungeons so that you likely need to beat Diablo last

def town(character):
    while True:
        if character.hp <= 0:
            print('You have died! Game over!')
            print('---------------------- \n')
            break
        elif not available_dungeons:
            print('Congratulations! You have defeated all the enemies and won the game!')
            break
        else:
            print('\n--------------------')
            print('You are in town')
            print('--------------------')
            print('1) Enter a dungeon')
            print('2) Chat with townsfolk')
            print('3) Drink Mystery Potion')
            print('4) Inspect your character')
            print('--------------------')
            choice = int(input('What would you like to do? '))
            print('--------------------')
            if choice == 1:
                dungeon = choose_dungeon()
                encounter(character, dungeon)
                # del available_dungeons[dungeon]
            elif choice == 2:
                chat_townsfolk()
            elif choice == 3:
                drink_potion(character)
            elif choice == 4:
                character.character_screen()
            else:
                print('INVALID CHOICE. TRY AGAIN.')


while True:
    # Game start
    print('\nWelcome to Tristram! Your goal is to vanquish all 3 bosses and save the town.')
    print('Choose your adventurer!\n')

    # Choose class
    hero = choose_class()

    # Display starting stats
    hero.character_screen()

    # Start adventure
    town(hero)

from pkg.functions import *

# TODO  OPTIONAL - use some switch statements instead of if/else
# TODO  game balance - add character buffs when beating dungeons so that you likely need to beat Diablo last
# TODO  FUTURE - add random loot when bosses get defeated, maybe add equipment, use SQL tables?


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

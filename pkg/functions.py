from pkg.classes import *
from pkg.townsfolk import *

import random
import time

available_dungeons = {
    'dungeon': Butcher(),
    'catacombs': SkeletonKing(),
    'hell': Diablo()
}

dungeon_codes = {
    'd': 'dungeon',
    'c': 'catacombs',
    'h': 'hell'
}


def short_sleep():
    time.sleep(2)


def long_sleep():
    time.sleep(3.5)


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
            choice = input('What would you like to do? ')
            print('--------------------')
            match choice:
                case '1':
                    dungeon = choose_dungeon()
                    encounter(character, dungeon)
                case '2':
                    chat_townsfolk()
                case '3':
                    drink_potion(character)
                case '4':
                    character.character_screen()
                case _:
                    print('INVALID CHOICE. TRY AGAIN.')


def choose_class():
    while True:
        print('1 = Warrior')
        print('2 = Sorcerer')
        print('3 = Rogue')
        choice = int(input('Choose your class: '))
        match choice:
            case 1:
                print('\nYou chose the Warrior\n')
                return Warrior()
            case 2:
                print('\nYou chose the Sorcerer\n')
                return Sorcerer()
            case 3:
                print('\nYou chose the Rogue\n')
                return Rogue()
            case _:
                print('Invalid choice. Try again. \n')


def chat_townsfolk():
    print('**** You Enter the Tavern and Speak to a Patron... ****')
    long_sleep()
    print(f'Patron says: {random.choice(townsfolk)}')
    long_sleep()


def drink_potion(character):
    print('**** YOU DRANK THE MYSTERY POTION ****')
    short_sleep()
    print('**** YOU BEGIN TO FEEL THE EFFECTS... ****')
    short_sleep()
    random_choice = round(random.random() * 100)
    if 0 <= random_choice <= 10:
        character.hp -= 80
        print('The potion is hurting your health.')
        short_sleep()
        print('You lost 80 HP.')
        short_sleep()
    elif 11 <= random_choice <= 35:
        character.hp += 20
        print('The potion is rejuvenating you.')
        short_sleep()
        print('You gained 20 HP.')
        short_sleep()
    elif 36 <= random_choice <= 65:
        character.max_damage += 20
        print('The potion is making you stronger!')
        short_sleep()
        print('Your maximum damage increased by 20.')
        short_sleep()
    elif 66 <= random_choice <= 89:
        print('The potion is making you weaker...')
        short_sleep()
        if character.min_damage <= 0:
            print('Your minimum damage is already zero.')
            short_sleep()
        else:
            character.min_damage -= 10
            if character.min_damage < 0:
                character.min_damage = 0
            print('Your minimum damage decreased by 10.')
            short_sleep()
    else:
        if character.critical_hit < .75:
            character.critical_hit += .2
            print('You feel lucky!')
            print('Your critical hit chance increased by 20%!')
        elif .75 <= character.critical_hit <= .95:
            character.critical_hit = .95
            print('You feel lucky!')
            print('Your critical hit chance increased by 20%!')
        else:
            print('Your critical hit chance is already maxed at 95%.')


def choose_dungeon():
    while True:
        print('\n **** AVAILABLE DUNGEONS **** ')
        print('--------------------')
        for key, value in dungeon_codes.items():
            print(f'{key}. {value}')
        print('--------------------')
        dungeon_choice = str(input('Choose a dungeon to explore: '))
        if dungeon_choice not in dungeon_codes:
            print('Invalid dungeon choice!')
        else:
            dungeon = available_dungeons[dungeon_codes[dungeon_choice]]
            return dungeon


def encounter(character, dungeon):
    boss = dungeon
    print('\n**** YOU EXPLORE THE DUNGEON ****\n')
    long_sleep()
    while True:
        print(f'\nYou have encountered {boss.name}!\n')
        short_sleep()
        print(f'1. Fight {boss.name}')
        print(f'2. Inspect {boss.name}')
        print(f'3. Inspect your character')
        print(f'4. Return to town')
        choice = input('\nWhat would you like to do? ')
        match choice:
            case '2':
                boss.boss_screen()
            case '3':
                character.character_screen()
            case '4':
                return ''
            case '1':
                print(f'\n**** You have engaged {boss.name}! ****\n')
                print('--------------------')
                battle(character, boss)
                return ''
            case _:
                print('Invalid choice!')


def battle(character, boss):
    while character.hp >= 0 and boss.hp >= 0:
        hero_hit(character, boss)
        boss_hit(character, boss)


def hero_hit(character, boss):
    critical_hit = (0 <= random.randint(1, 100) <= (character.critical_hit * 100))
    multiplier = 1.5 if critical_hit else 1.0
    if character.damage_type == boss.weakness:
        print('*** THE BOSS IS WEAK TO YOUR ATTACK ***')
        multiplier += .25
        short_sleep()
    character_hit = round((random.randint(character.min_damage, character.max_damage)) * multiplier)
    if critical_hit:
        print('*** CRITICAL HIT! ***')
    boss.hp -= character_hit
    print(f'You hit {boss.name} for {character_hit}!')
    print('--------------------')
    short_sleep()


def boss_hit(character, boss):
    if boss.hp <= 0:
        print(f'You have defeated {boss.name}!')
        available_dungeons.pop(boss.dungeon)
        dungeon_codes.pop(boss.dungeon[0])
        return ''
    critical_hit = (0 <= random.randint(1, 100) <= (boss.critical_hit * 100))
    multiplier = 1.5 if critical_hit else 1.0
    boss_hit = round((random.randint(boss.min_damage, boss.max_damage)) * multiplier)
    if critical_hit:
        print('*** CRITICAL HIT! ***')
    character.hp -= boss_hit
    print(f'{boss.name} hit you for {boss_hit}!')
    print('--------------------')
    short_sleep()
    if character.hp <= 0:
        print(f'{boss.name} has defeated you!')
        return ''
    else:
        print(f'You have {character.hp} HP left.')
        print(f'{boss.name} has {boss.hp} HP left.')
    print('--------------------')
    long_sleep()

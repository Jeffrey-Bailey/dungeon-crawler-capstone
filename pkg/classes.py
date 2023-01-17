class Entity:
    def __init__(self, name, hp, min_damage, max_damage, critical_hit):
        self.name = name
        self.hp = hp
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.critical_hit = critical_hit


class Character(Entity):
    def __init__(self, damage_type, name, hp, min_damage, max_damage, critical_hit):
        super().__init__(name, hp, min_damage, max_damage, critical_hit)
        self.damage_type = damage_type

    def character_screen(self):
        print('-----------------------------------')
        print(f'{self.name}')
        print(f'\nHP: {self.hp}')
        print(f'Damage: {self.min_damage} - {self.max_damage}')
        print(f'Damage Type: {self.damage_type}')
        print(f'Critical Hit Chance: {self.critical_hit * 100} %')
        print('-----------------------------------\n')


class Boss(Entity):
    def __init__(self, weakness, name, hp, min_damage, max_damage, critical_hit, dungeon):
        super().__init__(name, hp, min_damage, max_damage, critical_hit)
        self.weakness = weakness
        self.dungeon = dungeon

    def boss_screen(self):
        print('-----------------------------------')
        print(f'\n{self.name.upper()}')
        print(f'HP: {self.hp}')
        print(f'Damage: {self.min_damage} - {self.max_damage}')
        print(f'Critical Hit Chance: {self.critical_hit * 100} %')
        print('-----------------------------------\n')


class Warrior(Character):
    def __init__(self):
        super().__init__('slash', 'Warrior', 250, 40, 75, .20)


class Sorcerer(Character):
    def __init__(self):
        super().__init__('magic', 'Sorcerer', 150, 60, 85, .1)


class Rogue(Character):
    def __init__(self):
        super().__init__('pierce', 'Rogue', 200, 10, 105, .35)


class Butcher(Boss):
    def __init__(self):
        super().__init__('slash', 'BUTCHER DEMON', 200, 50, 75, .05, 'dungeon')


class SkeletonKing(Boss):
    def __init__(self):
        super().__init__('magic', 'SKELETON KING', 175, 25, 75, .30, 'catacombs')


class Diablo(Boss):
    def __init__(self):
        super().__init__('pierce', 'DIABLO', 350, 50, 95, .20, 'hell')

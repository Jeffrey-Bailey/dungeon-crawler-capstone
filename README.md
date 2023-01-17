# Dungeon_Crawler_Capstone

Introduction
•	This game recreates a game type from my childhood, “rogue-likes”, in which you traverse dungeons and battle bosses with very little explaining or help out of the gate.
2. Design and Implementation
•	In this game, you start off by choosing a character class. Each class has different hit point (HP), damage range, damage type. I created a parent class called Entity and then different sub-classes to handle the things that are the same between all characters and the things that are different. There are 3 bosses in the game, which also have HP, damage etc. and they are also subclass of the Entity parent class, but with some differences that are handled by the subclass. These all live in classes.py.
•	When you start the game (app.py), you choose a class from 3 available classes. Once you choose, you get shown the stats for that class so that you understand how much HP, damage and damage types you have. This creates an object from the chosen class which will be used throughout the game. From there you land in TOWN, where you have 4 options available to you:
o	Enter a dungeon
o	Chat with townfolk
o	Drink Mystery potion
o	Inspect your character

ENTER A DUNGEON
If you enter a dungeon, you then get to choose which dungeon, from 3. You then traverse the dungeon and encounter a boss, which you can:
•	Fight the boss
•	Inspect the boss
•	Inspect your character
•	Return to town
The idea here is to inspect the boss and compare it’s stats with yours and decide if you want to battle that boss or return to town and do something else. If you choose to fight the boss, it automatically battles for you. 

BATTLE
When you battle, you trade hits with the boss, each of you losing HP. The damage you deal is a calculation of a random number between your min and max damage values, plus extra damage (50% extra damage on top of your damage roll) if you get a critical hit and more bonus (25%) if you have the weakness to the specific boss. You can see the calcs etc. in the battle() in functions.py.
If you defeat the boss, you return to town and can do the same thing again, except the dungeon you defeated is now gone from the list. The point of the game is to defeat all 3 dungeons/bosses and win the game. If a boss defeats you, the game is over and starts again.

CHAT WITH TOWNSFOLK
This just gives you a random line of text from my townfolk.py. The idea is to give you some hints about the mechanics of the game. Kind of like an instruction manual of sorts. You return to town after.

DRINK MYSTERY POTION
This calls a function drink_potion(), which takes your character object and randomly rolls a number 1-100. There are a few different things that can happen based on the random roll, some things good, some things bad. For example, get extra critical hit chance permanently added to your character, or lose 20 HP. It is just a fun way to put some randomization on your character/chances.

INSPECT YOUR CHARACTER
This simply prints your stats from the object of your character so that you can see your damage/damage type/remaining HP at any time throughout the game.

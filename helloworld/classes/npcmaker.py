# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 16:20:20 2019

@author: Dima's_Monster
"""

import dice
from classes.npcdatabase import npcdatabase

npcdatabase = npcdatabase()

# spells, races, skills, chaos features, characters

# spell types: spirit, rune, sorcery,



class npcmaker:
    def __init__(self, database):
        self.database = npcdatabase.get("races")
        self.stats = {"str": 0, "dex": 0, "con": 0, "con": 0, "size": 0, "int": 0, "pow": 0, "cha": 0}
    # race and difficulty can be strings or lists of strings
    def create(self, race= "BROO"):
        self.stats["str"] = dice.roll(self.database[race]["STR"]+ "t")
        self.stats["dex"] = dice.roll(self.database[race]["DEX"]+ "t")
        self.stats["con"] = dice.roll(self.database[race]["CON"]+ "t")
        self.stats["size"] = dice.roll(self.database[race]["SIZE"]+ "t")
        self.stats["int"] = dice.roll(self.database[race]["INT"]+ "t")
        self.stats["pow"] = dice.roll(self.database[race]["POW"]+ "t")
        self.stats["cha"] = dice.roll(self.database[race]["CHA"]+ "t")
        return

    def outprint(self):
        print(self.stats)
        return

#npc_make = npcmaker(database)
#npc_make.outprint()
#npc_make.create()
#npc_make.outprint()

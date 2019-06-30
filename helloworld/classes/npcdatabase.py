# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 16:51:00 2019

@author: Dima's_Monster
"""

# spells, races, skills, chaos features

# spell types: spirit, rune, sorcery,

# race influences: stats

class npcdatabase:
    def __init__(self):
        self.skills = None
        self.races = None
        self.chaos_features = None
        self.spells = None
        self.initialize_database()

    def get(self, item):
        if item == 'skills':
            return self.skills
        elif item == 'races':
            return self.races
        elif item == 'spells':
            return self.spells
        elif item == 'chaos features':
            return self.chaos_features
        elif item == 'all':
            return self.races, self.skills, self.spells, self.chaos_features

    def initialize_database(self):
        self.races = {'BROO' : {'STR':'2D6+6','CON':'1D6+12','SIZE':'2D6+6','INT':'2D6+6','POW':'3D6','DEX':'3D6','CHA':'2D6'}}
        self.spells = {}
        self.skills = {}
        self.chaos_features = {}

#!/usr/bin/python
# -*- coding: utf-8 -*-

from fighter_game import Fighter, Weapon


class Fighter_manager:
    
    def __init__(self):
        self.fighter_list = [Fighter("Erik Zemmour", "Il aime pas les mohammed"), Fighter("Crackhead", "Il cuisine bien")]
        self.weapon_list = []

    def create_fighter(self):
        fighter = Fighter(str(input("Fighter name : ")), str(input("Description : ")))
        self.fighter_list.append(fighter)
        return fighter
        
    def create_weapon(self):
        weapon = Weapon(str(input("Weapon name : ")), input("Damage (be reasonable) : "), input("Number of ammo : "))
        self.weapon_list.append(weapon)
        return weapon
        
    def start_fight(self):
        """Creates all 4 fighters"""
        print("- Fighter 1 -")
        f1 = self.create_fighter()
        print("- Fighter 2 -")
        f2 = self.create_fighter()
        print("- Fighter 3 -")
        f3 = self.create_fighter()
        print("- Fighter 4 -")
        f4 = self.create_fighter()
        
        """Gives a random weapon to every fighter"""
        

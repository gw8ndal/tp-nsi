#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randrange, uniform

class Fighter:
    """Base class of a fighter"""
    def __init__(self, name, description):
        self.__name = name #__=attribut privé
        self.__description = description
        self.__agility = randrange(1,9)
        self.__health_points = 100
        self.__weapon = None

    def __repr__(self):
        return self.get_name()

    def get_name(self):     #Doctests, pour tester directement les méthodes
        """Return the name of the fighter
        >>> fighter_a = Fighter("Nicolas sarkozy", "Il aime pas les mohammed")
        >>> fighter_a.get_name()
        'Nicolas sarkozy'
        """
        return self.__name

    def get_description(self):
        """Return the description of the fighter
        >>> fighter_a = Fighter("Nicolas sarkozy", "Il aime pas les mohammed")
        >>> fighter_a.get_description()
        'Il aime pas les mohammed'
        """
        return self.__description

    def set_description(self, description):
        """Set the description of the fighter"""
        self.__description = description

    def get_agility(self):
        """Return the agility of the fighter"""
        return self.__agility

    def get_strength(self):
        """Return the strength of the fighter"""
        return 10 - self.get_agility()

    def get_health_points(self):
        """Return the health of the fighter"""
        return self.__health_points

    def get_weapon(self):
        """Return the weapon of the fighter"""
        return self.__weapon

    def punch(self, a_fighter):
        """
        Punch a Fighter
        return the health points of a Fighter
        """
        points = int(uniform(0.7,1.0)*10*self.get_strength()/a_fighter.get_agility())
        a_fighter.__health_points =   a_fighter.get_health_points() - points
        return a_fighter.__health_points

    def summary(self):
        """Return the summary of a fighter"""
        name = 'name : ' + self.get_name()
        description = 'description : ' + self.get_description()
        agility = 'agility : ' + str(self.get_agility())
        strength = 'strength : ' + str(self.get_strength())
        health_points = 'health_points : ' + str(self.get_health_points())
        summary = '\n'.join([name, description, agility, strength, health_points])
        if self.take_weapon():
            summary += self.take_weapon().summary()
        return summary

    def take_weapon(self, a_weapon):
        if self.__weapon != None:
            self.__weapon.set_owner(None)
        self.__weapon = a_weapon
        a_weapon.set_owner(self)
        return self.__weapon


class Weapon:
    """The base class of a weapon"""
    def __init__(self, name, damage, ammos):
        self.__name = name
        self.__damage = damage
        self.__ammos = ammos
        self.__owner = None

    def __repr__(self):
        return self.get_name()

    def get_name(self):
        """Returns the name of the weapon"""
        return self.__name

    def get_damage(self):
        """Returns the damage of the weapon"""
        return self.__damage

    def get_ammos(self):
        """Returns the ammo of the weapon"""
        return self.__ammos

    def get_owner(self):
        """Returns the owner of the weapon"""
        return self.__owner

    def set_owner(self, owner):
        """Returns the owner of the weapon"""
        self.__owner = owner

    def summary(self):
        """Return the summary of a weapon"""
        name = 'name : ' + self.get_name()
        damage = 'damage : ' + str(self.get_damage())
        ammos = 'ammo : ' + str(self.get_ammos())
        owner = 'owner : ' + str(self.get_owner())
        return '\n'.join([name, damage, ammos, owner])

    def shoot(self, a_fighter):
        """Shoot a fighter and return the fighter health points"""
        if self.get_ammos()>0:
            lostPoints = int(self.get_damage() / a_fighter.get_agility())
            lostPoints = int(lostPoints * uniform(0.5,1)) # some random added
            a_fighter.__health_points = a_fighter.get_health_points() - lostPoints
            self.__ammos -= 1 # remove one ammo
        return a_fighter.get_health_points()



machette = Weapon("machette haitienne", 13, 3)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

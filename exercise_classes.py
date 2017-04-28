#!/usr/bin/env python
"""
In this exercise we will create a number of classes and apply some elementary
object-oriented programming.

Implement the following classes describing some of the actors in an elementary
video game.

All actors have a property "strength". Strength is a number that can be
increased by x by calling the method "increase_strength(x)", resp. "strength" is
decreased by x by calling the method "decrease_strength(x)". If the strength drops
below zero, it should remain zero.

The property "is_alive" should start out True, and become False once strength
reaches zero. Contrary to popular opinion, Zombies and Vampires should
start out as alive.

All actors will contain the method "fight()". Actor x can start a fight with
Actor y by calling "x.fight(y)". The one with the highest strength wins,
the other dies. The winner is damaged however, and gets its strength decreased
by the strength of the opponent.

All actors have a "kills" property which increases by one when the actor wins a
fight.

Class Hero has an special property "magic". Hero's "strength" can increase only
if "magic" is above zero. x increase in "strength" causes x decrease in "magic".

Class Vampire will increase its property "strength" only if it survives after a
fight _it started itself_. The "strength" of Vampire will increase by x, where x
is half the "strength" of the opponent.

Class Zombie will increase its "strength" by x at the beginning of every fight
_it starts itself_, where x is a randomly generated number between 1 and 10.
"""


"""
First of all think about the inheritance hierarchy: what properties are shared by
what classes? We've provided you with the names of the classes that are required
to solve the problem, but it's up to you to implement them and lay out their
inheritance hierarchy.
"""


class Actor:
    """
    This is supposed to be the most general class, at the top of the hierarchy:
    everything that shared between all actors can be put here.
    """
    pass


class Hero:
    """
    Heroes start out with 100 strength and 50 magic.
    """
    pass


class Enemy:
    pass


class Zombie:
    """
    Zombies start out with 150 strength.
    Remember that Zombies increase their strength randomly at the beginning
    of each fight. How to generate a random number?
    """
    pass


class Vampire:
    """
    Vampires start out with 70 strength.
    Remember that when a Vampire wins a fight it starts, it obtains half of the
    strength of the enemy it has beaten.
    """
    pass


"""
From here on unit tests.
Do not modify this code!
"""


def test_hero_strength():
    hero = Hero()
    assert hero.strength == 100
    assert hero.magic == 50
    assert hero.is_alive

    hero.increase_strength(50)
    assert hero.strength == 150
    assert hero.is_alive

    assert hero.magic == 0

    hero.decrease_strength(149)
    assert hero.strength == 1
    assert hero.is_alive

    hero.decrease_strength(5)
    assert hero.strength == 0
    assert not hero.is_alive


def test_hero_fights_vs_vampires():
    hero = Hero()
    assert hero.strength == 100
    assert hero.kills == 0

    first_vampire = Vampire()
    assert first_vampire.strength == 70
    assert first_vampire.is_alive

    first_vampire.fight(hero)
    assert hero.strength == 30
    assert hero.is_alive
    assert hero.kills == 1
    assert not first_vampire.is_alive

    second_vampire = Vampire()
    second_vampire.fight(hero)

    assert hero.strength == 0
    assert not hero.is_alive
    assert hero.kills == 1
    assert second_vampire.is_alive
    assert second_vampire.strength == 85
    assert second_vampire.kills == 1


def test_hero_loses_against_zombie():
    hero = Hero()
    zombie = Zombie()
    assert zombie.strength == 150

    zombie.fight(hero)
    assert not hero.is_alive
    assert hero.kills == 0
    assert zombie.is_alive
    assert zombie.kills == 1
    assert zombie.strength > 50
    assert zombie.strength < 61


if __name__ == '__main__':
    from test_runner import run_tests
    run_tests()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Rucksack import Rucksack
from Item import Item


def provision(rucksack: Rucksack):
    """Fill the backpack as full as possible. It must contain one Weapon and one amunition.
    :param rucksack: The backpack to fill
    :returns: The filled backpack.
    """
    rucksack.pack(0, rucksack.get_item("Cola"))
    return rucksack


def setup_items(rucksack: Rucksack):
    """Create some items and add them to the Item registry.
    :param rucksack: The backpack to add the items to.
    :returns: A backpack that has the new items.
    """
    rucksack + Item("Cola",     1, "C")
    rucksack + Item("Munition", 1, "M")
    rucksack + Item("Pistole",  2, "P")
    rucksack + Item("Gewehr",   4, "G")
    rucksack + Item("Flasche",  2, "F")
    return rucksack

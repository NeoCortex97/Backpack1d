#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Backpack import Backpack
from Item import Item


def provision(backpack: Backpack):
    """Fill the backpack as full as possible. It must contain one Weapon and one amunition.
    :param backpack: The backpack to fill
    :returns: The filled backpack.
    """
    for i in range(len(backpack)):
        backpack.pack(i, "Coke")
    return backpack


def setup_items(backpack: Backpack):
    """Create some items and add them to the Item registry.
    :param backpack: The backpack to add the items to.
    :returns: A backpack that has the new items.
    """
    backpack + Item("Coke", 1, "C", 1000)
    backpack + Item("Ammo", 1, "A", 150)
    backpack + Item("Pistol", 2, "P")
    backpack + Item("Rifle", 4, "R")
    backpack + Item("Water bottle", 2, "B", 50)
    return backpack

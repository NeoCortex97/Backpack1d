#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Rucksack import Rucksack


def provision(rucksack: Rucksack):
    """Fill the backpack as full as possible. It must contain one Weapon and one amunition.
    :param rucksack: The backpack to fill
    :returns: The filled backpack.
    """
    rucksack.pack(0, rucksack.get_item("Cola"))
    return rucksack
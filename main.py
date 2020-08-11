#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Rucksack import Rucksack
from Item import Item
from Provision import provision


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


def main():
    r = Rucksack()
    r = setup_items(r)
    r = provision(r)
    print(r)


if __name__ == "__main__":
    main()

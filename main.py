#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Rucksack import Rucksack
from Item import Item


def setup_items(rucksack):
    rucksack + Item("Cola",     1, "C")
    rucksack + Item("Munition", 1, "M")
    rucksack + Item("Pistole",  2, "P")
    rucksack + Item("Gewehr",   4, "G")
    rucksack + Item("Flasche",  2, "F")
    return rucksack


def main():
    r = Rucksack()
    r = setup_items(r)
    r.pack(0, r.get_item("Cola"))
    print(r)


if __name__ == "__main__":
    main()

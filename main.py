#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Backpack import Backpack
from Provision import provision, setup_items


def main():
    backpack = Backpack()
    print("Story: You arrived at an old shelter that still seems tohave some usable supplies.")
    print("       After some looking around you find the following supplies that should be usable\n")
    backpack = setup_items(backpack)
    print(backpack)
    print("\n       You try to pack as much supplies as possible into your backpack, but you will at least need the following things:")
    print("       - At least 1 Weapon")
    print("       - At least 1 pack of Ammo")
    print("       - At least 1 bottle of clean water")
    print("       You should better fit as much stuff as possible!")
    print("       So you sit down, think about it and try some things:")
    print("#" * 79)
    backpack = provision(backpack)
    print("#" * 79)
    print("       You decide, that this is as perfect as it will get.")
    print("       Maybe you can have some rest, before you have to leave this place again.")
    print(backpack)


if __name__ == "__main__":
    main()

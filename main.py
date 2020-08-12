#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Backpack import Backpack
from Provision import provision, setup_items


def main():
    print("Story: You arrived at an old shelter that still seems tohave some usable supplies.")
    print("       After some looking around you find the following supplies that should be usable")
    backpack = Backpack()
    backpack = setup_items(backpack)
    print(backpack)
    backpack = provision(backpack)
    print(backpack)


if __name__ == "__main__":
    main()

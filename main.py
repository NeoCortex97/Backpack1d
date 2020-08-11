#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Rucksack import Rucksack
from Provision import provision, setup_items


def main():
    r = Rucksack()
    r = setup_items(r)
    r = provision(r)
    print(r)


if __name__ == "__main__":
    main()

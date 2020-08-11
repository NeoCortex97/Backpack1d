#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from Item import Item


class Rucksack:
    """Manages an One-dimensional inventory.
    """
    def __init__(self, length=10, blocks=2, items={}):
        """Initialises the Inventory with a size and a number of random blocks"""
        self.blocks = []
        self.array = [None for _ in range(length)]
        self.items = items
        if 0 not in items.keys():
            self.items[0] = Item("Blockade", 1, "#", blocks)
        for i in range(blocks):
            index = random.randint(0, length - 1)
            self.array[index] = 0
            self.blocks.append(index)

    def __len__(self):
        return len(self.array)

    def __str__(self):
        res = 'Symbol | Name                           | Size | Amount\n'
        res += "-------+--------------------------------+------+-------\n"
        res += '\n'.join([str(self.items[i]) for i in self.items.keys()]) + '\n\n'
        res += "|" + "".join([self.items[item].symbol if item is not None else " " for item in self.array]) + "|"
        return res

    def __add__(self, other):
        """Add an item to the item list it added to type item"""
        if type(other) == Item:
            self.items[len(self.items.keys())] = other

    def pack(self, start, typ):
        if start + self.items[typ].size >= len(self.array):
            print("Could not insert Item at {}, because it would stick out".format(start))
            return False
        for i in range(self.items[typ].size):
            if self.array[start + i] is not None:
                print("Could not insert Item at {}, becasue it would not fit in this space".format(start))
                return False
        else:
            for i in range(self.items[typ].size):
                self.array[start + i] = typ

    def get_item(self, name):
        for i in self.items.keys():
            if name == self.items[i].name:
                return i
        return None

    def is_free(self, pos):
        return self.array is None

    def fetch_item(self, name):
        if name in self.items.keys():
            return self.items[name]
        else:
            return None

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from Item import Item


class Rucksack:
    """
    Manages an One-dimensional inventory.
    The Inventory is internally represented as an Array.
    It is impossible to remove items from the inventory unless you take care of it yourself
    If you want to add items to the Item registry you can use the + operator.
    If you want to remove an item from the registry
    """
    def __init__(self, size: int = 10, blocks: int = 2):
        """
        Initialises the Inventory with a size and a number of random blocks
        :param size: size of the Inventory in slots. Defaults to 10
        :param blocks: Number of barriers to place randomly in the backpack. Defaults to 2
        :returns: Nothing
        """
        self.blocks = []
        self.array = [None for _ in range(size)]
        self.items = {}
        if 0 not in self.items.keys():
            self.items[0] = Item("Blockade", 1, "#", blocks)
        for i in range(blocks):
            index = random.randint(0, size - 1)
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

    def __sub__(self, other):
        if type(other) == str and other in [item.name for item in self.items]:
            self.items = {key:val for key, val in self.items.items() if val != other}

    def pack(self, start: int, typ: int):
        """
        Try to insert an item into the inventory.
        :param start: the index you want to insert the item at.
        :param typ: The internal id of the item you want to inset. can be obtained via get_item. This tho will likely
        be subject to refactoring sooner or later!
        :return: True if it was able to insert the item
        False if it was unable to insert the item.
        """
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

    def get_item(self, name: str):
        """
        This function spits out the internal id of an item
        :param name: The mane of the item you seek
        :return: The internal id of the item in the registry of this backpack
        :rtype: int
        """
        for i in self.items.keys():
            if name == self.items[i].name:
                return i
        return None

    def is_free(self, pos):
        """
        Check if a position in the inventory is occupied.
        :param pos: Position to test.
        :return: True if the position is empty.
        False if it is not.
        """
        return self.array[pos] is None

    def fetch_item(self, name):
        """
        Get an item object from the backpack
        :param name: Item name
        :return: The item object
        :rtype: Item
        """
        if name in self.items.keys():
            return self.items[name]
        else:
            return None

    def is_full(self):
        """
        Check if the inventory is already full
        :return: True if the inventory is full.
        False if it isn't.
        """
        return self.array.count(None) == 0

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from Item import Item


class Backpack:
    """
    Manages an One-dimensional inventory.
    The Inventory is internally represented as an Array.
    It is impossible to remove items from the inventory unless you take care of it yourself
    If you want to add items to the Item registry you can use the + operator.
    If you want to remove an item from the registry
    This class has a convinence attribute
    """
    items = {}

    def __init__(self, size: int = 10, blocks: int = 2):
        """
        Initialises the Inventory with a size and a number of random blocks
        :param size: size of the Inventory in slots. Defaults to 10
        :param blocks: Number of barriers to place randomly in the backpack. Defaults to 2
        :returns: Nothing
        """
        self.blocks = []
        self.array = [None for _ in range(size)]
        if 0 not in Backpack.items.keys():
            Backpack.items[0] = Item("Blockade", 1, "#", blocks)
        for i in range(blocks):
            index = int(random.randint(0, size - 1))
            self.array[index] = 0
            self.blocks.append(index)

    def __len__(self):
        return len(self.array)

    def __str__(self):
        """
        :return: A string containing a list all items that could be packed into the backpack and the current state of the backpack.
        :rtype: str
        """
        res = 'Symbol | Name                           | Size | Amount\n'
        res += "-------+--------------------------------+------+-------\n"
        res += '\n'.join([str(Backpack.items[i]) for i in Backpack.items.keys()]) + '\n\n'
        res += "Backpack: |" + "".join([Backpack.items[item].symbol if item is not None else " " for item in self.array]) + "|"
        return res

    def __add__(self, other):
        """
        Add an item to the item list it added to type item
        """
        if type(other) == Item:
            Backpack.items[len(Backpack.items.keys())] = other

    def __sub__(self, other):
        if type(other) == str and other in [item.name for item in Backpack.items]:
            Backpack.items = {key:val for key, val in Backpack.items.items() if val != other}

    def pack(self, start: int, name: str):
        """
        Try to insert an item into the inventory.
        :param start: the index you want to insert the item at.
        :param name: The name of the item you want to inset.
        :return: True if it was able to insert the item
        False if it was unable to insert the item.
        :rtype: bool
        """
        typ = self.get_item(name)
        if start + Backpack.items[typ].size >= len(self.array):
            print("Could not insert Item at {}, because it would stick out".format(start))
            return False
        for i in range(Backpack.items[typ].size):
            if self.array[start + i] is not None:
                print("Could not insert Item at {}, becasue it would not fit in this space".format(start))
                return False
        else:
            Backpack.items[typ].amount -= 1
            for i in range(Backpack.items[typ].size):
                self.array[start + i] = typ

    def get_item(self, name: str):
        """
        This function spits out the internal id of an item
        :param name: The mane of the item you seek
        :return: The internal id of the item in the registry of this backpack
        :rtype: int
        """
        for i in Backpack.items.keys():
            if name == Backpack.items[i].name:
                return i
        return None

    def is_free(self, pos: int):
        """
        Check if a position in the inventory is occupied.
        :param pos: Position to test.
        :return: True if the position is empty.
        False if it is not.
        :rtype: bool
        """
        return self.array[pos] is None

    def fetch_item(self, name: str):
        """
        Get an item object from the backpack
        :param name: Item name
        :return: The item object
        :rtype: Item
        """
        key = self.get_item(name)
        if key in Backpack.items.keys():
            return Backpack.items[key]
        else:
            return None

    def is_full(self):
        """
        Check if the inventory is already full
        :return: True if the inventory is full.
        False if it isn't.
        :rtype: bool
        """
        return self.array.count(None) == 0

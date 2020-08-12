#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Item:
    """
    This class holds Data of an item.
    """
    def __init__(self, name: str, size: int, symbol: str, amount: int = 1):
        """
        Construct a new item.
        :param name: The name of the new item.
        :param size: The room that is taken up by the item
        :param symbol: A Character that will be used as a symbol in the pretty print.
        :param amount: The number of items that exist of this type. This defaults to one
        """
        self.name = name
        self.size = size
        self.symbol = symbol
        self.amount = amount

    def __str__(self):
        return "{:6} | {:30} | {:4} | {:5}".format(self.symbol, self.name, self.size, self.amount)

    def __bool__(self):
        return self.amount > 0
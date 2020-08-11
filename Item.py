#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Item:
    def __init__(self, name, size, symbol, amount=1):
        self.name = name
        self.size = size
        self.symbol = symbol
        self.amount = amount

    def __str__(self):
        return "{:6} | {:30} | {:4} | {:5}".format(self.symbol, self.name, self.size, self.amount)
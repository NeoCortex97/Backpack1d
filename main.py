#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Backpack import Backpack
from Provision import provision, setup_items


def main():
    backpack = Backpack()
    backpack = setup_items(backpack)
    backpack = provision(backpack)
    print(backpack)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
responds with a random quote
"""
import random
import time

filename = "quotes.txt"

def citat():
    """
    Citat
    """
    with open(filename) as filehandle:
        content = filehandle.read().splitlines()
    print("\n" + random.choice(content))
    time.sleep(3)

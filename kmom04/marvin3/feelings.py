#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
feelings
"""

import random
import time
import datetime

def respond_feeling():
    """
    How does The Dark Emporers feel today
    """
    filename = open("feelings.txt")
    line = filename.readline()
    moods = ["happy", "sad", "angry", "pissed off", "frustrated with you", "tired", "emotional"]
    smileys = [";)", ":D", ":|", ":P", ":/"]
    mood = random.choice(moods)
    smiley = random.choice(smileys)
    today = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    num = random.randrange(1, 1000)
    flt = round(random.uniform(1, 100), 3)

    print("\n" + line.format(today=today, num=num, flt=flt, mood=mood, smiley=smiley))
    time.sleep(3)

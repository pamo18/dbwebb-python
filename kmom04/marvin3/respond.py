#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
responses
"""

import random

hello = ['Hello to you too! ',
         'Its really nice that you care. ',
         'It was a long time ago anyone cared about me ',
         'Hi, looks like its going to rain today.']

lunchQuote = ['ska vi ta %s?',
              'ska vi dra ned till %s?',
              'jag tänkte käka på %s, ska du med?',
              'På %s är det mysigt, ska vi ta där?']

lunchBTH = ['thairestaurangen vid korsningen',
            'det är lite mysigt i fiket jämte demolabbet',
            'Indiska',
            'Pappa curry',
            'boden uppe på parkeringen',
            'Bergåsa kebab',
            'Pasterian',
            'Villa Oscar',
            'Eat here',
            'Bistro J']

lunchstan = ['Olles krovbar',
             'Lila thai stället',
             'donken',
             'tex mex stället vid subway',
             'Subway',
             'Nya peking',
             'kebab house',
             'Royal thai',
             'thai stället vid hemmakväll',
             'Gelato',
             'Indian garden',
             'Sumo sushi',
             'Pasterian i stan',
             'Biobaren',
             'Michelangelo']

lunchLidkoping = ['pastavagnen på torget',
                  'Freds',
                  'mcDonalds',
                  'subway',
                  'kinabuffé på Cats',
                  'valentino',
                  'lotterilådan',
                  'casablance',
                  'det där stället i gallerian',
                  'infinity',
                  'östervärn',
                  'argentina',
                  'T4']

def respond_hello():
    """
    responds user
    """
    print("\n" + random.choice(hello))

def respond_lunch(where):
    """
    Generates where to eat either in centrum or around bth (or Lidköping)
    """
    quote = lunchQuote[random.randint(0, len(lunchQuote) - 1)]
    msg = ''
    if where.lower() == 'stan':
        msg = quote % lunchstan[random.randint(0, len(lunchstan) -1)]
    elif where.lower() == 'lidköping':
        index = random.randint(0, len(lunchLidkoping) - 1)
        msg = quote % lunchLidkoping[index]
    else:
        msg = quote % lunchBTH[random.randint(0, len(lunchBTH)-1)]

    print(msg)

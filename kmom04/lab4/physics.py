#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Physics"""

import math

def free_fall(time, initial_speed=0, gravity=9.82):
    """
    freefall
    """
    speed = initial_speed + gravity * time
    return speed

def kinetic_energy(m, v):
    """
    kinetic energy
    """
    ke = 0.5 * m * v**2
    return ke

def height(time, m, g=9.82):
    """
    height calc
    """
    ke = kinetic_energy(m, free_fall(time))
    calc_height = ke / (m * g)
    return calc_height

def gravitational_pull(m1, m2, r):
    """
    gravitational pull
    """
    m1 = m1 * math.pow(10, 24)
    G = 6.674 * math.pow(10, -11)
    force = (G * m1 * m2) / r**2
    return force

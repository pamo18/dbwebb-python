#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Energy Calculation
"""

import energy_calculation as ec

emil_time = 2.5 / 60
emil_energy = ec.calculate_energy(emil_time)
emil_cost = ec.calculate_cost(emil_energy)

emil_string = "Emil använder {energy:.4f} kWh och detta kostar {cost:.4f} kr".format(
    energy=emil_energy,
    cost=emil_cost
)
print(emil_string)
print("name: " + __name__)

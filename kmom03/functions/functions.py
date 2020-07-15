#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions"""

def say_hello():
    """Says hello"""
    print("Hello")

print("Simon says hello")
say_hello()

def calculate_energy1(time_in_microwave, name, effect=800):
    """
    Calculates the energy consumption i kWh
    And prints the consumption together with the name
    """
    energy = effect * time_in_microwave / 1000
    print(name + " använder " + str(energy) + " kWh")

emil_time = 2.5 / 60
calculate_energy1(emil_time, "Emil")

andreas_time = 3.5 / 60
calculate_energy1(andreas_time, "Andreas")

kenneth_and_mikael_time = 0.5 / 60
calculate_energy1(kenneth_and_mikael_time, "Mikael", 600)
calculate_energy1(kenneth_and_mikael_time, "Kenneth", 600)

def calculate_energy2(time_in_microwave, effect=800):
    """
    Calculates the energy consumption i kWh
    Resturns the consumption
    """
    energy = effect * time_in_microwave / 1000
    return energy

emil_time = 2.5 / 60
emil_energy = calculate_energy2(emil_time)

def calculate_energy(time_in_microwave, effect=800):
    """
    Calculates the energy consumption i kWh
    Returns the consumption
    """
    energy = effect * time_in_microwave / 1000
    return energy

def calculate_cost(energy, price_per_kwh=78.04):
    """
    Calculates the cost for a given energy consumption
    Returns the cost in kr
    """
    cost = energy * price_per_kwh / 100
    return cost

emil_time = 2.5 / 60
emil_energy = calculate_energy(emil_time)
emil_cost = calculate_cost(emil_energy)

print("Emil använder " + str(emil_energy) + " kWh och detta kostar " + str(emil_cost) + " kr")

emil_time = 2.5 / 60
emil_energy = calculate_energy(emil_time)
emil_cost = calculate_cost(emil_energy)

nice_string = "Emil använder {energy} kWh och detta kostar {cost} kr".format(
    energy=emil_energy,
    cost=emil_cost
)

emil_time = 2.5 / 60
emil_energy = calculate_energy(emil_time)
emil_cost = calculate_cost(emil_energy)

nice_string = "Emil använder {energy:.4f} kWh och detta kostar {cost:.4f} kr".format(
    energy=emil_energy,
    cost=emil_cost
)

print(nice_string)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dictioanries
"""
from operator import itemgetter

warehouse = {
    "kottfars" : 20,
    "gradde" : 80,
    "krossade tomater": 33,
    "gul lok" : 42
}
print(warehouse["krossade tomater"])
warehouse["krossade tomater"] = 58
warehouse["rod lok"] = 7
#adds new item
print(warehouse)

for key, value in warehouse.items():
    print(key, value)

#items = key value

for key in sorted(warehouse.keys()):
    print(key, warehouse[key])

for key, value in sorted(warehouse.items(), key=itemgetter(1), reverse=True):
    print(key, value)

warehouse_deluxe = {
    "kottfars" : {"stock" : 20, "price" : 50, "ids" : (1234, "K14")},
    "gradde" : {"stock" : 80, "price" : 20, "ids" : (3141, "L12")},
    "krossade tomater": {"stock" : 33, "price" : 10, "ids" : (4224, "E13")},
    "gul lok" : {"stock" : 42, "price" : 5, "ids" : (2742, "D02")}
}
for key in sorted(warehouse_deluxe.keys()):
    print(key, warehouse_deluxe[key]["price"])

warehouse_deluxe["röd lok"] = {}
warehouse_deluxe["röd lok"]["stock"] = 7
warehouse_deluxe["röd lok"]["price"] = 9
warehouse_deluxe["röd lok"]["ids"] = (6314, "D04")

for key in sorted(warehouse_deluxe.keys()):
    print("{product} cost {price} and have {stock} in stock. The barcode {barcode} and stock id {stock_id}.".format(
        product=key,
        price=warehouse_deluxe[key]["price"],
        stock=warehouse_deluxe[key]["stock"],
        barcode=warehouse_deluxe[key]["ids"][0],
        stock_id=warehouse_deluxe[key]["ids"][1]
    ))

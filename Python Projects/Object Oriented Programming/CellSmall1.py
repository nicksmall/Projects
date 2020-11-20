#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:28:19 2020

@author: nicholassmall
"""

import cellSMALL

def main():
    manufacturer = input("Enter the manufacturer: ")
    model = input("Enter the model number: ")
    retail_price = float(input("Enter the retail price: "))

    cellphone = cellSMALL.cellphone()
    cellphone.set_manufact(manufacturer)
    cellphone.set_model(model)
    cellphone.set_retail_price(retail_price)

    print("Here is the data that you entered:")
    print("Manufacturer: {}".format(cellphone.get_manufact()))
    print("Model Number: {}".format(cellphone.get_model()))
    print("Retail Price: {}".format(cellphone.get_retail_price()))

if __name__ == "__main__":
    main()
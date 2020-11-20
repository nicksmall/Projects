#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:26:36 2020

@author: nicholassmall
"""

class cellphone:
    def __init__(self):
        self.__manufact = ""
        self.__model = ""
        self.__retail_price = 1.0

    def set_manufact(self, manufact):
        self.__manufact = manufact

    def set_model(self, model):
        self.__model = model
    
    def set_retail_price(self, price):
        self.__retail_price = price
    
    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model
    
    def get_retail_price(self):
        return self.__retail_price
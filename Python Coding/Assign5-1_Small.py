#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 12:55:03 2020

@author: nicholassmall
"""

def main():
    numbers = open('numbers.txt', 'r')
    data = numbers.read()
    numbers.close()
    print(data)
    
main()
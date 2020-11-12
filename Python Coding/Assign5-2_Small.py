#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 13:59:51 2020

@author: nicholassmall
"""

LIMIT = 5

def main():
    test = str(input('Enter the name of the file: '))
    read_file = open(test, 'r')
    READLINES = 0
    
    for data in read_file:                  
        if READLINES < LIMIT:         
            print(data, end="")          
            READLINES += 1
        else:                            
            break       
    read_file.close()
    
main()
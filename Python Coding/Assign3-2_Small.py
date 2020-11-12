#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 19:15:51 2020

@author: nicholassmall
"""

RATE_PROPERTY_TAX = .72
ASSESSED_PERCENTAGE = .60

#Variables assigned for constants rate of property tax and assessed percentage

def main():
    property_value = float(input('Enter the actual value: $'))
    assessed_value = property_value * ASSESSED_PERCENTAGE
    property_tax = (assessed_value / 100) * RATE_PROPERTY_TAX
    showPropertyTax(assessed_value, property_tax)
    
#main function is defined with property value requesting an input
#assigned to the function showpropertytax
    
def showPropertyTax(value,tax):
    print('Assessed value: $', format(value, ',.2f'))
    print('Property tax: $', format(tax, ',.2f'))
    
#showpropertytax function assigned and named value/tax
#print displays the assessed value and property tax
    
main()
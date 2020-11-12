#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:39:28 2020

@author: nicholassmall
"""

def main():

    total_sales = 0.0
    sales = 0.0
    daily_sales = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday', 'Saturday']
    days = len(week_days)
#main function contains initialized variables and 2 lists for daily sales and week days.

    for sales in range(days):

        print("Enter the sales for", week_days[sales],": ", end = "")
        daily_sales[sales] = float(input())
        daily_sales.append(daily_sales)
        total_sales += daily_sales[sales]
    print("Total sales for the week: $", format(total_sales, '.2f'))

#Request user input and loops it through daily sales/week days. And finally displaying the total sales from daily sales list.

main()
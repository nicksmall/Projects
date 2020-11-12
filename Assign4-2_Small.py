#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 00:29:10 2020

@author: nicholassmall
"""

def main():
    
    Rooms = {'ISQS 5347': 'BA 289','ISQS 6337': 'BA 015','ISQS 6349': 'BA 287','ISQS 6348': 'BA 021', }
    Instructors = {'ISQS 5347': 'Zadeh','ISQS 6337': 'Song','ISQS 6349': 'Kim','ISQS 6348': 'Benjamin', }
    Times = {'ISQS 5347': '9:00 a.m','ISQS 6337': '2:00 p.m','ISQS 6349': '9:00 a.m','ISQS 6348': '2:00 p.m', }
    Course = input("Enter a course number: ")
    display_course_info(Rooms, Instructors, Times, Course)
    
# Main function containing Dictionaries and requesting input from user  
    
def display_course_info(A, B, C, D): 
    
    if (D == 'ISQS 5347'):
        print("The details for course", D, "are:")
        print("Room:", A.get(D))
        print("Instructor: ", B.get(D))
        print("Time: ", C.get(D))
    elif (D == 'ISQS 6337'):
        print("The details for course", D, "are:")
        print("Room:", A.get(D))
        print("Instructor: ", B.get(D))
        print("Time: ", C.get(D))
    elif (D == 'ISQS 6349'):
        print("The details for course", D, "are:")
        print("Room:", A.get(D))
        print("Instructor: ", B.get(D))
        print("Time: ", C.get(D))
    elif (D == 'ISQS 6348'):
        print("The details for course", D, "are:")
        print("Room:", A.get(D))
        print("Instructor: ", B.get(D))
        print("Time: ", C.get(D))
    else:
        print(D, "does not exist in the dictionary.")
        print("Please try a different course from the following list:")
        print(list(A.keys()))
        
    
# Display course info function contain if statements that provide course info or help the user find info in the dictionary
    
main()
#!/usr/bin/env python

# -*- coding: utf-8 -*-

print "Welcome! With this program you can convert kilometers into miles."

while True:
    kilometers = int(raw_input("Enter number of kilometers: "))
    calculation = kilometers*0.621371
    print calculation

    answer = raw_input("Do you want to do another calculation?: ")

    if answer.lower () != "yes":
        print "Thank you for using our calculator!"
        break
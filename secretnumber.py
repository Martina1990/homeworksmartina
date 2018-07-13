#!/usr/bin/env python

# -*- coding: utf-8 -*-



secret = 9

guess = int(raw_input("Guess the secret number:"))

if secret == guess:

    print "You won!"

else:

    print "You lost!"
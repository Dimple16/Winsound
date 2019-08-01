# -*- coding: utf-8 -*-
"""
Created on Thu May 10 06:31:27 2018

@author: DEV
"""

import winsound

#The winsound module provides access to the basic sound-playing machinery provided by Windows platforms. It includes functions and several constants

print("Binary Representation of sound")

print("Enter the duration of each note (in ms)?")
print("e.g. 200")
rate = int(input(">"))

print("Enter a 4-bit binary note")
print("Or more than one note separated by spaces")

"""

print("Notes:")
print("0000 = no sound")
print("0001 = Low C")
print("0010 = D")
print("0011 = E")
print("0100 = F")
print("0101 = G")
print("0110 = A")
print("0111 = B")
print("1000 = High C")

print("0101 0101 0101 0010 0011 0011 0010 0000 0111 0111 0110 0110 0101")
"""
soundBinary = input(">")


print("e.g: ")
for note in soundBinary.split():

    if note == "A":          #rest
        freq = 392
    elif note == "B":        #low c
        freq = 220
    elif note == "C":        #d
        freq = 38
    elif note == "D":        #e
        freq = 124
        
    elif note == "E":        #f
        freq = 74
    elif note == "F":        #g
        freq = 784
    elif note == "G":        #a
        freq = 165
    elif note == "H":        #b90
        freq = 62
    elif note == "I":        #high c
        freq =110
    elif note == "J":
        freq= 1000
        
    winsound.Beep(freq, rate)
    
    #Beep the PC’s speaker. The frequency parameter specifies frequency, in hertz, of the sound, and must be in the range 37 through 32,767. The duration parameter specifies the number of milliseconds the sound should last. If the system is not able to beep the speaker, RuntimeError is raised.
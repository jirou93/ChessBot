# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 18:14:49 2018

@author: p.castro.sampol
"""

class Caballo:
    
    #t = 0 --> tablero (1x128)
    #t = 1 --> tablero (8x8)
    #x--> row in the tablero (0-7)
    #y--> column in the tablero (0-7)
    def __init__(self, t, x, y):
        self.t = t
        if t  == 0:
            self.position = x*16 + y
        else :
            self.position = x
    
    
    def posibleMoves(self):
        positions = []
        
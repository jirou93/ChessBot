# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 18:14:49 2018

@author: p.castro.sampol
"""

class Caballo:
    
    #t = 0 --> tablero (1x128)
    #t = 1 --> tablero (8x8)
    #if t== 0 x = posicion
    #else 
    #   x--> row in the tablero (0-7)
    #   y--> column in the tablero (0-7)
    def __init__(self, t, x, y):
        self.t = t
        if t  == 0 :
            self.position = x*16 + y
        else :
            self.position = x
    
    # return positions in tablero (1x128)
    def posibleMoves(self):
        positions = []
        positions.append(self.position + 31)
        positions.append(self.position + 33)
        positions.append(self.position + 14)
        positions.append(self.position + 18)
        positions.append(self.position - 14)
        positions.append(self.position - 18)
        positions.append(self.position - 31)
        positions.append(self.position - 33)
        return positions
        
        
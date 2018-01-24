# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 18:43:37 2018

@author: p.castro.sampol
"""

class Alfil:
    
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
    
    def posibleMoves(self):
        positions = []
        p = self.position + 16
        i = 1
        while p < 127 :
            positions.append(p + i)
            positions.append(p-i)
            p = p +16
            i = i + 1
        p = self.position - 16
        i = 1
        while p > 0 :
            positions.append(p + i)
            positions.append(p-i)
            i = i + 1
            p = p-16
        return positions
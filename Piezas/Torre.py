# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 09:15:06 2018

@author: p.castro.sampol
"""

class Torre:
    
    #t = 0 --> tablero (1x128)
    #t = 1 --> tablero (8x8)
    #if t== 0 x = posicion
    #else 
    #   x--> row in the tablero (0-7)
    #   y--> column in the tablero (0-7)
    def __init__(self, t, x ,y):
        self.t = t
        if t  == 0 :
            self.position = x*16 + y
        else :
            self.position = x
            
    # return positions in tablero (1x128)
    def posibleMoves(self):
        positions = []
        x = 1
        while x < 8:
            positions.append(self.position + x)
            positions.append(self.position - x)
            aux = self.position + x*16
            if (aux < 128) :
                positions.append(aux)
            aux = self.position - x*16
            if (aux > 0) :
                positions.append(aux)    
            x = x+1
        return positions
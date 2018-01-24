# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 10:08:43 2018

@author: p.castro.sampol
"""

class Dama:
    
    #t = 0 --> tablero (1x128)
    #t = 1 --> tablero (8x8)
    #if t== 0 x = posicion
    #else 
    #   x--> row in the tablero (0-7)
    #   y--> column in the tablero (0-7)
    #piezas --> position of all pieces in format (1x128)
    def __init__(self, t, x ,y , piezas):
        self.piezas = piezas
        self.DA = 1 #Represents the down-left Diagonal: 0->obstacles 1->no obstacle
        self.DB = 1 #Represents the down-rigth Diagonal
        self.DC = 1 #Represents the up-left Diagonal
        self.DD = 1 #Represents the up-rigth Diagonal
        self.VA = 1 #Represents the down Vertical
        self.VB = 1 #Represents the up Vertical
        self.HA = 1 #Represents the left Horitzontal
        self.HB = 1 #Represents the rigth Horitzontal
        self.moves = [] #Represents the posibles moves of the piece in that position
        if t  == 0 :
            self.position = x*16 + y
        else :
            self.position = x
    
    # reset all booleans of moves to 1
    def resetMoves(self) :
        self.DA = 1 #Represents the down-left Diagonal: 0->obstacles 1->no obstacle
        self.DB = 1 #Represents the down-rigth Diagonal
        self.DC = 1 #Represents the up-left Diagonal
        self.DD = 1 #Represents the up-rigth Diagonal
        self.VA = 1 #Represents the down Vertical
        self.VB = 1 #Represents the up Vertical
        self.HA = 1 #Represents the left Horitzontal
        self.HB = 1 #Represents the rigth Horitzontal
        
    #x --> position of the piece in format (1x128)
    def movePiece(self, x):
        self.position = x
        self.resetMoves()
        self.posibleMoves(1)
    
    #piezas --> position of all pieces in format (1x128)
    def setPiezas(self, piezas):
        self.piezas = piezas
        
    # return positions in tablero (1x128)
    def posibleMoves(self):
        positions = []
        x = 1
        while x < 8 :
            if self.HB: 
                positions.append(self.position + x)
            if self.VB:
                positions.append(self.position + (x*16))
            if self.DD:
                positions.append(self.position + (x*16) + x)
            if self.DC:
                positions.append(self.position + (x*16) - x)
            if self.HA:
                positions.append(self.position - x)
            if self.VB:
                positions.append(self.position - (x*16))
            if self.DB:
                positions.append(self.position - (x*16) + x)
            if self.DA:
                positions.append(self.position - (x*16) - x) 
            x = x + 1
            self.checkAvaliableMoves(x)
        self.moves = positions
    
    # The function will check if the moves are avaliable with the rest of the pieces
    def checkAvaliableMoves(self, x) :
        if self.HB and self.piezas.contains(self.position + x) :
            self.HB = 0
        if self.VB and self.piezas.contains(self.position + (x*16)) :
            self.VB = 0
        if self.DD and self.piezas.contains(self.position + (x*16) + x) :
            self.DD = 0
        if self.DC and self.piezas.contains(self.position + (x*16) - x) :
            self.DC = 0
        if self.HA and self.piezas.contains(self.position - x) :
            self.HA = 0
        if self.VB and self.piezas.contains(self.position - (x*16)) :
            self.VB = 0
        if self.DB:
                positions.append(self.position - (x*16) + x)
            if self.DA:
                positions.append(self.position - (x*16) - x)
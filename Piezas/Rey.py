# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 23:36:32 2018

@author: pau
"""

class Rey:
    
    #x = position in board (1x128)
    #piezas --> position of all pieces in format (1x128)
    def __init__(self, x, piezas):
        self.piezas = piezas
        self.position = x
        self.posibleMoves()
        
    #x --> position of the piece in format (1x128)
    def movePiece(self, x):
        self.position = x
        self.checkAvaliableMoves(1)
        
    #piezas --> position of all pieces in format (1x128)
    def setPiezas(self, piezas):
        self.piezas = piezas
    
    # return positions in tablero (1x128)
    def posibleMoves(self):
        positions = []
        x = 1
        if not ((self.position + x) in self.piezas) and self.insideTab(self.position + x) : 
            positions.append(self.position + x)
        if not ((self.position + (x*16)) in self.piezas) and self.insideTab(self.position + (x*16)) :
            positions.append(self.position + (x*16))
        if not ((self.position + (x*16) + x) in self.piezas) and self.insideTab(self.position + (x*16) + x) :
            positions.append(self.position + (x*16) + x)
        if not ((self.position + (x*16) - x) in self.piezas) and self.insideTab(self.position + (x*16) - x) :
            positions.append(self.position + (x*16) - x)
        if not ((self.position - x) in self.piezas) and self.insideTab(self.position - x) :
            positions.append(self.position - x)
        if not ((self.position - (x*16)) in self.piezas) and self.insideTab(self.position - (x*16)) :
            positions.append(self.position - (x*16))
        if not ((self.position - (x*16) + x) in self.piezas) and self.insideTab(self.position - (x*16) + x) :
            positions.append(self.position - (x*16) + x)
        if not ((self.position - (x*16) - x) in self.piezas) and self.insideTab(self.position - (x*16) - x) :
            positions.append(self.position - (x*16) - x) 
        self.moves = positions
        
    #Chexk if the position 'x' it's inside the Board
    def insideTab(self, x):
        return (x & 0x88) == 0 
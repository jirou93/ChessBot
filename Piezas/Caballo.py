# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 18:14:49 2018

@author: p.castro.sampol
"""

class Caballo:
    
    def __init__(self, x, piezas):
        self.piezas = piezas
        self.position = x
        self.posibleMoves()#Represents the posibles moves of the piece in that position
    
    #x --> position of the piece in format (1x128)
    def movePiece(self, x):
        self.position = x
        self.resetMoves()
        self.posibleMoves()
        
    # return positions in tablero (1x128)
    def posibleMoves(self):
        positions = []
        if self.insideTab(self.position + 31) and not (self.position + 31 in self.piezas) :
            positions.append(self.position + 31)
        if self.insideTab(self.position + 33) and not self.position + 33 in self.piezas :
            positions.append(self.position + 33)
        if self.insideTab(self.position + 14) and not self.position + 14 in self.piezas :
            positions.append(self.position + 14)
        if self.insideTab(self.position + 18) and not self.position + 18 in self.piezas :
            positions.append(self.position + 18)
        if self.insideTab(self.position - 14) and not self.position - 14 in self.piezas :
            positions.append(self.position - 14)
        if self.insideTab(self.position - 18) and not self.position -18 in self.piezas :
            positions.append(self.position - 18)
        if self.insideTab(self.position - 31) and not self.position - 31 in self.piezas :
            positions.append(self.position - 31)
        if self.insideTab(self.position - 33) and not self.position - 33 in self.piezas :
            positions.append(self.position - 33)
        self.moves = positions
        
    #Chexk if the position 'x' it's inside the Board
    def insideTab(self, x):
        return (x & 0x88) == 0    
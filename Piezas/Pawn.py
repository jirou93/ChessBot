# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 09:36:59 2018

@author: p.castro.sampol
"""

class Pawn :
    
    #x = position in board (1x128)
    #piezas --> position of all pieces in format (1x128)
    #color: w --> white, b --> black
    def __init__(self, x, piezas, color):
        if color == 'w' :
            self.white = 1
        else :
            self.white = -1
        self.piezas = piezas
        self.resetMoves()
        self.position = x
        self.posibleMoves()
        self.moved = False
        
    #x --> position of the piece in format (1x128)
    def movePiece(self, x):
        self.moved = True
        self.position = x
        self.resetMoves()
        self.checkAvaliableMoves(1)
    
    # return positions in tablero (1x128)
    def posibleMoves(self):
        if self.position + 16 in self.piezas :
            self.moves = []
        else :
            self.moves.append(self.position + 16*self.white)
            if not self.moved and self.position + 32 in self.piezas :
                self.moves.append(self.position + 32*self.white)
        
    #piezas --> position of all pieces in format (1x128)
    def setPiezas(self, piezas):
        self.piezas = piezas
    
    #Chexk if the position 'x' it's inside the Board
    def insideTab(self, x):
        return (x & 0x88) == 0 
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 10:08:43 2018

@author: p.castro.sampol
"""
import UtilFunctions 

class Dama:
    
    #x = position in board (1x128)
    #piezas --> position of all pieces in format (1x128)
    def __init__(self, x, piezas):
        self.piezas = piezas
        self.resetMoves()
        self.position = x
        self.posibleMoves()
    
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
        self.checkAvaliableMoves(1)
    
    #piezas --> position of all pieces in format (1x128)
    def setPiezas(self, piezas):
        self.piezas = piezas
        
    # return positions in tablero (1x128)
    def posibleMoves(self):
        positions = []
        x = 1
        while x < 8 :
            self.checkAvaliableMoves(x)
            if self.HB and self.insideTab(self.position + x) : 
                positions.append(self.position + x)
            if self.VB and self.insideTab(self.position + (x*16)) :
                positions.append(self.position + (x*16))
            if self.DD and self.insideTab(self.position + (x*16) + x) :
                positions.append(self.position + (x*16) + x)
            if self.DC and self.insideTab(self.position + (x*16) - x) :
                positions.append(self.position + (x*16) - x)
            if self.HA and self.insideTab(self.position - x) :
                positions.append(self.position - x)
            if self.VB and self.insideTab(self.position - (x*16)) :
                positions.append(self.position - (x*16))
            if self.DB and self.insideTab(self.position - (x*16) + x) :
                positions.append(self.position - (x*16) + x)
            if self.DA and self.insideTab(self.position - (x*16) - x) :
                positions.append(self.position - (x*16) - x) 
            x = x + 1
        self.moves = positions
    
    # The function will check if the moves are avaliable with the rest of the pieces
    def checkAvaliableMoves(self, x) :
        if self.HB and self.position + x in self.piezas :
            self.HB = 0
        if self.VB and self.position + (x*16) in self.piezas :
            self.VB = 0
        if self.DD and self.position + (x*16) + x in self.piezas :
            self.DD = 0
        if self.DC and self.position + (x*16) - x in self.piezas :
            self.DC = 0
        if self.HA and self.position - x in self.piezas :
            self.HA = 0
        if self.VB and self.position - (x*16) in self.piezas :
            self.VB = 0
        if self.DB and self.position - (x*16) + x in self.piezas :
            self.DB = 0
        if self.DA and self.position - (x*16) - x in self.piezas :
            self.DA = 0
            
    #Chexk if the position 'x' it's inside the Board
    def insideTab(self, x):
        return (x & 0x88) == 0 
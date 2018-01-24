# -*- coding: utf-8 -*-
"""
Pau Castro Sampol

23/01/2018
"""
import numpy as np


class Board:
    
    def __init__(self):
        self.board = self.iniBoard() #Board with all pieces
        
    #Fuction that inicialitzates the Board
    def iniBoard(self):
        mat = np.zeros(128)
        mat[0] = mat[7] = mat[112] = mat[119] = 3   #3 --> Rock
        mat[1] = mat[6] = mat[113] = mat[118] = 5   #5 --> Horse
        mat[2] = mat[5] = mat[114] = mat[117] = 4   #4 --> Bishop
        mat[3] = mat[115] =1                        #1 --> King
        mat[4] = mat[116] = 2                       #2 --> Queen
        i = 0
        while i < 8 :
            mat[16+i] = mat[96 + i] = 6             #6 --> Pawn
            i = i + 1
        return mat
    
    #functions that prints the board on the terminal
    def printBoard(self) :
        i = 0
        while i < 8 :
            line = self.board[(i*16):((i*16)+8)]
            print(line)
            i = i +1
            

# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import numpy as np


class Tablero:
    
    def __init__(self):
        self.tab_posiciones = np.empty((1,128)) #tablero donde veremos los movimientos legales
        self.tab_piezas = self.iniciarTablero()
        


    def iniciarTablero(self):
        mat = [[0 for col in range(8)]for row in range(8)]
        mat[0][0] = mat[0][7] = 'T'
        mat[0][1] = mat[0][6] = 'C'
        mat[0][2] = mat[0][5] = 'A'
        mat[0][3] = 'R'
        mat[0][4] = 'D'
        mat[1] = ['P' for col in range(8)]
        mat[7][0] = mat[7][7] = 't'
        mat[7][1] = mat[7][6] = 'c'
        mat[7][2] = mat[7][5] = 'a'
        mat[7][3] = 'r'
        mat[7][4] = 'd'
        mat[6] = ['p' for col in range(8)]
        return mat
 
    def printarTablero(self) :
        for col in self.tab_piezas :
            print(col)
            
tab = Tablero()
tab.printarTablero()
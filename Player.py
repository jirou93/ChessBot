# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:19:54 2018

@author: p.castro.sampol
"""
import Torre
import Dama
import Rey
import Alfil
import Caballo
import Pawn

class Player:
    
    #Positions --> will contain all the position of the player pieces
    #pieces --> will contain the position of all pieces of the game
    #color --> 'w' = Player is playing with white, 'b' Player is playing with black
    def __init__(self, positions, pieces, color) :
        self.color = color
        self.longCastling = True            #long Castling avaliable
        self.shortCastling = True           #short Castling avaliable
        #In the next vector I will save the positions of all the pieces of the player
        # If the piece is dead it will put False
        #the vector will have the next estructure:
        #[King,Queen,Rock,Rock,Bishop,Bishop,Horse,Horse, Pawnx8]
        self.piecesPosition = positions
        #In the next vector I will save all the pieces of the player
        # If the piece is dead it will put False
        #the vector will have the next estructure:
        #[King,Queen,Rock,Rock,Bishop,Bishop,Horse,Horse, Pawnx8]
        #if the piece is dead I will put 
        self.pieces = self.createPieces(pieces)
        
    #with this function I will create all the pieces for the position
    def createPieces(self, completPieces) :
        pieces = []
        i = 0
        for p in self.piecesPosition :
            if not p :
                pieces.append(False)
            else :
                #Creation of the King
                if i == 0 :
                    pieces.append(Rey(self.piecesPosition[i], completPieces))
                #Creation of the Queen
                if i == 1 :
                    pieces.append(Dama(self.piecesPosition[i], completPieces))
                #Creation of the Rocks
                if i == 2 or i == 3 :
                    pieces.append(Torre(self.piecesPosition[i], completPieces))
                #Creation of the Bishops
                if i == 4 or i == 5 :
                    pieces.append(Alfil(self.piecesPosition[i], self.completPieces))
                #Creation of the Horses
                if i == 6 or i == 7 :
                    pieces.append(Caballo(self.piecesPosition[i], self.completPieces))
                #Creation of the Pawns
                else :
                    pieces.append(Caballo(self.piecesPosition[i], self.completPieces, self.color))
            i = i + 1
        return pieces
    
    #change the position of all pieces to the vector "pieces"
    def setPositions(self, positions) :
        self.piecesPosition = positions
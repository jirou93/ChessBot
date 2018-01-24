# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 18:23:55 2018

@author: p.castro.sampol
"""

class UtilFunctions:
    
    def insideTab(self, x):
        return (x & 0x88) == 0 
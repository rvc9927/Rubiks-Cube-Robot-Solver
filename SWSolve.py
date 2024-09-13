import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import *
from time import sleep
import json
import pandas as pd
import itertools
from CubeSetup2 import Moves, output, Cube
from CubeSetup2 import FullCube
from MotorFunctions import *
#from MotorFunctions import HWmoves
from time import process_time
Top = FullCube.Top
Front = FullCube.Front
Right = FullCube.Right
Left = FullCube.Left
Back = FullCube.Back
Bottom = FullCube.Bottom
moves_out = FullCube.moves_out
Flip = FullCube.Flip
FullCube = Cube(Top, Front, Right, Left, Back, Bottom, moves_out, Flip, dict)
moves_out = []
#from Cam import *
class Solve(Cube):

    def initializemoves(self, Top, Front, Right, Left, Back, Bottom, moves_out, Flip, dict):
        self.Top = np.arange(9).reshape(3, 3)
        self.Right = np.arange(9).reshape(3, 3)
        self.Left = np.arange(9).reshape(3, 3)
        self.Front = np.arange(9).reshape(3, 3)
        self.Back = np.arange(9).reshape(3, 3)
        self.Bottom = np.arange(9).reshape(3, 3)
        self.moves_out = moves_out
        self.Flip = Flip

        """# Set middle colors
        self.Top[1, 1] = "w"
        self.Right[1, 1] = "g"
        self.Left[1, 1] = "b"
        self.Front[1, 1] = "o"
        self.Back[1, 1] = "r"
        self.Bottom[1, 1] = "y"

        # Top Face
        ColorDetect(self)
        self.Top[2, 2] = self.BotLeft
        self.Top[1, 2] = self.BotMid
        self.Top[0, 2] = self.BotRight
        Moves.move(self, "ccw", 'Top')
        ColorDetect(self)
        self.Top[2, 0] = self.BotLeft
        self.Top[2, 1] = self.BotMid
        Moves.move(self, "ccw", 'Top')
        ColorDetect(self)
        self.Top[0, 0] = self.BotLeft
        self.Top[1, 0] = self.BotMid
        Moves.move(self, "ccw", 'Top')
        ColorDetect(self)
        self.Top[0, 1] = self.BotMid
        Moves.move(self, "ccw", 'Top')

        # Right Face
        Moves.move(self, "ccw", 'Front')
        Moves.move(self, "cw", 'Back')
        Moves.move(self, "ccw", 'Top')
        ColorDetect(self)
        self.Right[0, 0] = self.BotLeft
        self.Right[1, 0] = self.BotMid
        self.Right[2, 0] = self.BotRight
        Moves.move(self, "cw", 'Top')
        Moves.move(self, "cw", 'Top')
        ColorDetect(self)
        self.Right[2, 2] = self.BotLeft
        self.Right[1, 2] = self.BotMid
        self.Right[0, 2] = self.BotRight
        Moves.move(self, "cw", 'Top')
        Moves.move(self, "cw", 'Front')
        Moves.move(self, "ccw", 'Back')
        Moves.move(self, "cw", 'Right')
        Moves.move(self, "ccw", 'Front')
        Moves.move(self, "cw", 'Back')
        Moves.move(self, "cw", 'Top')
        ColorDetect(self)
        self.Right[0, 1] = self.BotMid
        Moves.move(self, "ccw", 'Top')
        Moves.move(self, "ccw", 'Top')
        ColorDetect(self)
        self.Right[2, 1] = self.BotMid
        Moves.move(self, "cw", 'Top')
        Moves.move(self, "cw", 'Front')
        Moves.move(self, "ccw", 'Back')
        Moves.move(self, "ccw", 'Right')

        # Left Face
        Moves.move(self, "cw", 'Front')
        Moves.move(self, "ccw", 'Back')
        Moves.move(self, "ccw", 'Top')
        ColorDetect(self)
        self.Left[2, 2] = self.BotLeft
        self.Left[1, 2] = self.BotMid
        self.Left[0, 2] = self.BotRight
        Moves.move(self, "cw", 'Top')
        Moves.move(self, "cw", 'Top')
        ColorDetect(self)
        self.Left[0, 0] = self.BotLeft
        self.Left[1, 0] = self.BotMid
        self.Left[2, 0] = self.BotRight
        Moves.move(self, "ccw", 'Top')
        Moves.move(self, "ccw", 'Front')
        Moves.move(self, "cw", 'Back')
        Moves.move(self, "cw", 'Left')
        Moves.move(self, "cw", 'Front')
        Moves.move(self, "ccw", 'Back')
        Moves.move(self, "ccw", 'Top')
        ColorDetect(self)
        self.Left[2, 1] = self.BotMid
        Moves.move(self, "cw", 'Top')
        Moves.move(self, "cw", 'Top')
        ColorDetect(self)
        self.Left[0, 1] = self.BotMid
        Moves.move(self, "ccw", 'Top')
        Moves.move(self, "ccw", 'Front')
        Moves.move(self, "cw", 'Back')
        Moves.move(self, "ccw", 'Left')

        # Back Face
        Moves.move(self, "cw", 'Left')
        Moves.move(self, "ccw", 'Right')
        ColorDetect(self)
        self.Back[0, 0] = self.BotLeft
        self.Back[1, 0] = self.BotMid
        self.Back[2, 0] = self.BotRight
        Moves.move(self, "cw", 'Top')
        Moves.move(self, "cw", 'Top')
        ColorDetect(self)
        self.Back[0, 2] = self.BotLeft
        self.Back[1, 2] = self.BotMid
        self.Back[2, 2] = self.BotRight
        Moves.move(self, "ccw", 'Top')
        Moves.move(self, "ccw", 'Top')
        Moves.move(self, "ccw", 'Left')
        Moves.move(self, "cw", 'Right')
        Moves.move(self, "cw", 'Back')
        Moves.move(self, "cw", 'Left')
        Moves.move(self, "ccw", 'Right')
        ColorDetect(self)
        self.Back[2, 1] = self.BotMid
        Moves.move(self, "cw", 'Top')
        Moves.move(self, "cw", 'Top')
        ColorDetect(self)
        self.Back[0, 1] = self.BotMid
        Moves.move(self, "ccw", 'Top')
        Moves.move(self, "ccw", 'Top')
        Moves.move(self, "ccw", 'Left')
        Moves.move(self, "cw", 'Right')
        Moves.move(self, "ccw", 'Back')

        # Front Face
        Moves.move(self, "ccw", 'Left')
        Moves.move(self, "cw", 'Right')
        ColorDetect(self)
        self.Front[2, 2] = self.BotLeft
        self.Front[1, 2] = self.BotMid
        self.Front[0, 2] = self.BotRight
        Moves.move(self, "cw", 'Top')
        Moves.move(self, "cw", 'Top')
        ColorDetect(self)
        self.Front[0, 0] = self.BotLeft
        self.Front[1, 0] = self.BotMid
        self.Front[2, 0] = self.BotRight
        Moves.move(self, "ccw", 'Top')
        Moves.move(self, "ccw", 'Top')
        Moves.move(self, "cw", 'Left')
        Moves.move(self, "ccw", 'Right')
        Moves.move(self, "cw", 'Front')
        Moves.move(self, "ccw", 'Left')
        Moves.move(self, "cw", 'Right')
        ColorDetect(self)
        self.Front[0, 1] = self.BotMid
        Moves.move(self, "cw", 'Top')
        Moves.move(self, "cw", 'Top')
        ColorDetect(self)
        self.Front[2, 1] = self.BotMid
        Moves.move(self, "ccw", 'Top')
        Moves.move(self, "ccw", 'Top')
        Moves.move(self, "ccw", 'Left')
        Moves.move(self, "cw", 'Right')
        Moves.move(self, "ccw", 'Back')

        # Bottom Face
        Moves.move(self, "cw", 'Left')
        Moves.move(self, "cw", 'Left')
        Moves.move(self, "cw", 'Right')
        Moves.move(self, "cw", 'Right')
        ColorDetect(self)
        self.Bottom[2, 2] = self.BotLeft
        self.Bottom[1, 2] = self.BotMid
        self.Bottom[0, 2] = self.BotRight
        Moves.move(self, "cw", 'Top')
        Moves.move(self, "cw", 'Top')
        ColorDetect(self)
        self.Bottom[0, 0] = self.BotLeft
        self.Bottom[1, 0] = self.BotMid
        self.Bottom[2, 0] = self.BotRight
        Moves.move(self, "cw", 'Left')
        Moves.move(self, "cw", 'Left')
        Moves.move(self, "cw", 'Right')
        Moves.move(self, "cw", 'Right')
        Moves.move(self, "cw", 'Front')
        Moves.move(self, "cw", 'Front')
        Moves.move(self, "cw", 'Back')
        Moves.move(self, "cw", 'Back')
        Moves.move(self, "cw", 'Top')
        ColorDetect(self)
        self.Bottom[2, 1] = self.BotMid
        Moves.move(self, "cw", 'Top')
        Moves.move(self, "cw", 'Top')
        ColorDetect(self)
        self.Bottom[0, 1] = self.BotMid
        Moves.move(self, "cw", 'Top')
        Moves.move(self, "cw", 'Top')
        Moves.move(self, "cw", 'Front')
        Moves.move(self, "cw", 'Front')
        Moves.move(self, "cw", 'Back')
        Moves.move(self, "cw", 'Back')
"""

    def check(self):
        Flat = np.ravel(self)
        List = ndarray.tolist(Flat)
        return len(set(List)) == 1


    def WhiteMoveBot(self): #Move White From Bottom Face to Top to Create Cross
        Top = self.Top.copy()
        Front = self.Front.copy()
        Right = self.Right.copy()
        Left = self.Left.copy()
        Back = self.Back.copy()
        Bottom = self.Bottom.copy()
        moves_out = self.moves_out
        Flip ='no'
        #side = [self.Top.copy(), self.Front.copy(), self.Right.copy(), self.Left.copy(), self.Back.copy(), self.Bottom.copy()]
        #j = 0
        """oDone = False
        rDone = False
        gDone = False
        bDone = False
        for x in bot:
            #j = j + 1
            for idx, i in np.ndenumerate(x):"""
        if Bottom[0,1] == "w" or Bottom[1,0] == "w" or Bottom[2,1] == "w" or Bottom[1,2] == "w":
            while Bottom[0, 1] == "w" or Bottom[1, 0] == "w" or Bottom[2, 1] == "w" or Bottom[1, 2] == "w":
                if Bottom[0,1] == "w": #and i2 == "g":  #Go through and iterate all possible situations to make the white cross
                    AdjFace = self.Front[2,1]
                elif Bottom[1,0] == "w":
                    AdjFace = self.Left[2,1]
                elif Bottom[1,2] == "w":
                    AdjFace = self.Right[2, 1]
                elif Bottom[2,1] == "w":
                    AdjFace = self.Back[2, 1]
                #if not eval((eval(f'AdjFace')+ 'Done')): #eval((eval(f'corner')+ 'a')
                Top = self.Top.copy()
                Front = self.Front.copy()
                Right = self.Right.copy()
                Left = self.Left.copy()
                Back = self.Back.copy()
                Bottom = self.Bottom.copy()
                moves_out = self.moves_out
                if AdjFace =="o":
                    Top = self.Top.copy()
                    Front = self.Front.copy()
                    Right = self.Right.copy()
                    Left = self.Left.copy()
                    Back = self.Back.copy()
                    Bottom = self.Bottom.copy()
                    moves_out = self.moves_out
                    while self.Front[2,1] != "o" or self.Bottom[0,1] != "w": #this works, just extrapolate for all colors
                        Moves.move(self, "cw", 'Bottom')
                    Moves.move(self, "cw", 'Front')
                    Moves.move(self, "cw", 'Front')
                if AdjFace == "g":
                    Top = self.Top.copy()
                    Front = self.Front.copy()
                    Right = self.Right.copy()
                    Left = self.Left.copy()
                    Back = self.Back.copy()
                    Bottom = self.Bottom.copy()
                    moves_out = self.moves_out
                    while self.Right[2, 1] != "g" or self.Bottom[1, 2] != "w":  # this works, just extrapolate for all colors
                        Moves.move(self, "cw", 'Bottom')
                    Moves.move(self, "cw", 'Right')
                    Moves.move(self, "cw", 'Right')
                if AdjFace =="r":
                    Top = self.Top.copy()
                    Front = self.Front.copy()
                    Right = self.Right.copy()
                    Left = self.Left.copy()
                    Back = self.Back.copy()
                    Bottom = self.Bottom.copy()
                    moves_out = self.moves_out
                    while self.Back[2,1] != "r" or self.Bottom[2,1] != "w": #this works, just extrapolate for all colors
                        Moves.move(self, "cw", 'Bottom')
                    Moves.move(self, "cw", 'Back')
                    Moves.move(self, "cw", 'Back')
                if AdjFace == "b":
                    Top = self.Top.copy()
                    Front = self.Front.copy()
                    Right = self.Right.copy()
                    Left = self.Left.copy()
                    Back = self.Back.copy()
                    Bottom = self.Bottom.copy()
                    moves_out = self.moves_out
                    while self.Left[2, 1] != "b" or self.Bottom[1, 0] != "w":  # this works, just extrapolate for all colors
                        Moves.move(self, "cw", 'Bottom')
                    Moves.move(self, "cw", 'Left')
                    Moves.move(self, "cw", 'Left')
                Top = self.Top.copy()
                Front = self.Front.copy()
                Right = self.Right.copy()
                Left = self.Left.copy()
                Back = self.Back.copy()
                Bottom = self.Bottom.copy()
                moves_out = self.moves_out


    def WhiteMoveSides(self):
        Topc = self.Top.copy()
        Frontc = self.Front.copy()
        Rightc = self.Right.copy()
        Backc = self.Back.copy()
        Leftc = self.Left.copy()

        CheckSide = ['Front', 'Right', 'Back', 'Left']
        RightSide = ['Right', 'Back', 'Left', 'Front'] #Right side in relation to checkside
        BackSide = ['Back', 'Left', 'Front', 'Right']
        LeftSide = [ 'Left', 'Front', 'Right', 'Back']
        CheckTopF = [(2,1), (1,2), (0,1), (1,0)] #Check if value on top Front to be moved is white/correct
        CheckTopL = [(1,0), (2,1), (1,2), (0,1)]  # Check if value on top Left to be moved is white/correct
        CheckTopR = [(1,2), (0,1), (1,0), (2,1)] #Check if value on top Right to be moved is white/correct
        while self.Top[0, 1] != "w" or self.Top[1, 0] != "w" or self.Top[1, 2] != "w" or self.Top[2, 1] != "w":
            if Topc[0, 1] == "w" or Topc[1, 0] == "w" or Topc[1, 2] == "w" or Topc[2, 1] == "w":
                if Topc[0, 1] == "w" and Backc[0,1] != Backc[1,1]:
                    Moves.move(self, "ccw", 'Back')
                    Moves.move(self, "ccw", 'Back')
                if Topc[1, 0] == "w" and Leftc[0,1] != Leftc[1,1]:
                    Moves.move(self, "ccw", 'Left')
                    Moves.move(self, "ccw", 'Left')
                if Topc[1, 2] == "w" and Rightc[0,1] != Rightc[1,1]:
                    Moves.move(self, "ccw", 'Right')
                    Moves.move(self, "ccw", 'Right')
                if Topc[2, 1] == "w" and Frontc[0,1] != Frontc[1,1]:
                    Moves.move(self, "ccw", 'Front')
                    Moves.move(self, "ccw", 'Front')
            Solve.WhiteMoveBot(self)
            sides = [self.Front, self.Right, self.Back, self.Left]
            for (side, CS, RS, BS, LS, CTF, CTL, CTR) in zip(sides, CheckSide, RightSide,BackSide,LeftSide, CheckTopF, CheckTopL, CheckTopR): # Fix white and YElow adjacent sides
                Top = self.Top.copy()
                Front = self.Front.copy()
                Right = self.Right.copy()
                Left = self.Left.copy()
                Back = self.Back.copy()
                Bottom = self.Bottom.copy()
                moves_out = self.moves_out
                if eval(eval(f'CS'))[0,1] == "w" or eval(eval(f'CS'))[1,0] == "w" or eval(eval(f'CS'))[1,2] == "w" or eval(eval(f'CS'))[2,1] == "w":
                    if eval(eval(f'CS'))[0,1] =="w":
                        Topi = self.Top.copy()
                        Front = self.Front.copy()
                        Right = self.Right.copy()
                        Left = self.Left.copy()
                        Back = self.Back.copy()
                        Bottom = self.Bottom.copy()
                        moves_out = self.moves_out
                        Moves.move(self, "ccw", eval(f'CS'))
                        Moves.move(self, "cw", eval(f'LS'))
                        Moves.move(self, "ccw", 'Bottom')
                        if Topi[eval(f'CTL')] == "w" and eval(eval(f'LS'))[0, 1] == eval(eval(f'LS'))[1, 1]:
                            Moves.move(self, "ccw", eval(f'LS'))
                        Moves.move(self, "cw", eval(f'CS'))
                        Solve.WhiteMoveBot(self)
                    if eval(eval(f'CS'))[1,0] == "w":
                        Topi = self.Top.copy()
                        Front = self.Front.copy()
                        Right = self.Right.copy()
                        Left = self.Left.copy()
                        Back = self.Back.copy()
                        Bottom = self.Bottom.copy()
                        moves_out = self.moves_out
                        Moves.move(self, "cw", eval(f'LS'))
                        Moves.move(self, "ccw", 'Bottom')
                        if Topi[eval(f'CTL')] == "w" and eval(eval(f'LS'))[0, 1] == eval(eval(f'LS'))[1, 1]:
                            Moves.move(self, "ccw", eval(f'LS'))
                        #if Topi[eval(f'CTF')] == "w" and eval(eval(f'CS'))[0, 1] == eval(eval(f'CS'))[1, 1]:
                        #    Moves.move(self, "ccw", eval(f'CS'))
                        Solve.WhiteMoveBot(self)
                    if eval(eval(f'CS'))[1, 2] == "w":
                        Topi = self.Top.copy()
                        Front = self.Front.copy()
                        Right = self.Right.copy()
                        Left = self.Left.copy()
                        Back = self.Back.copy()
                        Bottom = self.Bottom.copy()
                        moves_out = self.moves_out
                        Moves.move(self, "ccw", eval(f'RS'))
                        Moves.move(self, "cw", 'Bottom')
                        if Topi[eval(f'CTR')] == "w" and eval(eval(f'RS'))[0, 1] == eval(eval(f'RS'))[1, 1]:
                            Moves.move(self, "cw", eval(f'RS'))
                        Solve.WhiteMoveBot(self)
                    if eval(eval(f'CS'))[2,1] == "w":
                        Topi = self.Top.copy()
                        Front = self.Front.copy()
                        Right = self.Right.copy()
                        Left = self.Left.copy()
                        Back = self.Back.copy()
                        Bottom = self.Bottom.copy()
                        moves_out = self.moves_out
                        Moves.move(self, "cw", eval(f'CS'))
                        Moves.move(self, "cw", eval(f'LS'))
                        Moves.move(self, "ccw", 'Bottom')
                        if Topi[eval(f'CTL')] == "w" and eval(eval(f'LS'))[0, 1] == eval(eval(f'LS'))[1, 1]:
                            Moves.move(self, "ccw", eval(f'LS'))
                        if Topi[eval(f'CTF')] == "w" and eval(eval(f'CS'))[0, 1] == eval(eval(f'CS'))[1, 1]:
                            Moves.move(self, "ccw", eval(f'CS'))
                        Solve.WhiteMoveBot(self)
                    Top = self.Top.copy()
                    Front = self.Front.copy()
                    Right = self.Right.copy()
                    Left = self.Left.copy()
                    Back = self.Back.copy()
                    Bottom = self.Bottom.copy()
                    moves_out = self.moves_out
        #HAVE TO CHECK INPUTS FOR MOVES TO REFERENCE CORRECT SIDES

    def WhiteCorners(self):
        Top = self.Top
        Front = self.Front
        Right = self.Right
        Left = self.Left
        Back = self.Back
        Bottom = self.Bottom
        FLa = ['w', 'o', 'b']  # REPRESENT Finished
        FRa = ['w', 'o', 'g']
        BLa = ['w', 'r', 'b']
        BRa = ['w', 'r', 'g']

        # TFL = [Top[2,0],Front[0,0],Left[0,2]] # REPRESENT INITIAL CORNERS
        # TFR = [Top[2, 2], Front[0, 2], Right[0, 0]]
        # TBL = [Top[0, 0], Back[0, 2], Left[0, 0]]
        # TBR = [Top[2, 0], Back[0, 0], Right[0, 2]]
        # TopCorners = [TFL, TFR, TBL, TBR]
        # BFL = [Bottom[0, 0], Front[2, 0], Left[2, 2]]
        # BFR = [Bottom[0, 2], Front[2, 2], Right[2, 0]]
        # BBL = [Bottom[2, 0], Back[2, 2], Left[2, 0]]
        # BBR = [Bottom[2, 2], Back[0, 2], Right[2, 2]]
        BotCorners = [f'BFL', f'BFR', f'BBL', f'BBR', f'TFL', f'TFR', f'TBL', f'TBR']
        while not (Solve.check(self.Top) and Solve.check(self.Front[0]) and Solve.check(self.Right[0]) and Solve.check(self.Back[0]) and Solve.check(self.Left[0])):
            for corner in BotCorners:
                # Top = self.Top.copy()
                # Front = self.Front.copy()
                # Right = self.Right.copy()
                # Left = self.Left.copy()
                # Back = self.Back.copy()
                # Bottom = self.Bottom.copy()
                #moves_out = self.moves_out

                TFL = [self.Top[2, 0], self.Front[0, 0], self.Left[0, 2]]  # REPRESENT ACTUAL CORNERS
                TFR = [self.Top[2, 2], self.Front[0, 2], self.Right[0, 0]]
                TBL = [self.Top[0, 0], self.Back[0, 2], self.Left[0, 0]]
                TBR = [self.Top[0, 2], self.Back[0, 0], self.Right[0, 2]]
                TopCornersn = [TFL, TFR, TBL, TBR]
                BFL = [self.Bottom[0, 0], self.Front[2, 0], self.Left[2, 2]]
                BFR = [self.Bottom[0, 2], self.Front[2, 2], self.Right[2, 0]]
                BBL = [self.Bottom[2, 0], self.Back[2, 2], self.Left[2, 0]]
                BBR = [self.Bottom[2, 2], self.Back[2, 0], self.Right[2, 2]]
                s = set(eval(corner))
                if 'w' in s: # CHECK BBL
                    cornerupdate = eval(corner)
                    if cornerupdate != eval((eval(f'corner')+ 'a')[1:]):
                        if corner == 'TFR':
                            Top = self.Top.copy()
                            Front = self.Front.copy()
                            Right = self.Right.copy()
                            Left = self.Left.copy()
                            Back = self.Back.copy()
                            Bottom = self.Bottom.copy()
                            moves_out = self.moves_out
                            Moves.move(self, "ccw", 'Right')
                            Moves.move(self, "cw", 'Bottom')
                            Moves.move(self, "cw", 'Right')
                        if corner == 'TFL':
                            Top = self.Top.copy()
                            Front = self.Front.copy()
                            Right = self.Right.copy()
                            Left = self.Left.copy()
                            Back = self.Back.copy()
                            Bottom = self.Bottom.copy()
                            moves_out = self.moves_out
                            Moves.move(self, "cw", 'Left')
                            Moves.move(self, "ccw", 'Bottom')
                            Moves.move(self, "ccw", 'Left')
                        if corner == 'TBR':
                            Top = self.Top.copy()
                            Front = self.Front.copy()
                            Right = self.Right.copy()
                            Left = self.Left.copy()
                            Back = self.Back.copy()
                            Bottom = self.Bottom.copy()
                            moves_out = self.moves_out
                            Moves.move(self, "cw", 'Right')
                            Moves.move(self, "ccw", 'Bottom')
                            Moves.move(self, "ccw", 'Right')
                        if corner == 'TBL':
                            Top = self.Top.copy()
                            Front = self.Front.copy()
                            Right = self.Right.copy()
                            Left = self.Left.copy()
                            Back = self.Back.copy()
                            Bottom = self.Bottom.copy()
                            moves_out = self.moves_out
                            Moves.move(self, "ccw", 'Left')
                            Moves.move(self, "cw", 'Bottom')
                            Moves.move(self, "cw", 'Left')
                    if cornerupdate != eval((eval(f'corner')+ 'a')[1:]):
                        if 'r' in s and 'b' in s and 'w' in s:
                            Top = self.Top.copy()
                            Front = self.Front.copy()
                            Right = self.Right.copy()
                            Left = self.Left.copy()
                            Back = self.Back.copy()
                            Bottom = self.Bottom.copy()
                            moves_out = self.moves_out
                            BBL = [Bottom[2, 0], Back[2, 2], Left[2, 0]]
                            TBL = [self.Top[0, 0], self.Back[0, 2], self.Left[0, 0]]
                            while 'r' not in BBL or 'b' not in BBL or 'w' not in BBL:
                                Top = self.Top.copy()
                                Front = self.Front.copy()
                                Right = self.Right.copy()
                                Left = self.Left.copy()
                                Back = self.Back.copy()
                                Bottom = self.Bottom.copy()
                                moves_out = self.moves_out
                                if 'w' in TBL:
                                    Moves.move(self, "ccw", 'Left')
                                    Moves.move(self, "cw", 'Bottom')
                                    Moves.move(self, "cw", 'Left')
                                Moves.move(self, "cw", 'Bottom')
                                TBL = [self.Top[0, 0], self.Back[0, 2], self.Left[0, 0]]
                                BBL = [self.Bottom[2, 0], self.Back[2, 2], self.Left[2, 0]]
                            while (self.Top[0,0] != 'w') or (self.Back[0, 2] != 'r') or self.Left[0, 0] != 'b':
                                Moves.RightAlgorithm(self, 'Back')
                        if 'r' in s and 'g' in s and 'w' in s:
                            Top = self.Top.copy()
                            Front = self.Front.copy()
                            Right = self.Right.copy()
                            Left = self.Left.copy()
                            Back = self.Back.copy()
                            Bottom = self.Bottom.copy()
                            moves_out = self.moves_out
                            BBR = [Bottom[2, 2], Back[2, 0], Right[2, 2]]
                            TBR = [self.Top[0, 2], self.Back[0, 0], self.Right[0, 2]]
                            while 'r' not in BBR or 'g' not in BBR or 'w' not in BBR:
                                Top = self.Top.copy()
                                Front = self.Front.copy()
                                Right = self.Right.copy()
                                Left = self.Left.copy()
                                Back = self.Back.copy()
                                Bottom = self.Bottom.copy()
                                moves_out = self.moves_out
                                if 'w' in TBR:
                                    Moves.move(self, "cw", 'Right')
                                    Moves.move(self, "ccw", 'Bottom')
                                    Moves.move(self, "ccw", 'Right')
                                Moves.move(self, "ccw", 'Bottom')
                                BBR = [self.Bottom[2, 2], self.Back[2, 0], self.Right[2, 2]]
                                TBR = [self.Top[0, 2], self.Back[0, 0], self.Right[0, 2]]
                            while (self.Top[0,2] != 'w') or (self.Back[0, 0] != 'r') or self.Right[0, 2] != 'g':
                                Moves.RightAlgorithm(self, 'Right')
                        if 'o' in s and 'g' in s and 'w' in s:
                            Top = self.Top.copy()
                            Front = self.Front.copy()
                            Right = self.Right.copy()
                            Left = self.Left.copy()
                            Back = self.Back.copy()
                            Bottom = self.Bottom.copy()
                            moves_out = self.moves_out
                            BFR = [self.Bottom[0, 2], self.Front[2, 2], self.Right[2, 0]]
                            TFR = [self.Top[2, 2], self.Front[0, 2], self.Right[0, 0]]
                            while 'o' not in BFR or 'g' not in BFR or 'w' not in BFR:
                                Top = self.Top.copy()
                                Front = self.Front.copy()
                                Right = self.Right.copy()
                                Left = self.Left.copy()
                                Back = self.Back.copy()
                                Bottom = self.Bottom.copy()
                                moves_out = self.moves_out
                                if 'w' in TFR:
                                    Moves.move(self, "ccw", 'Right')
                                    Moves.move(self, "ccw", 'Bottom')
                                    Moves.move(self, "cw", 'Right')
                                Moves.move(self, "ccw", 'Bottom')
                                BFR = [self.Bottom[0, 2], self.Front[2, 2], self.Right[2, 0]]
                                TFR = [self.Top[2, 2], self.Front[0, 2], self.Right[0, 0]]
                            while (self.Top[2,2] != 'w') or (self.Front[0, 2] != 'o') or self.Right[0, 0] != 'g':
                                Moves.RightAlgorithm(self, 'Front')
                        if 'o' in s and 'b' in s and 'w' in s:
                            Top = self.Top.copy()
                            Front = self.Front.copy()
                            Right = self.Right.copy()
                            Left = self.Left.copy()
                            Back = self.Back.copy()
                            Bottom = self.Bottom.copy()
                            moves_out = self.moves_out
                            BFL = [self.Bottom[0, 0], self.Front[2, 0], self.Left[2, 2]]
                            TFL = [self.Top[2, 0], self.Front[0, 0], self.Left[0, 2]]
                            while 'o' not in BFL or 'b' not in BFL or 'w' not in BFL:
                                if 'w' in TFL:
                                    Moves.move(self, "cw", 'Left')
                                    Moves.move(self, "cw", 'Bottom')
                                    Moves.move(self, "ccw", 'Left')
                                Moves.move(self, "cw", 'Bottom')
                                TFL = [self.Top[2, 0], self.Front[0, 0], self.Left[0, 2]]
                                BFL = [self.Bottom[0, 0], self.Front[2, 0], self.Left[2, 2]]
                            while (self.Top[2,0] != 'w') or (self.Front[0, 0] != 'o') or self.Left[0, 2] != 'b':
                                Moves.RightAlgorithm(self, 'Left')

    def SolveLayerTwo(self): # Solve for 2nd layer # Done
        Topc = self.Top.copy()
        Frontc = self.Front.copy()
        Rightc = self.Right.copy()
        Backc = self.Back.copy()
        Leftc = self.Left.copy()
        Flip = 'yes'
        self.Flip = 'yes'


        CheckSide = ['Front', 'Right', 'Back', 'Left']
        RightSide = ['Right', 'Back', 'Left', 'Front']  # Right side in relation to checkside
        BackSide = ['Back', 'Left', 'Front', 'Right']
        LeftSide = ['Left', 'Front', 'Right', 'Back']
        CheckTopFront = [(2, 1), (1, 2), (0, 1), (1, 0)]  # Check if value on Front Top to be moved is white/correct
        CheckTopRight = [(1, 2), (0, 1), (1, 0), (2, 1)]
        CheckTopBack = [ (0, 1), (1, 0), (2, 1), (1, 2)]
        CheckTopLeft = [(1, 0), (2, 1), (1, 2), (0, 1)]
        #Flipping Everything to make it easier to picture/code
        self.FrontFlip = np.flip(self.Front.copy())
        self.RightFlip = np.flip(self.Left.copy())
        self.LeftFlip = np.flip(self.Right.copy())
        self.BackFlip = np.flip(self.Back.copy())
        self.TopFlip = np.flip(self.Bottom.copy())
        self.BottomFlip = np.flip(self.Top.copy())

        self.Front = self.FrontFlip.copy()
        self.Right = self.RightFlip.copy()
        self.Left = self.LeftFlip.copy()
        self.Back = self.BackFlip.copy()
        self.Top = self.TopFlip.copy()
        self.Bottom = self.BottomFlip.copy()
        i = 0
        sides = [self.Front, self.Right, self.Back, self.Left]
        while not (Solve.check(self.Front[1]) and (Solve.check(self.Right[1])) and (Solve.check(self.Left[1])) and (Solve.check(self.Back[1]))):
            for (side, CS, RS, BS, LS, CTF, CTR, CTB, CTL) in zip(sides, CheckSide, RightSide,BackSide,LeftSide, CheckTopFront, CheckTopRight, CheckTopBack, CheckTopLeft):
                if not (Solve.check(self.Front[1]) and (Solve.check(self.Right[1])) and (Solve.check(self.Left[1])) and (Solve.check(self.Back[1]))):
                    i = i + 1
                    Top = self.Top.copy()
                    Front = self.Front.copy()
                    Right = self.Right.copy()
                    Left = self.Left.copy()
                    Back = self.Back.copy()
                    Bottom = self.Bottom.copy()
                    moves_out = self.moves_out
                    if Top[CTF] != 'y' and eval(eval(f'CS'))[0,1] != 'y':
                        if eval(eval(f'CS'))[0,1] == eval(eval(f'CS'))[1,1]:
                            if Top[CTF] == eval(eval(f'LS'))[1,1]:
                                Top = self.Top.copy()
                                Front = self.Front.copy()
                                Right = self.Right.copy()
                                Left = self.Left.copy()
                                Back = self.Back.copy()
                                Bottom = self.Bottom.copy()
                                moves_out = self.moves_out
                                Moves.move(self,"ccw", "Top")
                                Moves.LeftAlgorithmFlip(self,  eval(f'LS'))
                                Moves.RightAlgorithmFlip(self,  eval(f'CS'))
                            if Top[CTF] == eval(eval(f'RS'))[1, 1]:
                                Top = self.Top.copy()
                                Front = self.Front.copy()
                                Right = self.Right.copy()
                                Back = self.Back.copy()
                                Left = self.Left.copy()
                                Bottom = self.Bottom.copy()
                                moves_out = self.moves_out
                                Moves.move(self, "cw", "Top")
                                Moves.RightAlgorithmFlip(self, eval(f'RS'))
                                Moves.LeftAlgorithmFlip(self, eval(f'CS'))
                            i = 0
                        else:
                            Top = self.Top.copy()
                            Front = self.Front.copy()
                            Right = self.Right.copy()
                            Back = self.Back.copy()
                            Left = self.Left.copy()
                            Bottom = self.Bottom.copy()
                            moves_out = self.moves_out
                            while not ((eval(eval(f'CS'))[0, 1] == eval(eval(f'CS'))[1, 1] and ((Top[CTF] == (eval(eval(f'RS'))[1, 1])) or (Top[CTF] == eval(eval(f'LS'))[1, 1]))) or (
                                    eval(eval(f'RS'))[0, 1] == eval(eval(f'RS'))[1, 1] and ((Top[CTR] == (eval(eval(f'CS'))[1, 1])) or ((Top[CTR] == eval(eval(f'BS'))[1, 1])))) or (
                                    eval(eval(f'BS'))[0, 1] == eval(eval(f'BS'))[1, 1] and ((Top[CTB] == (eval(eval(f'RS'))[1, 1])) or ((Top[CTB] == eval(eval(f'LS'))[1, 1])))) or (
                                    eval(eval(f'LS'))[0, 1] == eval(eval(f'LS'))[1, 1] and ((Top[CTL] == (eval(eval(f'BS'))[1, 1]) or ((Top[CTL] == eval(eval(f'CS'))[1, 1])))))):
                                Moves.move(self, "cw", "Top")
                                Top = self.Top.copy()
                                Front = self.Front.copy()
                                Right = self.Right.copy()
                                Back = self.Back.copy()
                                Left = self.Left.copy()
                                Bottom = self.Bottom.copy()
                                moves_out = self.moves_out
                        i = 0

                    elif i>5:

                        if (eval(eval(f'CS'))[1,0] != eval(eval(f'LS'))[1,1]) or (eval(eval(f'CS'))[1,1] != eval(eval(f'RS'))[0,1]):
                            if eval(eval(f'CS'))[1,1] != eval(eval(f'RS'))[0,1]:
                                Top = self.Top.copy()
                                Front = self.Front.copy()
                                Right = self.Right.copy()
                                Back = self.Back.copy()
                                Left = self.Left.copy()
                                Bottom = self.Bottom.copy()
                                moves_out = self.moves_out
                                Moves.move(self, "cw", "Top")
                                Moves.RightAlgorithmFlip(self, eval(f'RS'))
                                Moves.LeftAlgorithmFlip(self, eval(f'CS'))
                                i = 0
                            elif eval(eval(f'CS'))[1,1] != eval(eval(f'LS'))[1,2]:
                                Top = self.Top.copy()
                                Front = self.Front.copy()
                                Right = self.Right.copy()
                                Back = self.Back.copy()
                                Left = self.Left.copy()
                                Bottom = self.Bottom.copy()
                                moves_out = self.moves_out
                                Moves.move(self, "ccw", "Top")
                                Moves.LeftAlgorithmFlip(self, eval(f'LS'))
                                Moves.RightAlgorithmFlip(self, eval(f'CS'))
                                i = 0
        Top = self.Top.copy()
        Front = self.Front.copy()
        Right = self.Right.copy()
        Left = self.Left.copy()
        Back = self.Back.copy()
        Bottom = self.Bottom.copy()
        moves_out = self.moves_out

    def YellowCross(self):
        Top = self.Top.copy()
        Front = self.Front.copy()
        Right = self.Right.copy()
        Left = self.Left.copy()
        Back = self.Back.copy()
        Bottom = self.Bottom.copy()
        moves_out = self.moves_out
        Flip = 'yes'
        self.Flip = 'yes'


        if not (Top[1, 1] == 'y' and Top[1, 2] == 'y' and Top[2, 1] == 'y' and Top[1, 0] == 'y' and Top[0, 1] == 'y'):
            if (Top[1, 1] == 'y' and Top[1, 2] != 'y' and Top[2, 1] != 'y' and Top[1, 0] != 'y' and Top[0, 1] != 'y'):
                Moves.move(self, "cw", 'Front')
                Moves.RightAlgorithmFlip(self, 'Right')
                Moves.move(self, "ccw", 'Front')

            if (Solve.check(Top[:,1]) or Solve.check(Top[1])):
                if Solve.check(Top[1]):
                    Moves.move(self, "cw", 'Front')
                    Moves.RightAlgorithmFlip(self, 'Right')
                    Moves.move(self, "ccw", 'Front')
                else:
                    Moves.move(self, "cw", 'Right')
                    Moves.RightAlgorithmFlip(self, 'Back')
                    Moves.move(self, "ccw", 'Right')

            Top = self.Top.copy()
            Front = self.Front.copy()
            Right = self.Right.copy()
            Left = self.Left.copy()
            Back = self.Back.copy()
            Bottom = self.Bottom.copy()
            moves_out = self.moves_out
            if not (Top[1, 1] == 'y' and Top[1, 2] == 'y' and Top[2, 1] == 'y' and Top[1, 0] == 'y' and Top[0, 1] == 'y'):

                if (Top[1,1] =='y' and Top[1,2] =='y' and Top[2,1] =='y'): #Bottom Right
                    Moves.move(self, "cw", "Back")
                    #Right Alg from top
                    Moves.move(self, "cw", 'Top')
                    Moves.move(self, "cw", 'Left')
                    Moves.move(self, "ccw", 'Top')
                    Moves.move(self, "ccw", 'Left')

                    Moves.move(self, "ccw", "Back")

                elif Top[1,1] =='y' and Top[1,2] =='y' and Top[0,1] =='y': #Top Right
                    Moves.move(self, "cw", "Left")

                    Moves.move(self, "cw", 'Top')
                    Moves.move(self, "cw", 'Front')
                    Moves.move(self, "ccw", 'Top')
                    Moves.move(self, "ccw", 'Front')

                    Moves.move(self, "ccw", "Left")

                elif (Top[1, 1] == 'y' and Top[1, 0] == 'y' and Top[0, 1] == 'y'): #Top Left
                    Moves.move(self, "cw", "Front")

                    Moves.move(self, "cw", 'Top')
                    Moves.move(self, "cw", 'Right')
                    Moves.move(self, "ccw", 'Top')
                    Moves.move(self, "ccw", 'Right')

                    Moves.move(self, "ccw", "Front")
                elif (Top[1, 1] == 'y' and Top[1, 0] == 'y' and Top[2, 1] == 'y'): #Bottom Left
                    Moves.move(self, "cw", "Right")

                    Moves.move(self, "cw", 'Top')
                    Moves.move(self, "cw", 'Back')
                    Moves.move(self, "ccw", 'Top')
                    Moves.move(self, "ccw", 'Back')

                    Moves.move(self, "ccw", "Right")


    def FinishCorners(self):
        Top = self.Top.copy()
        Front = self.Front.copy()
        Right = self.Right.copy()
        Left = self.Left.copy()
        Back = self.Back.copy()
        Bottom = self.Bottom.copy()
        moves_out = self.moves_out
        Flip = 'yes'
        self.Flip = 'yes'
        TFL = [self.Top[2, 0], self.Front[0, 0], self.Left[0, 2]]  # REPRESENT ACTUAL CORNERS
        TFR = [self.Top[2, 2], self.Front[0, 2], self.Right[0, 0]]
        TBL = [self.Top[0, 0], self.Back[0, 2], self.Left[0, 0]]
        TBR = [self.Top[0, 2], self.Back[0, 0], self.Right[0, 2]]
        #Only check for adjacent orange because im lazy
        if ('o' in TFR and 'o' in TBR):
            Moves.move(self, "cw", 'Top')
        elif ('o' in TBL and 'o' in TBR):
            Moves.move(self, "cw", 'Top')
            Moves.move(self, "cw", 'Top')
        elif ('o' in TBL and 'o' in TFL):
            Moves.move(self, "ccw", 'Top')
        else:
            TFL = [self.Top[2, 0], self.Front[0, 0], self.Left[0, 2]]
            while 'o' not in TFL:
                Moves.move(self, "ccw", 'Top')
                TFL = [self.Top[2, 0], self.Front[0, 0], self.Left[0, 2]]
        TFL = [self.Top[2, 0], self.Front[0, 0], self.Left[0, 2]]  # REPRESENT ACTUAL CORNERS
        TFR = [self.Top[2, 2], self.Front[0, 2], self.Right[0, 0]]
        TBL = [self.Top[0, 0], self.Back[0, 2], self.Left[0, 0]]
        TBR = [self.Top[0, 2], self.Back[0, 0], self.Right[0, 2]]
        if 'o' in TFL and 'b' in TFL:
            Moves.RightAlgorithmFlip(self, 'Front')
            Moves.RightAlgorithmFlip(self, 'Front')
            Moves.RightAlgorithmFlip(self, 'Front')
            Moves.LeftAlgorithmFlip(self, "Left")
            Moves.LeftAlgorithmFlip(self, "Left")
            Moves.LeftAlgorithmFlip(self, "Left")
            Moves.move(self, "ccw", 'Top')
        TFL = [self.Top[2, 0], self.Front[0, 0], self.Left[0, 2]]  # REPRESENT ACTUAL CORNERS
        TFR = [self.Top[2, 2], self.Front[0, 2], self.Right[0, 0]]
        TBL = [self.Top[0, 0], self.Back[0, 2], self.Left[0, 0]]
        TBR = [self.Top[0, 2], self.Back[0, 0], self.Right[0, 2]]
        if 'o' in TBL:
            if 'o' in TBL and 'b' in TBL:
                Moves.RightAlgorithmFlip(self, 'Left')
                Moves.RightAlgorithmFlip(self, 'Left')
                Moves.RightAlgorithmFlip(self, 'Left')
                Moves.LeftAlgorithmFlip(self, "Back")
                Moves.LeftAlgorithmFlip(self, "Back")
                Moves.LeftAlgorithmFlip(self, "Back")
                Moves.move(self, "ccw", 'Top')
        TFL = [self.Top[2, 0], self.Front[0, 0], self.Left[0, 2]]  # REPRESENT ACTUAL CORNERS
        TFR = [self.Top[2, 2], self.Front[0, 2], self.Right[0, 0]]
        TBL = [self.Top[0, 0], self.Back[0, 2], self.Left[0, 0]]
        TBR = [self.Top[0, 2], self.Back[0, 0], self.Right[0, 2]]
        if 'o' in TBR:
            if 'o' in TBR and 'b' in TBR:
                Moves.RightAlgorithmFlip(self, 'Right')
                Moves.RightAlgorithmFlip(self, 'Right')
                Moves.RightAlgorithmFlip(self, 'Right')
                Moves.LeftAlgorithmFlip(self, "Front")
                Moves.LeftAlgorithmFlip(self, "Front")
                Moves.LeftAlgorithmFlip(self, "Front")
                Moves.move(self, "ccw", 'Top')
        TFL = [self.Top[2, 0], self.Front[0, 0], self.Left[0, 2]]  # REPRESENT ACTUAL CORNERS
        TFR = [self.Top[2, 2], self.Front[0, 2], self.Right[0, 0]]
        TBL = [self.Top[0, 0], self.Back[0, 2], self.Left[0, 0]]
        TBR = [self.Top[0, 2], self.Back[0, 0], self.Right[0, 2]]
        if 'b' in TBL:
            Moves.RightAlgorithmFlip(self, 'Back')
            Moves.RightAlgorithmFlip(self, 'Back')
            Moves.RightAlgorithmFlip(self, 'Back')
            Moves.LeftAlgorithmFlip(self, "Right")
            Moves.LeftAlgorithmFlip(self, "Right")
            Moves.LeftAlgorithmFlip(self, "Right")
            Moves.move(self, "ccw", 'Top')
        TFL = [self.Top[2, 0], self.Front[0, 0], self.Left[0, 2]]  # REPRESENT ACTUAL CORNERS
        TFR = [self.Top[2, 2], self.Front[0, 2], self.Right[0, 0]]
        TBL = [self.Top[0, 0], self.Back[0, 2], self.Left[0, 0]]
        TBR = [self.Top[0, 2], self.Back[0, 0], self.Right[0, 2]]
        if 'b' in TFL and 'b' in TFR:
            Moves.move(self, "ccw", 'Top')
            TFL = [self.Top[2, 0], self.Front[0, 0], self.Left[0, 2]]  # REPRESENT ACTUAL CORNERS
            TFR = [self.Top[2, 2], self.Front[0, 2], self.Right[0, 0]]
            TBL = [self.Top[0, 0], self.Back[0, 2], self.Left[0, 0]]
            TBR = [self.Top[0, 2], self.Back[0, 0], self.Right[0, 2]]
            if 'o' in TBR:
                Moves.RightAlgorithmFlip(self, 'Right')
                Moves.RightAlgorithmFlip(self, 'Right')
                Moves.RightAlgorithmFlip(self, 'Right')
                Moves.LeftAlgorithmFlip(self, "Front")
                Moves.LeftAlgorithmFlip(self, "Front")
                Moves.LeftAlgorithmFlip(self, "Front")
                Moves.move(self, "ccw", 'Top')
        TFL = [self.Top[2, 0], self.Front[0, 0], self.Left[0, 2]]  # REPRESENT ACTUAL CORNERS
        TFR = [self.Top[2, 2], self.Front[0, 2], self.Right[0, 0]]
        TBL = [self.Top[0, 0], self.Back[0, 2], self.Left[0, 0]]
        TBR = [self.Top[0, 2], self.Back[0, 0], self.Right[0, 2]]
        if 'o' in TBL:
            Moves.RightAlgorithmFlip(self, 'Left')
            Moves.RightAlgorithmFlip(self, 'Left')
            Moves.RightAlgorithmFlip(self, 'Left')
            Moves.LeftAlgorithmFlip(self, "Back")
            Moves.LeftAlgorithmFlip(self, "Back")
            Moves.LeftAlgorithmFlip(self, "Back")
            Moves.move(self, "ccw", 'Top')

        while not Solve.check(self.Top):
            if self.Top[2,0] != 'y':
                while self.Top[2,0] != 'y':
                    Moves.RightAlgorithm(self, 'Left')
                Moves.move(self, "ccw", 'Top')
            else:
                Moves.move(self, "ccw", 'Top')
            Top = self.Top.copy()
            Front = self.Front.copy()
            Right = self.Right.copy()
            Left = self.Left.copy()
            Back = self.Back.copy()
            Bottom = self.Bottom.copy()
            moves_out = self.moves_out
        Moves.move(self, "ccw", 'Top')
    def FinishCube(self):

        Top = self.Top.copy()
        Front = self.Front.copy()
        Right = self.Right.copy()
        Left = self.Left.copy()
        Back = self.Back.copy()
        Bottom = self.Bottom.copy()
        moves_out = self.moves_out
        Flip = 'yes'
        self.Flip = 'yes'
        TFL = [self.Top[2, 0], self.Front[0, 0], self.Left[0, 2]]  # REPRESENT ACTUAL CORNERS
        TFR = [self.Top[2, 2], self.Front[0, 2], self.Right[0, 0]]
        TBL = [self.Top[0, 0], self.Back[0, 2], self.Left[0, 0]]
        TBR = [self.Top[0, 2], self.Back[0, 0], self.Right[0, 2]]
        while Front[0,0] !='o' and Front[0,2] !='o':
            Moves.move(self, "ccw", 'Top')
            Top = self.Top.copy()
            Front = self.Front.copy()
            Right = self.Right.copy()
            Left = self.Left.copy()
            Back = self.Back.copy()
            Bottom = self.Bottom.copy()
            moves_out = self.moves_out
        CheckSide = ['Front', 'Right', 'Back', 'Left']
        RightSide = ['Right', 'Back', 'Left', 'Front']  # Right side in relation to checkside
        BackSide = ['Back', 'Left', 'Front', 'Right']
        LeftSide = ['Left', 'Front', 'Right', 'Back']
        sides = [self.Front, self.Right, self.Back, self.Left]
        for (side, CS, RS, BS, LS) in zip(sides, CheckSide, RightSide,BackSide,LeftSide):
            if not (Solve.check(Front) and Solve.check(Left) and Solve.check(Back) and Solve.check(Right)):
                if Solve.check(eval(eval(f'CS'))[0]):
                    while not (Solve.check(Front) and Solve.check(Left) and Solve.check(Back) and Solve.check(Right)):
                        if eval(eval(f'LS'))[0,1] == eval(eval(f'RS'))[1,1]:
                            Moves.RightAlgorithmFlip(self, eval(f'RS'))
                            Moves.LeftAlgorithmFlip(self, eval(f'LS'))
                            Moves.RightAlgorithmFlip(self, eval(f'RS'))
                            Moves.RightAlgorithmFlip(self, eval(f'RS'))
                            Moves.RightAlgorithmFlip(self, eval(f'RS'))
                            Moves.RightAlgorithmFlip(self, eval(f'RS'))
                            Moves.RightAlgorithmFlip(self, eval(f'RS'))
                            Moves.LeftAlgorithmFlip(self, eval(f'LS'))
                            Moves.LeftAlgorithmFlip(self, eval(f'LS'))
                            Moves.LeftAlgorithmFlip(self, eval(f'LS'))
                            Moves.LeftAlgorithmFlip(self, eval(f'LS'))
                            Moves.LeftAlgorithmFlip(self, eval(f'LS'))
                        if eval(eval(f'LS'))[0,1] == eval(eval(f'BS'))[1,1]:
                            Moves.LeftAlgorithmFlip(self, eval(f'LS'))
                            Moves.RightAlgorithmFlip(self, eval(f'RS'))
                            Moves.LeftAlgorithmFlip(self, eval(f'LS'))
                            Moves.LeftAlgorithmFlip(self, eval(f'LS'))
                            Moves.LeftAlgorithmFlip(self, eval(f'LS'))
                            Moves.LeftAlgorithmFlip(self, eval(f'LS'))
                            Moves.LeftAlgorithmFlip(self, eval(f'LS'))
                            Moves.RightAlgorithmFlip(self, eval(f'RS'))
                            Moves.RightAlgorithmFlip(self, eval(f'RS'))
                            Moves.RightAlgorithmFlip(self, eval(f'RS'))
                            Moves.RightAlgorithmFlip(self, eval(f'RS'))
                            Moves.RightAlgorithmFlip(self, eval(f'RS'))
                        else:
                            Moves.RightAlgorithmFlip(self, eval(f'RS'))
                            Moves.LeftAlgorithmFlip(self, eval(f'LS'))
                            Moves.RightAlgorithmFlip(self, eval(f'RS'))
                            Moves.RightAlgorithmFlip(self, eval(f'RS'))
                            Moves.RightAlgorithmFlip(self, eval(f'RS'))
                            Moves.RightAlgorithmFlip(self, eval(f'RS'))
                            Moves.RightAlgorithmFlip(self, eval(f'RS'))
                            Moves.LeftAlgorithmFlip(self, eval(f'LS'))
                            Moves.LeftAlgorithmFlip(self, eval(f'LS'))
                            Moves.LeftAlgorithmFlip(self, eval(f'LS'))
                            Moves.LeftAlgorithmFlip(self, eval(f'LS'))
                            Moves.LeftAlgorithmFlip(self, eval(f'LS'))
                        Top = self.Top
                        Front = self.Front
                        Right = self.Right
                        Left = self.Left
                        Back = self.Back
                        Bottom = self.Bottom
                        moves_out = self.moves_out

    def Test(self):

        Top = self.Top.copy()
        Front = self.Front.copy()
        Right = self.Right.copy()
        Left = self.Left.copy()
        Back = self.Back.copy()
        Bottom = self.Bottom.copy()
        moves_out = self.moves_out
        Flip = 'yes'
        self.Flip = 'yes'
        Moves.LeftAlgorithmFlip(self, 'Front')
        Top = self.Top
        Front = self.Front
        Right = self.Right
        Left = self.Left
        Back = self.Back
        Bottom = self.Bottom
        moves_out = self.moves_out





#Solve in SW, Outputs Hardware Moves List
    def SWSolve(self):
        #Solve.Test(self)
        Solve.WhiteMoveBot(self)
        print('WhiteMoveBotdone')
        Solve.WhiteMoveSides(self)
        print('WhiteMoveSides')
        Solve.WhiteCorners(self)
        print('WhiteCorners')
        Solve.SolveLayerTwo(self)
        print('SolveLayerTwo')
        Solve.YellowCross(self)
        print('YellowCross')
        Solve.FinishCorners(self)
        print('FinishCorners')
        Solve.FinishCube(self)



#Detect colors of Cube & Output Physical HW Moves
    def HW_output(self, moves_out):
        #moves_out = self.moves_out
        n_moves = 0
        self.hw_moves = []
        hw_moves = self.hw_moves
        for move in self.moves_out:
            n_moves = n_moves+1
            #print(move)
            #move = eval(move)
            #eval('HWmoves.' + f'{move}'+'(self)')
            #print('HWmoves.' + f'{move}'+'(self)')
            moves_out.append(f'{move}'+'()')

#        for move in moves_out:
#            eval(f'move')
#            #sleep(.5)
#            print(eval(f'move'))


    def HWSolve(self):
        Solve.HW_output(self, moves_out)



Solve.SWSolve(FullCube) #FIX INPUT ISSUES
Solve.HWSolve(FullCube)  ,
for move in FullCube.moves_out:
    #sleep(0.1)
    #print(f'{move}'+'()')
    eval(f'{move}'+'()')
    #sleep(0.1)


#for idx, i in np.ndenumerate(self.Top.copy(), self.Front(), self.Right.copy(), self.Left.copy(), self.Back.copy()):
    #Output Moves for Motors

GPIO.output(RESET_BACK, GPIO.HIGH)
GPIO.output(RESET_BOT, GPIO.HIGH)
GPIO.output(RESET_T, GPIO.HIGH)
GPIO.output(RESET_F, GPIO.HIGH)
GPIO.output(RESET_R, GPIO.HIGH)
GPIO.output(RESET_L, GPIO.HIGH)




#print(FullCube.Top[1,2])

#Moves.RightAlgorithm(FullCube, 'Right')

#FullCube = Cube(Top, Front, Right, Left, Back, Bottom,dict)



Right = FullCube.Right
Left = FullCube.Left
Top = FullCube.Top
Bottom = FullCube.Bottom
Front = FullCube.Front
Back = FullCube.Back

#Adjust Output to accurately map positions
Top = np.rot90(Top, 1, axes= (1,0)); #rotate ccw
Bottom = np.rot90(Bottom, 1, axes= (0,1)); #rotate cw

#Flatten Individual Arrays
RightFlat = np.ravel(Right)
LeftFlat = np.ravel(Left)
FrontFlat = np.ravel(Front)
BackFlat = np.ravel(Back)
TopFlat = np.ravel(Top)
BottomFlat = np.ravel(Bottom)

FullCubeFlat = np.transpose(np.vstack((RightFlat, TopFlat, BackFlat, BottomFlat, FrontFlat, LeftFlat)))
print(FullCubeFlat)

#Adjust Output to accurately map positions



#Adjust Output for Input into Cube Simulator
DFCube = pd.DataFrame(FullCubeFlat, index = [1, 2, 3, 4, 5, 6, 7, 8, 9], columns=['w', 'r', 'g', 'o', 'b', 'y' ])
face = "wrgoby"
StringCube = DFCube.copy()
for i, v in enumerate(face):
    print(v)
    StringCube[v] = StringCube[v].replace({1: 'w'})
    StringCube[v] = StringCube[v].replace({2: 'b'})
    StringCube[v] = StringCube[v].replace({3: 'r'})
    StringCube[v] = StringCube[v].replace({4: 'g'})
    StringCube[v] = StringCube[v].replace({5: 'o'})
    StringCube[v] = StringCube[v].replace({6: 'y'})
print(StringCube)

#DFCube['w'] = DFCube['DFCube'].replace({'1':'w', '2':'b', '3':'r', '4':'g', '5':'o', '6':'y', })
#Almost done, just have to figure out how to add index to each row
for i in range(1,10):
    k=i-1
    print(StringCube.iloc[[k]])
    StringCube.iloc[k] = StringCube.iloc[k] + f'{i}'

print(StringCube)
#output.save(StringCube)
print("This code took", process_time(),"s to execute")



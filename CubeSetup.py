import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import *
import json
import pandas as pd
import itertools


#Define Colors
w = "w"
b = "b"
r = "r"
g = "g"
o = "o"
y = "y"
#"""
#Store Test Configs
Top = np.arange(9).reshape(3, 3)

Right = np.arange(9).reshape(3, 3)

Left = np.arange(9).reshape(3, 3)

Front = np.arange(9).reshape(3, 3)

Back = np.arange(9).reshape(3, 3)

Bottom = np.arange(9).reshape(3, 3)
#"""

"""
Top = array([
    [i, i, i] ,
    [i, i, i] ,
    [i, i, i]
])

Right = array([
    [g, g, o] ,
    [b, g, w] ,
    [b, r, w]
])

Left = array([
    [y, b, r] ,
    [y, b, b] ,
    [y, o, o]
])

Front = array([
    [b, g, o] ,
    [o, o, y] ,
    [g, g, y]
])

Back = array([
    [w, r, r] ,
    [r, r, r] ,
    [r, o, r]
])

Bottom = array([
    [y, y, o] ,
    [w, y, g] ,
    [g, y, g]
])
"""
StartCube = array([
    [Top],
    [Right],
    [Left],
    [Front],
    [Back],
    [Bottom]
])

moves_out = []
"""
TopCW = np.rot90(Top, 1, axes=(1, 0))
RightCW = np.rot90(Right, 1, axes=(1, 0))
LeftCW = np.rot90(Left, 1, axes=(1, 0))
FrontCW = np.rot90(Front, 1, axes=(1, 0))
BackCW = np.rot90(Back, 1, axes=(1, 0))
BottomCW = np.rot90(Bottom, 1, axes=(1, 0))

print(Back)
Bottom[:,[2,2]] = Front[:,[0,2]] #Swaps Right Columns
Back[:,[0,0]] = (np.rot90(Top, 2, axes=(0, 1))[:,[0,0]])#Swaps Left Columns
Top[:,[2,2]] = Front[:,[0,2]]
print(Top)
"""
class Cube():
    def __init__(self, Top, Front, Right, Left, Back, Bottom, moves_out, data: dict ):
        self.Top = Top
        self.Front = Front
        self.Right = Right
        self.Left = Left
        self.Back = Back
        self.Bottom = Bottom
        self.side1 = np.arange(9).reshape(3, 3)
        self.side2 = np.arange(9).reshape(3, 3)
        self.side3 = np.arange(9).reshape(3, 3)
        self.side4 = np.arange(9).reshape(3, 3)
        self.side5 = np.arange(9).reshape(3, 3)
        self.side6 = np.arange(9).reshape(3, 3)
        self.moves_out = moves_out


    def Right(self, Top, Front, Right, Left, Back, Bottom):
        self.side1 = self.Right
        self.side2 = self.Back
        self.side3 = self.Front
        self.side4 = self.Top
        self.side5 = self.Bottom
        self.side6 = self.Left

    def Left(self, Top, Front, Right, Left, Back, Bottom):
        self.side1 = self.Left
        self.side2 = self.Front
        self.side3 = self.Back
        self.side4 = self.Top
        self.side5 = self.Bottom
        self.side6 = self.Right

class Moves(Cube):

    def __init__(self):
        self.side1o = np.arange(12).reshape(3, 3)
        self.side2o = np.arange(12).reshape(3, 3)
        self.side3o= np.arange(12).reshape(3, 3)
        self.side4o = np.arange(12).reshape(3, 3)
        self.side5o = np.arange(12).reshape(3, 3)

    def move(self, dir, rotationside):
        if rotationside == 'Front' or rotationside == 'Right' or rotationside == 'Left' or rotationside == 'Back':
            if (rotationside == 'Right'): #Done
                self.side1 = self.Right.copy()
                self.side2 = self.Back
                self.side2o = np.rot90(self.Back.copy(), 2 , axes=(0,1))
                self.side3 = self.Front
                self.side3o = self.Front.copy()
                self.side4 = self.Top
                self.side4o = np.rot90(self.Top.copy(), 2 , axes=(0,1))
                self.side5 = self.Bottom
                self.side5o =self.Bottom.copy()
                self.side6 = self.Left

            if (rotationside == 'Left'): #Done
                self.side1 = self.Left.copy()
                self.side2 = self.Front
                self.side2o = np.rot90(self.Front.copy(), 2, axes=(0, 1))
                self.side3 = self.Back
                self.side3o = self.Back.copy()
                self.side4 = np.rot90(self.Top, 2 , axes=(0,1))
                self.side4o = self.Top.copy()
                self.side5 = np.rot90(self.Bottom, 2 , axes=(0,1))
                self.side5o = np.rot90(self.Bottom.copy(), 2, axes=(0, 1))
                self.side6 = self.Right
            if (rotationside == 'Back'): #Done
                self.side1 = self.Back.copy()
                self.side2 = self.Left
                self.side2o = np.flip(self.Left.copy())
                self.side3 = self.Right
                self.side3o = self.Right.copy()
                self.side4 = np.rot90(self.Top, 1, axes=(1, 0))
                self.side4o = np.rot90(np.flip(self.Top.copy()),1, axes=(1, 0) )
                self.side5 = np.rot90(np.flip(self.Bottom.copy()),1, axes=(1, 0) )
                self.side5o = np.rot90(np.flip(self.Bottom.copy()),1, axes=(1, 0) )
                self.side6 = self.Front
            if (rotationside == 'Front'): #Done
                self.side1 = self.Front.copy()
                self.side2 = self.Right
                self.side2o = np.flip(self.Right.copy())
                self.side3 = self.Left
                self.side3o = self.Left.copy()
                self.side4 = np.rot90(self.Top, 1, axes=(0, 1))
                self.side4o = np.rot90(np.flip(self.Top.copy()),1, axes=(0, 1) )
                self.side5 = np.rot90(np.flip(self.Bottom.copy()),1, axes=(0, 1) )
                self.side5o = np.rot90(np.flip(self.Bottom.copy()),1, axes=(0, 1) )
                self.side6 = self.Back
            if (dir == "cw"):
                self.side1 = np.rot90(self.side1, 1, axes=(1, 0))
                self.side2[:,[0]] = self.side4o[:,[0]] #side to right of rotation side (Done)
                self.side3[:,[2,2]] = self.side5o[:,[0,2]]   #side to left of rotation side (Done)
                self.side4[:,[2,2]] = self.side3o[:,[0,2]]  #side Above(Top) of rotation side (Done)
                self.side5[:,[2,2]] = self.side2o[:,[0,2]]   #side Below(Bottom) of rotation side (Done) #HAVE TO FINISH DEFINING SIDES  AND OUTPUTS (ROTATING TOP AND BOTTOM TO MATCH ALL CASES
            if (dir == "ccw"):
                self.side1 = np.rot90(self.side1, 1, axes=(0, 1))
                self.side2[:, [0, 0]] = np.rot90(self.side5o, 2, axes=(1, 0) )[:, [1, 0]]  # side to right of rotation side (Done)
                self.side3[:, [2, 2]] = np.rot90(self.side4o, 2, axes=(1, 0) )[:, [0, 2]]  # side to left of rotation side (Done)
                self.side4[:, [2, 2]] = self.side2o[:, [0, 2]]  # side Above(Top) of rotation side (Done)
                self.side5[:, [2, 2]] = self.side3o[:, [0, 2]]  # side Below(Bottom) of rotation side (Done) #HAVE TO FINISH DEFINING SIDES  AND OUTPUTS (ROTATING TOP AND BOTTOM TO MATCH ALL CASES

        if (rotationside == 'Top' or 'Bottom'):  #Orientation of cw in reference to side being turned only
            if (rotationside == 'Top'): #Done for both dir
                    if (dir == "cw"): self.side1 = np.rot90(self.Top.copy(), 1, axes=(1, 0))
                    if (dir == "ccw"): self.side1 = np.rot90(self.Top.copy(), 1, axes=(0, 1))
                    self.side2 = self.Right.copy()
                    self.side2o = self.Right.copy()
                    self.side3 = self.Left.copy()
                    self.side3o = self.Left.copy()
                    self.side4 = self.Back.copy()
                    self.side4o = self.Back.copy()
                    self.side5 = self.Front.copy()
                    self.side5o = self.Front.copy()
                    self.side6 = self.Bottom

            if (rotationside == 'Bottom'): #Done for both dir
                if (dir == "cw"): self.side1 = np.rot90(self.Bottom.copy(), 1, axes=(1, 0))
                if (dir == "ccw"): self.side1 = np.rot90(self.Bottom.copy(), 1, axes=(0, 1))
                self.side2 = self.Right.copy()
                self.side2o = self.Right.copy()
                self.side3 = self.Left.copy()
                self.side3o = self.Left.copy()
                self.side4 = self.Back.copy()
                self.side4o = self.Back.copy()
                self.side5 = self.Front.copy()
                self.side5o = self.Front.copy()
                self.side6 = self.Top

            if rotationside == 'Top': i = 0
            if rotationside == 'Bottom': i = 2
            if (dir == "cw" and rotationside == 'Top') or (dir == "ccw" and rotationside == 'Bottom'): # Works but slow
                self.side2[[i]] = self.side4o[[i]]  # Right side (OUTPUTS)
                self.side3[[i]] = self.side5o[[i]]  # Left side
                self.side4[[i]] = self.side3o[[i]]  # Back side
                self.side5[[i]] = self.side2o[[i]]  # Front side
            if (dir == "cw" and rotationside == 'Bottom') or (dir == "ccw" and rotationside == 'Top'):
                self.side2[[i]] = self.side5o[[i]]  # Right side (OUTPUTS)
                self.side3[[i]] = self.side4o[[i]]  # Left side
                self.side4[[i]] = self.side2o[[i]]  # Back side
                self.side5[[i]] = self.side3o[[i]]  # Front side
        #Setup Outputs to match cube
        if (rotationside == 'Right'): #DONE
            self.Right = self.side1
            self.Back = self.side2
            self.Front = self.side3
            self.Top = self.side4
            self.Bottom = self.side5
            self.Left = self.side6

        if (rotationside == 'Left'): #DONE
                self.Left = self.side1
                self.Front = self.side2
                self.Back = self.side3
                self.Top = np.rot90(self.side4, 2, axes=(0, 1))
                self.Bottom = np.rot90(self.side5, 2, axes=(0, 1))
                self.Right = self.side6

        if (rotationside == 'Back'): #DONE
                self.Back = self.side1
                self.Left = self.side2
                self.Right = self.side3
                self.Top = np.rot90(self.side4, 1, axes=(0, 1))
                self.Bottom = np.rot90(self.side5, 1, axes=(1, 0))
                self.Front = self.side6

        if (rotationside == 'Front'): #DONE
                self.Front = self.side1
                self.Right = self.side2
                self.Left = self.side3
                self.Top = np.rot90(self.side4, 1, axes=(1, 0))
                self.Bottom = np.rot90(self.side5, 1, axes=(0, 1))
                self.Back = self.side6

        if (rotationside == 'Top'):  # DONE
            self.Top = self.side1
            self.Right = self.side2
            self.Left = self.side3
            self.Back = self.side4
            self.Front = self.side5
            self.Bottom = self.side6

        if (rotationside == 'Bottom'):  # DONE
            self.Bottom = self.side1
            self.Right = self.side2
            self.Left = self.side3
            self.Back = self.side4
            self.Front = self.side5
            self.Top = self.side6
        #moves_out = self.moves_out.copy
        #activemove = f'{rotationside}_{dir}'
        self.moves_out.append(f'{rotationside}_{dir}')
        #self.moves_out = moves_out
        # Adjust Output to accurately map positions
        #self.Top = np.rot90(self.Top.copy(), 1, axes=(1, 0));  # rotate ccw
        #self.Bottom = np.rot90(self.Bottom.copy(), 1, axes=(0, 1));  # rotate cw
        FullCube = Cube(self.Top, self.Front, self.Right, self.Left, self.Back, self.Bottom, self.moves_out, dict)
    def RightAlgorithm(self, rotationside): #Based on upside down cube bc white is top
        Moves.move(self, "cw", rotationside)
        Moves.move(self, "cw", 'Bottom')
        Moves.move(self, "ccw", rotationside)
        Moves.move(self, "ccw", 'Bottom')

    #def LeftAlgorithm(self, rotationside): ##Fix NOWWWWWWWWW
 #      Moves.move(FullCube, "cw", rotationside)
 ##       Moves.move(FullCube, "ccw", 'Bottom')
  #      Moves.move(FullCube, "ccw", rotationside)
  #      Moves.move(FullCube, "cw", 'Bottom')

    def RightAlgorithmFlip(self, rotationside): #After Cube has been flipped (yellow on top)
        Moves.move(self, "cw", rotationside)
        Moves.move(self, "cw", 'Top')
        Moves.move(self, "ccw", rotationside)
        Moves.move(self, "ccw", 'Top')

    def LeftAlgorithmFlip(self, rotationside): #After Cube has been flipped (yellow on top)
        Moves.move(self, "ccw", rotationside)
        Moves.move(self, "ccw", 'Top')
        Moves.move(self, "cw", rotationside)
        Moves.move(self, "cw", 'Top')


class output():
    def __init__(self, data: dict):
        """
        Constructor method to generate the initial cube variables.
        :param data: loads the cube data from the json file with the latest saved state.
        """
        self.dcube = pd.DataFrame(data)

 #   @staticmethod
 #   def save(dcube: pd.DataFrame):
#        """
 #       Saves the state of the cube in a json file.
#        :param dcube: Dataframe with the data of the state of the cube.
 #       :return: None.
 #       """
 #       data = dcube.to_dict('list')
#        with open('data/cube_saved.json', 'w') as f:
#            json.dump(data, f, indent=4)
FullCube = Cube(Top, Front, Right, Left, Back, Bottom, moves_out, dict)


#For Testing Alg Purposes only
#Moves.move(FullCube, "ccw", 'Top')
#Moves.RightAlgorithm(FullCube, 'Right')

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



"""
#FullCube = Cube(FullCube)
FullCubeN = Moves.cwmove(FullCube, Right)
print(FullCubeN)
#(Have to build cwmove input to accept cube side (i.e. Right) as side 1)
"""
"""class Moves():
    def cwMove(self, side1, side2, side3, side4, side5):
        if(self.side1 == Front):
            self.side1 = np.rot90(self.side1, 1, axes=(0, 1))
            self.side2[:,[0,0]] = (np.rot90(self.side4, 1, axes=(0, 1)))[:,[1,0]]) #side to right of rotation side
            self.side3[:,[2,2]] = (np.rot90(self.side5, 1, axes=(0, 1)))[:,[1,0]])   #side to left of rotation side
            self.side4[[2,2]] = (np.rot90(self.side3, 1, axes=(0, 1)) [[1,0]])  #side Above(Top) of rotation side
            self.side5[[0,0]] = (np.rot90(self.side2, 1, axes=(1, 0))[[1,0]])   #side Below(Bottom) of rotation side

        if (self.side1 == Right):
            self.side1 = np.rot90(self.side1, 1, axes=(0, 1))
            self.side2[:, [0, 0]] = (np.rot90(self.side4, 2, axes=(0, 1)))[:, [0, 0]])  # side to right of rotation side
            self.side3[:, [2, 2]] = self.side5[:, [0, 2]])  # side to left of rotation side
            self.side4[[2, 2]] = self.side3[[0, 2]])  # side Above(Top) of rotation side
            self.side5[[2, 2]] = self.side2[[0, 2]])  # side Below(Bottom) of rotation side

        return self.side1
        return self.side2
        return self.side3
        return self.side4
        return self.side5


    def ccwMove(self, side):
            self.side = np.rot90(self.side, 1, axes=(0, 1))
            return self.side


class Cube():
    def __init__(self, Top, Front, Right, Left, Back, Bottom):
        self.Top = Top
        self.Front = Front
        self.Right = Right
        self.Left = Left
        self.Back = Back
        self.Bottom = Bottom
"""
"Build Output Cube Faces for Display"
"""
RightOut = Right.reshape(9)
FrontOut = Front.reshape(9)
LeftOut = Left.reshape(9)
TopOut = Top.reshape(9)
BackOut = Back.reshape(9)
BottomOut = Bottom.reshape(9)"""
"print(RightOut)"
"print(Right)"

"cwMove(Cube.Front, Cube.Right, Cube.Left, Cube.Top, Cube.Bottom)"
"""
DisplayCube = np.ones((3,3,3,), dtype = 'bool')
print()
fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.set_facecolor("White")
ax.voxels(DisplayCube, facecolor = "#E02050", edgecolors = 'k')
ax.axis('off')
plt.show()

Viz.render()
"""
"""
FullCube = Cube(Front,Right,Left,Back,Bottom)

print(FullCube.Front)



def frontCw(self):
    return numpy.rot90(self, 1, axes=(1,0))
"""
"Cube = frontccw(Cube)"

"print(Cube.Front)"



"""
Front1 = Cube()
Front1 = Front1.front()


print(Front)
print(Front1)
print(numpy.rot90(Front, 1, axes=(0,1)))"""



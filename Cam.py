import math

from picamera import PiCamera
from time import sleep
import webcolors
from PIL import Image
import cv2
import numpy as np
from numpy import *

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
Flip =[]
FullCube = Cube(Top, Front, Right, Left, Back, Bottom, moves_out, Flip, dict)
moves_out = []



camera = cv2.VideoCapture(0)
def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_color_name(rgb):
    colors = {
    "r": (255, 0, 0),
    "g": (0, 255, 0),
    "b": (0, 0, 255),
    "y": (255, 255, 0),
    "w": (255, 255, 255),
    "o": (255, 121, 0)

}
    """
    print(rgb[1])
    min_distance = float("inf")
    closest_color = None
    for r,g,b in colors:
        print(r)
        rd = (rgb[0] - r) ** 2
        gd = (rgb[1] - g) ** 2
        bd = (rgb[2] - b) ** 2
        distance = math.sqrt(rd+gd+bd)
        if distance < min_distance:
            min_distance = distance
            closest_color = color
    return closest_color
"""
    min_distance = float("inf")
    closest_color = None
    for color, value in colors.items():
        distance = math.sqrt(sum([(i - j) ** 2 for i, j in zip(rgb, value)]))
        if distance < min_distance:
            min_distance = distance
            avg = (rgb[0] + rgb[1] + rgb[2])/3
            ab = (abs(rgb[0] - avg)+ abs(rgb[1] - avg)+ abs(rgb[2] - avg))/3
            print(ab)
            if color == "b":
                if (255 - rgb[2])> 50:
                    closest_color = "w"
                else:
                    closest_color = "bc"
            #if ab < 8: #HAVE TO FIX THIS, WHITE IS COMING OUT AS BLUE
            #    closest_color = "w"
            else:
                closest_color = color

    return closest_color
def ColorDetect(self):
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    focus = 0  # min: 0, max: 255, increment:5
    camera.set(cv2.CAP_PROP_FOCUS,focus)
    s, im = camera.read()
    cv2.imwrite('/home/rvc/cam.jpg', im)
    im = Image.open('/home/rvc/cam.jpg')
    rgb_im = im.convert('RGB')
    #"""
    #Top Left Color
    r1, g1, b1 = rgb_im.getpixel((400, 200))
    rgb1 = (r1,g1,b1)
    TopLeft = get_color_name(rgb1)
    print(TopLeft)
    #Top Middle Color
    r2, g2, b2 = rgb_im.getpixel((400, 200))
    rgb2 = (r2, g2, b2)
    TopMid = get_color_name(rgb2)
    print(TopMid)
    # Top Right Color
    r3, g3, b3 = rgb_im.getpixel((400, 300))
    rgb3 = (r3, g3, b3)
    TopRight = get_color_name(rgb3)
    print(TopRight)
    # Middle Left Color
    r4, g4, b4 = rgb_im.getpixel((400, 400))
    rgb4 = (r4, g4, b4)
    MidLeft = get_color_name(rgb4)
    print(MidLeft)
    # Middle Middle Color
    r5, g5, b5 = rgb_im.getpixel((400, 500))
    rgb5 = (r5, g5, b5)
    MidMid = get_color_name(rgb5)
    print(MidMid)
    # Middle Right Color
    r6, g6, b6 = rgb_im.getpixel((400, 600))
    rgb6 = (r6, g6, b6)
    MidRight = get_color_name(rgb6)
    print(MidRight)
    # Bottom Left Color
    r7, g7, b7 = rgb_im.getpixel((400, 700))
    rgb7 = (r7, g7, b7)
    BotLeft = get_color_name(rgb7)
    print(BotLeft)
    # Bottom Middle Color
    r8, g8, b8 = rgb_im.getpixel((400, 800))
    rgb8 = (r8, g8, b8)
    BotMid = get_color_name(rgb8)
    print(BotMid)
    # Bottom Right Color
    r9, g9, b9 = rgb_im.getpixel((400, 900))
    rgb9 = (r9, g9, b9)
    BotRight = get_color_name(rgb9)
    print(BotRight)
    #"""
    # Bottom Left Color

    r7 = 0
    g7 = 0
    b7 = 0
    n=0
    for pixelx in range(1400,1700):
        for pixely in range(700, 900):
            r7i, g7i, b7i = rgb_im.getpixel((pixelx, pixely))
            rgb7i = (r7i, g7i, b7i)
            r7 = r7i + r7
            g7 = g7i + g7
            b7 = b7i + b7
            n=n+1
            rgb7 = (r7, g7, b7)
    rgb7 = (r7/n, g7/n, b7/n)



    print(rgb7)

    self.BotLeft = get_color_name(rgb7)
    print(self.BotLeft)

    # Bottom Middle Color
    r8 = 0
    g8 = 0
    b8 = 0
    n = 0
    for pixelx in range(850, 1000):
        for pixely in range(700, 900):
            r8i, g8i, b8i = rgb_im.getpixel((pixelx, pixely))
            rgb8i = (r8i, g8i, b8i)
            r8 = r8i + r8
            g8 = g8i + g8
            b8 = b8i + b8
            n = n + 1
            rgb8 = (r8, g8, b8)
    rgb8 = (r8 / n, g8 / n, b8 / n)

    #r8, g8, b8 = rgb_im.getpixel((950, 800))
    #rgb8 = (r8, g8, b8)
    print(rgb8)
    self.BotMid = get_color_name(rgb8)
    print(self.BotMid)

    # Bottom Right Color
    r9 = 0
    g9 = 0
    b9 = 0
    n = 0
    for pixelx in range(300, 400):
        for pixely in range(700, 900):
            r9i, g9i, b9i = rgb_im.getpixel((pixelx, pixely))
            rgb9i = (r9i, g9i, b9i)
            r9 = r9i + r9
            g9 = g9i + g9
            b9 = b9i + b9
            n = n + 1
            rgb9 = (r9, g9, b9)
    rgb9 = (r9 / n, g9 / n, b9 / n)

    #r9, g9, b9 = rgb_im.getpixel((350, 800))
    #rgb9 = (r9, g9, b9)
    print(rgb9)

    self.BotRight = get_color_name(rgb9)
    print(self.BotRight)
    sleep(.5)


def CubeStart(self):
    self.Top = array([
    ['i', 'i', 'i'] ,
    ['i', 'i', 'i'] ,
    ['i', 'i', 'i'] ,
])
    self.moves_out = moves_out

    # Set middle colors
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
    print(self.Top)
    #Top_ccw()
    Top_ccw()

    ColorDetect(self)
    self.Top[2, 0] = self.BotLeft
    self.Top[2, 1] = self.BotMid
    #Top_ccw()
    Top_ccw()

    ColorDetect(self)
    self.Top[0, 0] = self.BotLeft
    self.Top[1, 0] = self.BotMid
    #Top_ccw()
    Top_ccw()

    ColorDetect(self)
    self.Top[0, 1] = self.BotMid
    #Top_ccw()
    Top_ccw()
    print(self.Top)
    Top = self.Top
    Front = self.Front
    Right = self.Right
    Left = self.Left
    Back = self.Back
    Bottom = self.Bottom
#"""

    #Right Face
    Front_ccw()
    Back_cw()
    Top_ccw()
    ColorDetect(self)
    self.Right[0, 0] = self.BotLeft
    self.Right[1, 0] = self.BotMid
    self.Right[2, 0] = self.BotRight
    Top_cw()
    Top_cw()
    ColorDetect(self)
    self.Right[2, 2] = self.BotLeft
    self.Right[1, 2] = self.BotMid
    self.Right[0, 2] = self.BotRight
    Top_ccw()
    Front_cw()
    Back_ccw()
    Right_cw()
    Front_ccw()
    Back_cw()
    Top_cw()
    ColorDetect(self)
    self.Right[0, 1] = self.BotMid
    Top_ccw()
    Top_ccw()
    ColorDetect(self)
    self.Right[2, 1] = self.BotMid
    Top_cw()
    Front_cw()
    Back_ccw()
    Right_ccw()
    Top = self.Top
    Front = self.Front
    Right = self.Right
    Left = self.Left
    Back = self.Back
    Bottom = self.Bottom


    # Left Face
    Front_cw()
    Back_ccw()
    Top_ccw()
    ColorDetect(self)
    self.Left[2, 2] = self.BotLeft
    self.Left[1, 2] = self.BotMid
    self.Left[0, 2] = self.BotRight
    Top_cw()
    Top_cw()
    ColorDetect(self)
    self.Left[0, 0] = self.BotLeft
    self.Left[1, 0] = self.BotMid
    self.Left[2, 0] = self.BotRight
    Top_ccw()
    Front_ccw()
    Back_cw()
    Left_cw()
    Front_cw()
    Back_ccw()
    Top_ccw()
    ColorDetect(self)
    self.Left[2, 1] = self.BotMid
    Top_cw()
    Top_cw()
    ColorDetect(self)
    self.Left[0, 1] = self.BotMid
    Top_ccw()
    Front_ccw()
    Back_cw()
    Left_ccw()

    # Back Face
    Left_cw()
    Right_ccw()
    ColorDetect(self)
    self.Back[0, 0] = self.BotLeft
    self.Back[1, 0] = self.BotMid
    self.Back[2, 0] = self.BotRight
    Top_cw()
    Top_cw()
    ColorDetect(self)
    self.Back[0, 2] = self.BotLeft
    self.Back[1, 2] = self.BotMid
    self.Back[2, 2] = self.BotRight
    Top_ccw()
    Top_ccw()
    Left_ccw()
    Right_cw()
    Back_cw()
    Left_cw()
    Right_ccw()
    ColorDetect(self)
    self.Back[2, 1] = self.BotMid
    Top_cw()
    Top_cw()
    ColorDetect(self)
    self.Back[0, 1] = self.BotMid
    Top_ccw()
    Top_ccw()
    Left_ccw()
    Right_cw()
    Back_ccw()

    # Front Face
    Left_ccw()
    Right_cw()
    ColorDetect(self)
    self.Front[2, 2] = self.BotLeft
    self.Front[1, 2] = self.BotMid
    self.Front[0, 2] = self.BotRight
    Top_cw()
    Top_cw()
    ColorDetect(self)
    self.Front[0, 0] = self.BotLeft
    self.Front[1, 0] = self.BotMid
    self.Front[2, 0] = self.BotRight
    Top_ccw()
    Top_ccw()
    Left_cw()
    Right_ccw()
    Front_cw()
    Left_ccw()
    Right_cw()
    ColorDetect(self)
    self.Front[0, 1] = self.BotMid
    Top_cw()
    Top_cw()
    ColorDetect(self)
    self.Front[2, 1] = self.BotMid
    Top_ccw()
    Top_ccw()
    Left_cw()
    Right_ccw()
    Front_ccw()

    # Bottom Face
    Left_cw()
    Left_cw()
    Right_cw()
    Right_cw()
    ColorDetect(self)
    self.Bottom[2, 2] = self.BotLeft
    self.Bottom[1, 2] = self.BotMid
    self.Bottom[0, 2] = self.BotRight
    Top_cw()
    Top_cw()
    ColorDetect(self)
    self.Bottom[0, 0] = self.BotLeft
    self.Bottom[1, 0] = self.BotMid
    self.Bottom[2, 0] = self.BotRight
    Left_cw()
    Left_cw()
    Right_cw()
    Right_cw()
    Front_cw()
    Front_cw()
    Back_cw()
    Back_cw()
    Top_cw()
    ColorDetect(self)
    self.Bottom[2, 1] = self.BotMid
    Top_cw()
    Top_cw()
    ColorDetect(self)
    self.Bottom[0, 1] = self.BotMid
    Top_cw()
    Top_cw()
    Front_cw()
    Front_cw()
    Back_cw()
    Back_cw()

    Top = self.Top
    Front = self.Front
    Right = self.Right
    Left = self.Left
    Back = self.Back
    Bottom = self.Bottom
#


#ColorDetect(FullCube)
CubeStart(FullCube)


Right = FullCube.Right
Left = FullCube.Left
Top = FullCube.Top
Bottom = FullCube.Bottom
Front = FullCube.Front
Back = FullCube.Back

#Adjust Output to accurately map positions
#Top = np.rot90(Top, 1, axes= (1,0)); #rotate ccw
Bottom = np.rot90(Bottom, 1, axes= (0,1)); #rotate cw

print(Top)
print(Right)
print(Left)
print(Back)
print(Bottom)
print(Front)


#Flatten Individual Arrays
RightFlat = np.ravel(Right)
LeftFlat = np.ravel(Left)
FrontFlat = np.ravel(Front)
BackFlat = np.ravel(Back)
TopFlat = np.ravel(Top)
BottomFlat = np.ravel(Bottom)

FullCubeFlat = np.transpose(np.vstack((RightFlat, TopFlat, BackFlat, BottomFlat, FrontFlat, LeftFlat)))
#print(FullCubeFlat)

#Adjust Output to accurately map positions



#Adjust Output for Input into Cube Simulator
DFCube = pd.DataFrame(FullCubeFlat, index = [1, 2, 3, 4, 5, 6, 7, 8, 9], columns=['w', 'r', 'g', 'o', 'b', 'y' ])
face = "wrgoby"
StringCube = DFCube.copy()
for i, v in enumerate(face):
    #print(v)
    StringCube[v] = StringCube[v].replace({1: 'w'})
    StringCube[v] = StringCube[v].replace({2: 'b'})
    StringCube[v] = StringCube[v].replace({3: 'r'})
    StringCube[v] = StringCube[v].replace({4: 'g'})
    StringCube[v] = StringCube[v].replace({5: 'o'})
    StringCube[v] = StringCube[v].replace({6: 'y'})
#print(StringCube)

#DFCube['w'] = DFCube['DFCube'].replace({'1':'w', '2':'b', '3':'r', '4':'g', '5':'o', '6':'y', })
#Almost done, just have to figure out how to add index to each row
for i in range(1,10):
    k=i-1
    #print(StringCube.iloc[[k]])
    StringCube.iloc[k] = StringCube.iloc[k] + f'{i}'

#print(StringCube)
#output.save(StringCube)
print("This code took", process_time(),"s to execute")

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 13:25:28 2022

@author: Jeremy
"""

import Classes

import tkinter 
import time
from random import random
import threading


# if __name__ == '__main__':

#     a=Classes.MyClass()
#     a.greet()

#     b=Classes.MyNextClass()
#     b.greetAgain()

print("Main Program")

 
myWorld = Classes.World(100, 100)
myWorld.generateMap()

myWorld.printEntities()



Window_Width=800
Window_Height=600

Ball_Start_XPosition = 50

Ball_Start_YPosition = 50

Ball_Radius = 30

Ball_min_movement = 50

Refresh_Sec = 0.03

Zoom=20
  

def create_animation_window():
  Window = tkinter.Tk()
  Window.title("Python Guides")

  Window.geometry(f'{Window_Width}x{Window_Height}')
  return Window
 

def create_animation_canvas(Window):
  canvas = tkinter.Canvas(Window)
  canvas.configure(bg="Blue")
  canvas.pack(fill="both", expand=True)
  return canvas
 

def animate_entities(Window, canvas):


  cameraCenterX = -Window_Width / 2
  cameraCenterY = -Window_Height / 2
  xOffset = 0
  yOffset = 0


  
  while True:
    
      canvas.delete("all")

      me = myWorld.character
      xOffset = Window_Width / 2  - ((me.xLoc + .5) * Zoom)
      yOffset = Window_Height / 2  - ((me.yLoc + .5) * Zoom)
    
      myCharacter = canvas.create_rectangle(
            me.xLoc * Zoom + xOffset,
            me.yLoc * Zoom + yOffset,
            (me.xLoc + 1) * Zoom + xOffset,
            (me.yLoc + 1) * Zoom + yOffset,
            fill="Green", outline="Green", width=1)
    
      for entity in myWorld.entities:
        if entity.type == "Stone":
            canvas.create_rectangle(
            entity.xLoc * Zoom + xOffset,
            entity.yLoc * Zoom + yOffset,
            (entity.xLoc + 1) * Zoom + xOffset,
            (entity.yLoc + 1) * Zoom + yOffset,
            fill="Gray", outline="Gray", width=1)
    
      for enemy in myWorld.enemies:
                canvas.create_rectangle(
                enemy.xLoc * Zoom + xOffset,
                enemy.yLoc * Zoom + yOffset,
                (enemy.xLoc + 1) * Zoom + xOffset,
                (enemy.yLoc + 1) * Zoom + yOffset,
                fill="Red", outline="Red", width=1)
                

      #for entity in animatedEntities:
      # canvas.move(myCharacter, 1, 1)
      Window.update()
      
      time.sleep(Refresh_Sec)
      
      for enemy in myWorld.enemies:
           xDiff = me.xLoc - enemy.xLoc
           yDiff = me.yLoc - enemy.yLoc
           if abs(xDiff) > abs(yDiff) and xDiff > 4:
               enemy.xLoc += 1 * (xDiff/abs(xDiff))
           elif yDiff > 4:
               enemy.yLoc += 1 * (yDiff/abs(yDiff))
        
     

          
          
               
          
      
      
#  ball_pos = canvas.coords(ball)
    # unpack array to variables
  # al,bl,ar,br = ball_pos
  # if al < abs(xinc) or ar > Window_Width-abs(xinc):
  #   xinc = -xinc
  # if bl < abs(yinc) or br > Window_Height-abs(yinc):
  #   yinc = -yinc
 
# from pynput import keyboard

# def on_press(key):
#     if key == keyboard.Key.esc:
#         return False  # stop listener
#     try:
#         k = key.char  # single-char keys
#     except:
#         k = key.name  # other keys
#     if k in ['1', '2', 'left', 'right']:  # keys of interest
#         # self.keys.append(k)  # store it in global-like variable
#         print('Key pressed: ' + k)
#         # return False  # stop listener; remove this if want more keys

# listener = keyboard.Listener(on_press=on_press)
# listener.start()  # start to listen on a separate thread
# #listener.join()  # remove if main thread is polling self.keys

def up(event):
    myWorld.character.yLoc -= 1 
    print(myWorld.character)
def down(event):
    myWorld.character.yLoc += 1 
    print(myWorld.character)
def left(event):
    myWorld.character.xLoc -= 1 
    print(myWorld.character)
def right(event):
    myWorld.character.xLoc += 1 
    print(myWorld.character)

Animation_Window = create_animation_window()
Animation_canvas = create_animation_canvas(Animation_Window)

Animation_Window.bind("<w>",up)
Animation_Window.bind("<a>",left)
Animation_Window.bind("<s>",down)
Animation_Window.bind("<d>",right)
Animation_Window.bind("<Up>",up)
Animation_Window.bind("<Left>",left)
Animation_Window.bind("<Down>",down)
Animation_Window.bind("<Right>",right)

animate_entities(Animation_Window,Animation_canvas)

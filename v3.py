"""
/********************************************************************************************************************
 * Project by: Aditya Milind Ponde 
 * Chrome Dino Bot V1.3
 *
 * This script uses pyautigui and pytesseract to cheat the Chrome Dino game.
 *
 * pyautogui is used to locate the position of the cactus in a given part of 
 * the field and to control the keyboard to make the dino jump.
 *
 * pytesseract is used to keep track of the score as the game speeds up.
 * 
 * pytesseract is currently not being used. (in progress) V1.4 will have a working version.
********************************************************************************************************************/
"""


# importing the libraries needed for code to funciton
import pyautogui
import time
import os
import pytesseract


# x and y values for the start pixel pyautogui.locateOnScreen() uses
x, y = 580,970
# dimentions of FOV rectangle that pyautogui.locateOnScreen() uses
w, h = 440, 145


# first method called before game is started. Pauses for given interval then starts the game
def gameStart():
	time.sleep(1)
	pyautogui.moveTo(100, 500)
	pyautogui.click()
	pyautogui.click()
	pyautogui.moveTo(100, 1000)
	pyautogui.click()
	pyautogui.click()


# method checks for cactus in the given FOV using x, y coordinates and a rectangle of width: w and height: h
# returns location in the region as list(locationRegion). Consists of (x, y) coordinates or None if cactus
# doesn't exist
def location():
	locationRegion = pyautogui.locateOnScreen('Cactus.png', region = (x, y, w, h), grayscale = True, confidence=0.18)
	return locationRegion


# prints the location of the cactus in the box
def _locationInBox(box):
	print("X: " + str(box[0]) + " Y: " + str(box[1]))


# To check the FOV position on the screen by taking a screenshot of (x,y) startpoint and of size w, h
def _imageOutput():
	pyautogui.screenshot('s.png', region=(x, y, w, h))


# Presses the key specified through the parameter
def key(thisKey):
	pyautogui.keyDown(thisKey)

# *********************************************************************
# IN PROGRESS --------------------------------------------- NOT WORKING
# accounts for the speeding up of the game and calculated the reduction 
# in time before jumping
def timejump():
	time = 0.0
	img = pyautogui.screenshot(region=(1640, 720, 200, 80))
	score = pytesseract.image_to_string(img)
	numbersList = [0, 0, 0, 0, 0]
	for i in range(len(score) - 1):
		if score[i].isdigit():
			numbersList[i] = int(score[i])


	if numbersList[2] < 2:
		return 0.0
	else:
		return 0.2
# *********************************************************************


# responsible to jump when theres a cactus
# takes into account the position of the cactus in the FOV box to determine best time to jump
# if cactus is closer to the left of the FOV rectangle, dino jumps with less delay
# inverse true if cactus is closer to right of rectangle
def movement(timeDiff = 0.0):
	currentPosition = location()
	if currentPosition != None:
		if currentPosition[0] < 650:
			_locationInBox(currentPosition)
			key('up')

		elif currentPosition[0] >=  650 and currentPosition[0] <= 750:
			_locationInBox(currentPosition)
			time.sleep(0.11 - timeDiff)
			key('up')

		elif currentPosition[0] > 750 and currentPosition[0] <= 800:
			_locationInBox(currentPosition)
			time.sleep(0.14 - timeDiff)
			key('up')

		elif currentPosition[0] > 800 and currentPosition[0] <= 900:
			_locationInBox(currentPosition)
			time.sleep(0.16 - timeDiff)
			key('up')

		elif currentPosition[0] > 900:
			_locationInBox(currentPosition)
			time.sleep(0.19 - timeDiff)
			key('up')

# infinite loop to play the game
def main():
	gameStart()
	while 1:
		movement()

if __name__ == '__main__':
    main()





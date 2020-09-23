# perusall

Perusall is used as an online textbook viewing website. This site is used to give a grade for how much of a particular textbook chapter you have read. Many courses I have taken so far also require you to read all new comments on each annotation. This script will automatically read the chapter, as well as read each of the annotations*. 

Rooms for improvement
-It currently only reads where the green dots are. I could add yellow, however it will skill skip many of the annotations. 
-There is a problem when switching from the scroller (used to read the chapter) to the comment reader. 
-Some code is repetitive

Requirements
Google Chrome
Python 3.7
import pygame
import time
import random
import pyautogui
Screen size of 1080p (1920x1080)

How to use - Comment viewer
1st Make sure the script runs. 
2nd Open the chapter you are going to read. Have 
3rd When prompted in terminal, type yes to using the comment viewer

import pygame
import time
import random
import pyautogui

#functions

#done = True #used to bypass the scrolling part and go to the auto click on comments
def scroller(clickx=0, clicky=0, basecolor=0, commmentcheck=0):
	'''
	clickx is the x cordinate you want it to click to scroll down. This should be the little scrolling bar.
	clicky is the same as clickx except the y value
	basecolor is the color that it will compare to see when the page is all the way down.
	'''

	#condition to see if the variables are set.
	if clickx == 0 or clicky == 0 or basecolor == 0:
		print("Move mosue to scoll down spot then press enter")
		input("Press enter when you're ready")

		clickx, clicky = pyautogui.position()
		basecolor = pyautogui.pixel(clickx, clicky)

	done = False
	while not done:

		for event in pygame.event.get():
			print("hey")
			waittime = random.randint(80,120)
			#waittime = 1
			pyautogui.click(clickx, clicky)	
			
			if commmentcheck == 1:
				commentcheck()
			
			#to make sure the display is not closed
			if event.type == pygame.QUIT:
				done = True

			screencolor = pyautogui.pixel(clickx, clicky)
			if screencolor != basecolor:
				print("New pixel color for where it's set to click.")
				done = True

			pygame.display.flip()

def like():
	'''
	used to randomly like a post. To increase liked posted frequency, decrease the outof number below
	'''
	try:
		outof = 20
		if random.randint(0,outof) == 2:

			print("Going to like this post.")

			if pyautogui.locateCenterOnScreen("images/1080p/green_like.png", confidence=.9):
				pyautogui.click(pyautogui.locateCenterOnScreen("images/1080p/green_like.png", confidence=.9))
				time.sleep(2)
				print("Liked")
			elif pyautogui.locateCenterOnScreen("images/1080p/like.png", confidence=.9):
				pyautogui.click(pyautogui.locateCenterOnScreen("images/1080p/like.png", confidence=.9))
				time.sleep(2)
				print("Liked")
			else:
				print("I tried to like a post... but I couldn't find one to like..")
	except:
		print("Error in like function")
		exit()
	return

def scrollup():
	print("Running scollup")
	
	#gets back button location
	closex, closey, closewidth, closeheight = backbutton()
	screensizex, screensizey = screensize()

	print("Up arrow found so we can scroll up! but first, lets 'read'")
	like()
	time.sleep(2)
	try:
		pyautogui.click(pyautogui.locateCenterOnScreen("images/1080p/up_arrow.png", region=(closex, closey, closewidth+20, screensizey - closey), confidence=.9))

	except:
		print("Error 3")

	if pyautogui.locateOnScreen("images/1080p/up_arrow.png", region=(closex, closey, closewidth+20, screensizey - closey), confidence=.9) != None:
		scrollup()
	else:
		print("Done scrolling up")
		return

def scrolldown():
	print("Running scolldown")
	
	closex, closey, closewidth, closeheight = backbutton()
	screensizex, screensizey = screensize()
	

	print("Down arrow found so we can scroll down! but first, lets 'read'")
	like()
	time.sleep(2)
	try:
		pyautogui.click(pyautogui.locateCenterOnScreen("images/1080p/down_arrow.png", region=(closex, closey, closewidth+20, screensizey - closey), confidence=.9))
	except:
		print("Error 3")
	if pyautogui.locateOnScreen("images/1080p/down_arrow.png", region=(closex, closey, closewidth+20, screensizey - closey), confidence=.9) != None:
		scrolldown()
	else:
		return

def backbutton():
	try:
		closex, closey, closewidth, closeheight = pyautogui.locateOnScreen("images/1080p/close.png", confidence=.9)
		return closex, closey, closewidth, closeheight
	except:
		print("Error 1-1. Unable to find the close comments button. Exiting now.")
		exit()

def screensize():
	try:
		screensizex, screensizey = pyautogui.size()
	except:
		print("error 1-2")
	return screensizex, screensizey

def commentcheck():
	print("Running comment check")
	try:
		backbuttonx, backbuttony = pyautogui.locateCenterOnScreen("back.png")
	except:
		print("Error getting back button")

	try:
		greenlist = pyautogui.locateAllOnScreen("green.png", confidence=.9)
	except:
		print("Error getting green list")

	try:
		closex, closey, closewidth, closeheight = pyautogui.locateOnScreen("images/1080p/close.png")
	except:
		print("Error 1-1")
	try:
		screensizex, screensizey = pyautogui.size()
	except:
		print("error 1-2")


	try:
		for box in greenlist:
			print("\n\n\n")
			print("Found a green comment box thing!!")
			
			#print(box) prints the data in box
			time.sleep(random.uniform(1,2)) #waits a second
			pyautogui.click(box[0]+5, box[1]+5)

			time.sleep(2) #for page to load
			
			try:
				if pyautogui.locateOnScreen("images/1080p/up_arrow.png", region=(closex, closey, closewidth+20, screensizey - closey)):
					print("Scrollup found.")
					scrollup()
				else:
					if pyautogui.locateOnScreen("images/1080p/down_arrow.png", region=(closex, closey, closewidth+20, screensizey - closey)):
						print("Scrolldown found.")
						scrolldown()
					else:
						print("Neither scroll found.")
			except:
				print("Error running scroller.")
			#if pyautogui.locateOnScreen("images/1080p/up_arrow.png", region=(closex, closey, closewidth+20, screensizey - closey)):
			#	scrollup()
			#elif pyautogui.locateOnScreen("images/1080p/down_arrow.png", region=(closex, closey, closewidth+20, screensizey - closey)):
			#	scrolldown()
			#else:
			#	print("Comments page has no scrolling to do. ")
			#	like()
			time.sleep(3)


			#if the up arrow is found


			time.sleep(random.uniform(1,3))
			#goes back

			pyautogui.click(backbuttonx, backbuttony)
			time.sleep(1)
	except:
		print("Error on loop")
		exit()

#iniialize pygame window. Pygame only used to get the window to close.
pygame.init()
screen = pygame.display.set_mode((400, 300))

scrollerinput = input("Do you want to read the textbook? Enter yes if so, otherwise, press enter.")
commentviewerinput = input("Do you want to read all the comments? Enter yes if so, otherwise, press enter.")

if input("Press enter to begin") == '':
	pass
else:
	exit()

#runs the scroller if yes is input above
if scrollerinput == "yes":

	print("Move mouse to scoll down spot then press enter")
	input("Press enter when you're ready")

	clickx, clicky = pyautogui.position()
	basecolor = pyautogui.pixel(clickx, clicky)

	scroller()




if commentviewerinput == "yes":
	#clicks on all conversations/comments
	if pyautogui.locateCenterOnScreen("images/1080p/all_comments_on.png") == None:
		print("Not currently viewing all comments. CLicking to open all comments.")
		pyautogui.click(pyautogui.locateCenterOnScreen("images/1080p/all_comments.png"))
		if pyautogui.locateOnScreen("images/1080p/all_comments_on.png") == None:
			print("Why are we not viewing all the comments?")
			exit()
		time.sleep(1)

	else:
		print("Already viewing all comments.")

	scroller(commmentcheck=1)


exit()
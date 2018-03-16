from graphics import *
import time
import random
def randomFill():
	#r, g, and b are randomized from 0 to 255 and those are put into the function color_rgb() from graphics
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	return color_rgb(r, g, b)
def main():
	allPoints = []
	width = 750
	height = 600
	textCenter = Point(width/2, height*7/8)
	win = GraphWin("Connect The Dots", width, height)
	p1 = Point(0, height*3/4)
	p2 = Point(width, height)
	seeShapeBox = Rectangle(p1, p2)
	seeShapeBox.draw(win)
	seeShapeBox.setFill("gray")
	boxText = Text(textCenter, "Click above to add dots, click here to see shape")
	boxText.draw(win)
	while True:
		click = win.getMouse()
		if click.getY() < p1.getY():
			click.draw(win)
			allPoints.append(click)
		else:
			break
	boxText.undraw()
	if allPoints == []:
		errorDrawing = Text(textCenter, "Error: no dots drawn, click anywhere to close")
		errorDrawing.draw(win)
	else:
		finalFigure = Polygon(allPoints)
		finalFigure.draw(win)
		color = randomFill()
		finalFigure.setOutline(color)
		finalFigure.setFill(color)
		finalDrawn = Text(textCenter, "Click anywhere to close")
		finalDrawn.draw(win)
	win.getMouse()
	win.close()
main()
from graphics import *
import time
def main():
	width = 750
	height = 600
	sunMoveDist = 1
	sunRadius = height/15
	win = GraphWin("Animated Scene", width, height)
	#making the window
	win.setBackground("light blue")
	textPoint = Point(width/2, height/30)
	#the point in which all of the texts' centers will be
	sunText = Text(textPoint, "Click for sun")
	sunText.draw(win)
	clickSun = win.getMouse()
	#clickSun is the sun's center point
	sun = Circle(clickSun, sunRadius)
	sun.draw(win)
	sun.setOutline("yellow")
	sun.setFill("yellow")
	sunText.undraw()
	#undraws the sun's text so it doesn't just stick around when drawing new texts
	waterText = Text(textPoint, "Click for water")
	waterText.draw(win)
	clickWater = win.getMouse()
	waterP1 = Point(0, clickWater.getY())
	waterP2 = Point(width, height)
	water = Rectangle(waterP1, waterP2)
	water.draw(win)
	water.setOutline("dark blue")
	water.setFill("dark blue")
	waterText.undraw()
	sandText1 = Text(textPoint, "Click for sand")
	sandText1.draw(win)
	clickSand1 = win.getMouse()
	while clickSand1.getY() < waterP1.getY():
	#while loop to make sure the point isn't above the water
		sandText1.undraw()
		sandText1 = Text(textPoint, "Try clicking below the water")
		sandText1.draw(win)
		clickSand1 = win.getMouse()
	sandText1.undraw()
	sandText2 = Text(textPoint, "Click again for sand")
	sandText2.draw(win)
	clickSand2 = win.getMouse()
	while clickSand2.getY() < waterP1.getY():
	#while loop to make sure the point isn't above the water
		sandText2.undraw()
		sandText2 = Text(textPoint, "Sand can not go above water")
		sandText2.draw(win)
		clickSand2 = win.getMouse()
	sandText2.undraw()
	while clickSand1.getX() == clickSand2.getX() and clickSand1.getY() == clickSand2.getY():
		sandText = Text(textPoint, "Sand can not go above water")
		sandText.draw(win)
		clickSand2 = win.getMouse()
		sandText.undraw()
	slope = (clickSand2.getY() - clickSand1.getY()) / (clickSand2.getX() - clickSand1.getX())
	yint = clickSand1.getY() - (slope*clickSand1.getX())
	#yint is y intercept
	y1 = yint #the point on the slope on the left of the screen
	y2 = slope*width + yint #the point on the slope on the right of the screen
	while y1 < waterP1.getY() or y2 < waterP1.getY():
	#while loop to make sure the y1 or y2
		sandText = Text(textPoint, "Sand can not go above water")
		sandText.draw(win)
		clickSand2 = win.getMouse()
		slope = (clickSand2.getY() - clickSand1.getY()) / (clickSand2.getX() - clickSand1.getX())
		yint = clickSand1.getY() - (slope*clickSand1.getX())
		y1 = yint
		y2 = slope*width + yint
		sandText.undraw()
	sP1 = Point(0, height)
	sP4 = Point(width, height)
	sP2 = Point(0, y1)
	sP3 = Point(width, y2)
	sandPoints = [sP1, sP2, sP3, sP4]
	#list of all four points to the polygon (sand)
	sand = Polygon(sandPoints)
	sand.draw(win)
	sand.setOutline("tan")
	sand.setFill("tan")
	sunsetText = Text(textPoint, "Click for sunset")
	sunsetText.draw(win)
	win.getMouse()
	sunsetText.undraw()
	while sun.getCenter().getY() - sunRadius + sunMoveDist < waterP1.getY():
	#while loop moves the sun until the top of the sun reaches the top of the water
		sun.move(0, sunMoveDist)
		time.sleep(0.01)
	#closes the window after the sunset
	win.close()
main()
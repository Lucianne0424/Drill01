import turtle as tu

tu.shape("turtle")

def moveTurtleW():
     tu.setheading(90)
     tu.stamp()
     tu.forward(50)

def moveTurtleA():
     tu.setheading(180)
     tu.stamp()
     tu.forward(50)

def moveTurtleS():
     tu.setheading(270)
     tu.stamp()
     tu.forward(50)

def moveTurtleD():
     tu.setheading(0)
     tu.stamp()
     tu.forward(50)

def moveTurtleESC():
     tu.reset()


tu.onkey(moveTurtleW, 'w')
tu.onkey(moveTurtleA, 'a')
tu.onkey(moveTurtleS, 's')
tu.onkey(moveTurtleD, 'd')
tu.onkey(moveTurtleESC, 'Escape')
tu.listen()
tu.exitonclick()

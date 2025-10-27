# Code here
import turtle as trtl
import random as rand

#----- Variables and screen setup
soccer_ball = "soccerball.gif"
goal = "goal.gif"


wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(soccer_ball)
wn.bgpic(goal)
trtl.Screen().bgcolor("#00bfff")

ball = trtl.Turtle()
ball.shape(soccer_ball)
ball.turtlesize(2)
ball.penup()
ball.goto(0,-120)
wn.tracer(False)

#----functions






wn = trtl.Screen()
wn.mainloop()
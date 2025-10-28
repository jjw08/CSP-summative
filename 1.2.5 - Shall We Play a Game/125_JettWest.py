import turtle as trtl
import random as rand

#----- Variables and screen setup
soccer_ball = "soccerball.gif"
goal = "goal.gif"
goaler = "goalie.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(soccer_ball)
wn.bgpic(goal)
trtl.Screen().bgcolor("#00bfff")


#Create ball 
ball = trtl.Turtle()
ball.shape(soccer_ball)
ball.penup()
ball.goto(0,-120)
wn.tracer(False)

#Add goalie

goalie = trtl.Turtle()
goalie.shape(goaler)
goalie.penup()
goalie.goto(0,0)
wn.tracer(False)


#----functions
#Create onclick functions for a, w, d, move ball to specific positions

#create specific random positions for the golie to move to

#if ball and goalie = same x.cor then print you lose, end game


#if ball and goalie = diff x.cor then add 1 score, reloop the game.





wn = trtl.Screen()
wn.mainloop()
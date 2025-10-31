import turtle as trtl
import random as rand

#----- Variables and screen setup
soccer_ball = "soccerball.gif"
goal = "goal.gif"
goaler = "goalie.gif"
game = False

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(soccer_ball)
wn.addshape(goaler)
wn.bgpic(goal)
trtl.Screen().bgcolor("#00bfff")

#Add goalie

goalie = trtl.Turtle()
goalie.shape(goaler)
goalie.penup()
goalie.goto(0,-40)
goalie_postions = [(0,-40), (-80,-40), (80,-40)]
#Create ball 
ball = trtl.Turtle()
ball.shape(soccer_ball)
ball.penup()
ball.goto(0,-120)

#add word turtle
word = trtl.Turtle()
word.hideturtle()
word.penup()
word.pensize(2)
word.speed(10)
word.color("white")
word.goto(0,100)
word.write("Click the ball to start!", align='center',  font=("Arial", 20, "normal"))

#----functions
#create a start game function
def startgame(x,y):
    global game
    game = True
    #print("game is true")
    ball.goto(0,-120)
    wn.onkeypress(shoot_left, "a")
    wn.onkeypress(shoot_center, "s")
    wn.onkeypress(shoot_right, "d")
    wn.listen()
    word.clear()
    word.write("press a(left), s(middle), or d(right) to shoot!", align='center',  font=("Arial", 20, "normal"))
    
#create end game function
def endgame():
    global game
    game = False
    #disable shooting
    wn.onkeypress(None, "a")
    wn.onkeypress(None, "s")
    wn.onkeypress(None, "d")



#Create onpress functions for a, s, d, move ball to specific positions, move goalie to random positions
def shoot_left():
    global game
    if game:
        goalie.goto(rand.choice(goalie_postions))
        ball.goto(-80,-40)
        endgame()
        #print("game is now false")
def shoot_center():
    global game
    if game:
        goalie.goto(rand.choice(goalie_postions))
        ball.goto(0, -40)
        endgame()
        #print("game is now false")
def shoot_right():
    global game
    if game:
        goalie.goto(rand.choice(goalie_postions))
        ball.goto(80, -40)
        endgame()
        #print("game is now false")




#if ball and goalie = same x.cor then print you lose, end game



#if ball and goalie = diff x.cor then add 1 score, reloop the game.


#---events


ball.onclick(startgame) #start game

if goalie.xcor() == ball.xcor():
    #Call up leaderboard
    print("you lose!")
elif goalie.xcor() != ball.xcor(): 
    #reset game
    print("you win!")

wn.mainloop()
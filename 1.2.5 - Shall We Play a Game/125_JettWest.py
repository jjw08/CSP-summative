import turtle as trtl
import random as rand

#----- Variables and screen setup
soccer_ball = "soccerball.gif"
goal = "goal.gif"
goaler = "goalie.gif"
game = False
win = False
lose = False
score = 0





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
    global win
    global lose
    game = True
    win = False
    lose = False

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
    global score
    if game:
        goalie.goto(rand.choice(goalie_postions))
        ball.goto(-80,-40)
        endgame()
        
        if goalie.xcor() == ball.xcor(): #lose condition
            global lose 
            lose = True
            print("you lose!")
            word.clear()
            word.write("BLOCKED BY JAMES! Click the ball to shoot again!", align='center',  font=("Arial", 20, "normal"))
            score = 0
            print(score)
          
        elif goalie.xcor() != ball.xcor(): #win condition
            global win
            win = True
            print("you win!")
            word.clear()
            word.write("Gooooaaaal! Click the ball to shoot again!", align='center',  font=("Arial", 20, "normal"))
            score = score + 1
            print(score)


      

def shoot_center():
    global game
    global score
    if game:
        goalie.goto(rand.choice(goalie_postions))
        ball.goto(0, -40)
        endgame()
        
        if goalie.xcor() == ball.xcor():
            global lose 
            lose = True
            print("you lose!")
            word.clear()
            word.write("BLOCKED BY JAMES! Click the ball to shoot again!", align='center',  font=("Arial", 20, "normal"))
            score = 0
            print(score)
        elif goalie.xcor() != ball.xcor(): 
            global win
            win = True
            print("you win!")
            word.clear()
            word.write("Gooooaaaal! Click the ball to shoot again!", align='center',  font=("Arial", 20, "normal"))
            score = score + 1
            print(score)
        

def shoot_right():
    global game
    global score
    if game:
        goalie.goto(rand.choice(goalie_postions))
        ball.goto(80, -40)
        endgame()
        
        if goalie.xcor() == ball.xcor():
            global lose 
            lose = True
            print("you lose!")
            word.clear()
            word.write("BLOCKED BY JAMES! Click the ball to shoot again!", align='center',  font=("Arial", 20, "normal"))
            score = 0
            print(score)
            

        elif goalie.xcor() != ball.xcor():  
            global win
            win = True
            print("you win!")
            word.clear()
            word.write("Gooooaaaal! Click the ball to shoot again!", align='center',  font=("Arial", 20, "normal"))
            score = score + 1 
            print(score)



#---events


ball.onclick(startgame) #start game



wn.mainloop()
import turtle as trtl
import random as rand
import leaderboard as lb
#----- Variables and screen setup
soccer_ball = "soccerball.gif"
goal = "goal.gif"
goaler = "goalie.gif"
game = False
win = False
lose = False
score = 0

leader_turtle = trtl.Turtle()
leader_turtle.hideturtle()
leader_turtle.penup()
leadernames = []
leaderscores = []
leaderboard_file_name = "a125_leaderboard.txt"


# Score Writer
score_writer = trtl.Turtle()
score_writer.hideturtle()

#score turtle
score_turt = trtl.Turtle()
score_turt.hideturtle()
score_turt.penup()
score_turt.pensize(2)
score_turt.speed(10)
score_turt.color("white")
score_turt.goto(0,200)


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


player_name = trtl.textinput("enter your intials", "Please enter your initials")
player_name = player_name.upper()
player_name = player_name[:3]
#----functions
#create a start game function
def startgame(x,y):
    score_writer.clear()
    global game
    global win
    global lose
    global score
    game = True
    win = False
    lose = False
    
    #print("game is true")
    score_turt.clear()
    score_turt.write(score, align='center',  font=("Arial", 20, "normal"))
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
           
            updateleaderboard()
           
            score = 0
            

        elif goalie.xcor() != ball.xcor(): #win condition
            global win
            win = True
            score_turt.clear()
            print("you win!")
            word.clear()
            word.write("Gooooaaaal! Click the ball to shoot again!", align='center',  font=("Arial", 20, "normal"))
            score = score + 1
            print(score)
            score_turt.write(score, align='center',  font=("Arial", 20, "normal"))

      

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
            
            updateleaderboard()
            score = 0
            
        elif goalie.xcor() != ball.xcor(): 
            global win
            win = True
            score_turt.clear()
            print("you win!")
            word.clear()
            word.write("Gooooaaaal! Click the ball to shoot again!", align='center',  font=("Arial", 20, "normal"))
            score = score + 1
            print(score)
            score_turt.write(score, align='center',  font=("Arial", 20, "normal"))
        

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
            
            print(score)
            updateleaderboard()
            score = 0
            

        elif goalie.xcor() != ball.xcor():  
            global win
            win = True
            score_turt.clear()
            print("you win!")
            word.clear()
            word.write("Gooooaaaal! Click the ball to shoot again!", align='center',  font=("Arial", 20, "normal"))
            score = score + 1
            print(score)
            score_turt.write(score, align='center',  font=("Arial", 20, "normal"))


def updateleaderboard():
    

  global score
  

  # get the names and scores from the leaderboard file
  leadernames = lb.get_names(leaderboard_file_name)
  leaderscores = lb.get_scores(leaderboard_file_name)

 #check to see if score is higher than leaderboard scores
  if (len(leaderscores) < 5 or score >= leaderscores[4]):
    lb.update_leaderboard(leaderboard_file_name, leadernames, leaderscores, player_name, score)

    leadernames = lb.get_names(leaderboard_file_name)
    leaderscores = lb.get_scores(leaderboard_file_name)


    lb.draw_leaderboard(True, leadernames, leaderscores, score_writer)

  else:
    lb.draw_leaderboard(False, leadernames, leaderscores, score_writer)

#---events


ball.onclick(startgame) #start game



wn.mainloop()
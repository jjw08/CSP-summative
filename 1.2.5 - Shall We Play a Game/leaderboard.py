import turtle as trtl


# return names in the leaderboard file
def get_names(file_name):
    leaderboard_file = open(file_name, "r") 

  
    names = []
    for line in leaderboard_file:
      leader_name = ""
      index = 0

      
      while (line[index] != ","):
        leader_name = leader_name + line[index] 
        index = index + 1
      
      
      names.append(leader_name)
   
    leaderboard_file.close()

   
    return names

  
# return scores from the leaderboard file
def get_scores(file_name):
  leaderboard_file = open(file_name, "r")  
  scores = []
  for line in leaderboard_file:
    leader_score = ""    
    index = 0

    
    while(line[index] != ","):
       index += 1 
    index +=1 
    
  
  
    while(line[index] != "\n"):
       leader_score = leader_score + line[index]
       index += 1
    print(leader_score)
      
   
    leader_score = int(leader_score)
    scores.append(leader_score)
  print(scores)
  leaderboard_file.close()


  return scores


# update leaderboard by inserting the current player and score to the list at the correct position
def update_leaderboard(file_name, leader_names, leader_scores, player_name, score,):

  index = 0


  for index in range(len(leader_scores)):

   
    if (score >= leader_scores[index]):
      break
    else:
        index = index + 1
  
    
  
  leader_scores.insert(index, score)
  leader_names.insert(index, player_name)

    
  while len(leader_scores) > 5:
       leader_names.pop()
       leader_scores.pop()

   
  leaderboard_file = open(file_name, "w") 
  
  
  for index in range(len(leader_names)) :
      leaderboard_file.write(leader_names[index] + "," + str(leader_scores[index]) + "\n")
                             
  leaderboard_file.close()
    
  


def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object):
    trtl.tracer(0)
    font_setup = ("Arial", 20, "normal")
    turtle_object.color("white")
    turtle_object.clear() 
    turtle_object.penup()
    turtle_object.goto(300,100)
    turtle_object.hideturtle()
    turtle_object.down()
    trtl.update()
    trtl.tracer(1)
    turtle_object.clear()
    for index in range(len(leader_names)):
      
      turtle_object.write(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]), font=font_setup)
      turtle_object.penup()
      turtle_object.goto(300,int(turtle_object.ycor())-50)
      turtle_object.down()
    turtle_object.penup()
    turtle_object.goto(300,int(turtle_object.ycor())-50)
    turtle_object.pendown()


   
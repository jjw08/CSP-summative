import turtle as trtl
painter = trtl.Turtle()
#Add custom plane turtle
trtl.addshape("plane", ((-64,-8),(-40,8),(32,8),(48,32),(48,8),(40,-8)))

#Create lists
plane_color = [trtl.textinput("Plane color", 'What color do you want the plane to be?')]
plane_shape = ["plane"]
plane_full = []
plane_speed = int((trtl.textinput("Plane Speed", 'How fast should the plane be? (1-10)')))


#Draw runway, add backround
trtl.bgcolor("CadetBlue1")
trtl.tracer(0)
painter.penup()
painter.color("gray20")
painter.goto(-1000,0)
painter.pendown()
painter.begin_fill()
painter.forward(2000)
painter.right(90)
painter.forward(2000)
painter.right(90)
painter.forward(2000)
painter.right(90)
painter.forward(2000)
painter.end_fill()
trtl.update()
trtl.tracer(1)



# create plane
for s in plane_shape:
  t = trtl.Turtle(shape=s)
  c = plane_color.pop()
  t.color(c)
  t.penup()
  
  plane_full.append(t)

startx = 300
starty = 8

for t in plane_full:
   t.goto(startx,starty)
   t.setheading(90)

#trtl.update()


#Make plane movement
t.speed(plane_speed)
t.goto(-200,8)
t.goto(-500,150)


#Ask user if they want to run the program again




wn = trtl.Screen()
wn.mainloop()
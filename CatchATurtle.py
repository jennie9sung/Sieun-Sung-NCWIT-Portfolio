#-----import statements-----
 
import turtle as trtl
 
import random as rand
 
#-----game configuration----
 
turtle_color = "green"
turtle_size = 2
turtle_shape = "turtle"
 
font_setup = ("Arial", 20, "normal")
 
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
 
 
#-----initialize turtle-----
 
turtle = trtl.Turtle()
score_writer = trtl.Turtle()
counter =  trtl.Turtle()
 
score = 0
 
counter.hideturtle()
counter.penup()
counter.goto(150, 130)
 
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-150, 130)
 
turtle.fillcolor(turtle_color)
turtle.shapesize(turtle_size)
turtle.shape(turtle_shape)
 
#-----game functions--------
 
def turtle_clicked(x,y):
    print("You clicked a turtle!")
    update_score()
    change_position()
 
def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
 
def change_position():
    new_xpos = rand.randint(-200,200)
    new_ypos = rand.randint(-150, 150)
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(new_xpos, new_ypos)
    turtle.showturtle()
 
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    turtle.hideturtle()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
 
#-----events----------------
wn = trtl.Screen()
turtle.onclick(turtle_clicked)
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
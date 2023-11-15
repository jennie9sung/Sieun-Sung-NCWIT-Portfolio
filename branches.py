# code


import turtle as trtl

painter = trtl.Turtle()

# leaves - list, loop iterating through the list, various shapes, various colors


painter.penup()
painter.goto(90,50)
painter.pendown()
painter.turtlesize(3)

xc = painter.xcor()
yc = painter.ycor()

# shape of the leaves
painter.shape('circle')
# color of the leaves
lcolor_list = ['red', 'orange', 'yellow']

# right side leaves
times = 4
c = 0
# print leaves with 3 colors, number of leaves decrease by 1 for each color
for lc in lcolor_list:
  pc = lcolor_list[c]
  painter.color(pc)
  
  painter.setheading(100)
  
  for leaves in range (times):
    painter.stamp()
    painter.left(15)
    painter.penup()
    painter.forward(33)
    painter.pendown()
  xc = xc - 25
  painter.penup()
  painter.goto(xc, yc) 
  painter.pendown() 
  c= c+1
  times = times - 1


painter.penup()
painter.goto(-90,50)
painter.pendown()

xc = painter.xcor()
# left side leaves
times = 5
c = 0
# print leaves with 3 colors, number of leaves decrease by 1 for each color
for lc in lcolor_list:
  pc = lcolor_list[c]
  painter.color(pc)
  
  painter.setheading(80)
  
  for leaves in range (times):
    painter.stamp()
    painter.right(15)
    painter.penup()
    painter.forward(33)
    painter.pendown()
  xc = xc + 25
  painter.penup()
  painter.goto(xc, yc) 
  painter.pendown() 
  c= c+1
  times = times - 1



# trunk


painter.color('brown')
painter.pensize(40)
painter.penup()
painter.goto(0,-80)
painter.pendown()
painter.goto(0,50)

# branches - while loop


painter.pensize(8)
# variables
branch = 0
angle = 90

# left side
while(branch <=4):
    painter.penup()
    painter.goto(0,50)
    painter.pendown()
    painter.setheading(angle)
    painter.forward(80)
    branch = branch + 1
    angle = angle + 20
    
branch = 0
angle = 90

# right side
while(branch <=3):
    painter.penup()
    painter.goto(0,50)
    painter.pendown()
    angle = angle - 20
    painter.setheading(angle)
    painter.forward(80)
    branch = branch + 1

# roots - if statement


painter.penup()
painter.goto(0,-80)
painter.pendown()
# variables
root = 0
right_side = 180
left_side = 0

for times in range (6):
    # right side
    if (root<=2):
        right_side = right_side + 20
        painter.setheading(right_side)
        painter.forward(115)
        painter.penup()
        painter.goto(0, -80)
        painter.pendown()
        root = root + 1
    # left side
    else:
        left_side = left_side - 20
        painter.setheading(left_side)
        painter.forward(115)
        painter.penup()
        painter.goto(0, -80)
        painter.pendown()
        root = root + 1


    
painter.hideturtle()

# various sizes through out the entire program



wn = trtl.Screen()
wn.mainloop()
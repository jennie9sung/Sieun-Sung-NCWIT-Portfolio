#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

wn = trtl.Screen()
wn.screensize(canvwidth = 0.8, canvheight = 0.8)

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle"]
horiz_colors = ["red", "blue", "green", "orange", "purple"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo"]

tloc = 50
m=4
for ts in turtle_shapes:
  ts = turtle_shapes[m]
  hc = horiz_colors[m]
  vc = vert_colors[m]

  ht = trtl.Turtle(shape=ts)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = hc
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)

  vt = trtl.Turtle(shape=ts)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vc
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  m = m-1
  tloc += 50
  

# TODO: move turtles across and down screen, stopping for collisions
"""
for step in range(50):
	# do something
"""


m=0
step = 0
while step < 50:

  for t in horiz_turtles:
    t.forward(5)
  for t in vert_turtles:
    t.forward(5)
  for ht in horiz_turtles:
    for vt in vert_turtles:
      if(abs(ht.xcor()-vt.xcor()) < 20):
        if(abs(ht.ycor()-vt.ycor()) < 20):
          ht.shape('classic')
          vt.shape('classic')
          ht.fillcolor('gold')
          vt.fillcolor('gold')
          ht.left(180)
          vt.left(180)
          # have to go back to original shape and color
          
          ts = turtle_shapes[m]
          hc = horiz_colors[m]
          vc = vert_colors[m]
          ht.shape(ts)
          h_color=hc
          ht.fillcolor(h_color)
          vt.shape(ts)
          v_color = vc
          vt.fillcolor(v_color)
          m = m +1
        
  step = step + 1

for ht in horiz_turtles:
    for vt in vert_turtles:
        vt.fillcolor('brown')
        ht.fillcolor('brown')



wn = trtl.Screen()
wn.mainloop()

#created by Pratishtha and Jennifer on Nov 8, 2022
#Video description : This program is a game to design your own pet. It will require the users to press keyboards and give inputs through the terminal. The user first picks an animal and selects animal color. Then the user will choose decorations, background, and the name of the pet. The images are displayed based on the inputs of the users and it will display the 'sparkling.gif' image to tell that the game is ended.
# reused code from greeksforgreeks.     Website link:  # I changed the code from greeksforgreeks to check if an item is in the list.   Website link: https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/
import turtle as trtl
import random as rand

#---turtles---
writer = trtl.Turtle()  # write the instructions
animal = trtl.Turtle()  # show the animal images
dec = trtl.Turtle()   # show the decoration images
sparkling = trtl.Turtle()   # show the sparkling.gif images
comment = trtl.Turtle()    # write comments for decoration choices


wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
# set the starting background
wn.bgpic("rainbowbackground.gif")
 
#---images---
originalH = "originalH.gif"
pinkH = "pinkH.gif"
greenH = "greenH.gif"
blueH = "blueH.gif"
 
originalR = "originalR.gif"
pinkR = "pinkR.gif"
greenR = "greenR.gif"
blueR = "blueR.gif"
 
sg = "sunglasses.gif"
sh = "santahat.gif"
ht = "heart.gif"
 
wh = "wizardhat.gif"
rb = "ribbon.gif"
st = "star.gif"

forest = "forest.gif"
castle = "castle.gif"
beach = "beach.gif"

sk = "sparkling.gif"


wn.addshape(originalH)
wn.addshape(pinkH)
wn.addshape(greenH)
wn.addshape(blueH)
wn.addshape(originalR)
wn.addshape(pinkR)
wn.addshape(greenR)
wn.addshape(blueR)
 
wn.addshape(sg)
wn.addshape(sh)
wn.addshape(ht)
wn.addshape(wh)
wn.addshape(rb)
wn.addshape(st)

wn.addshape(sk)

 
#---lists---

decoration_1 = ["sunglasses", "santahat", "heart"]  # list with decoration items that will make the comment turtle write "Stylish!"
name_color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'white'] # list with color items for the name written by the writer turtle
 
#---write the title of the game---
writer.hideturtle()
writer.penup()
writer.goto(-180,35)
writer.color('blue')
writer.write("Design a Pet", font = ("Fixedsys", 44, "bold"))
 
writer.goto(-100,-30)
writer.color('black')
writer.write("Press g to start", font = ("System", 20, "bold"))

# This part of the program will display the starting screen of the game with basic instructions.
 
 
#---functions---
def hideturtle(turtle):
    turtle.hideturtle()
    turtle.penup()

# this functions reduces the complicity and the length of the code by using turtle names as a parameter to hide the turtle and make the turtle pen up.
 
def clickg():
    writer.clear()
    print_animal(writer, animal)

# this will be called by onkeypress(clickg,'g') so that when the user presses g, it will call the print_animal function of which the parameter (write, draw) is replaced with (writer, animal).

def print_animal(write, draw):
    # give instructions and ask the user input on rabbit or hamster.
    write.goto(-225,-10)
    write.write("Choose an animal: rabbit or hamster   ", font = ("System", 18))
    animal_type = input("Choose an animal: rabbit or hamster    ")
    write.clear()
    write.goto(-280,-10)
    writer.clear()
    # clears everything written before and give instructions and ask the user to type one thing from original, pink, green, and blue.
    write.write("Choose a color: original / pink / green / blue    ", font = ("System", 18))
    color=input("Choose a color: original / pink / green / blue    ")
    write.clear()
    # the image setted for the animal turtle will all differ from the input of the user. For example, if the user types hamster and pink, it will set the animal turtle's shape as 
    if (animal_type == 'hamster'):  # animal_type == hamster, but color differs
        if (color == 'original'):
            draw.shape(originalH)
            draw.showturtle()
        elif (color == 'pink'):
            draw.shape(pinkH)
            draw.showturtle()
        elif (color == 'green'):
            draw.shape(greenH)
            draw.showturtle()
        else:
            draw.shape(blueH)
            draw.showturtle()
    else:   # animal_type == rabbit, but color differs
        if (color == 'original'):
            draw.shape(originalR)
            draw.showturtle()
        elif (color == 'pink'):
            draw.shape(pinkR)
            draw.showturtle()
        elif (color == 'green'):
            draw.shape(greenR)
            draw.showturtle()
        else:
            draw.shape(blueR)
            draw.showturtle()
    dec_options() # calls the dec_options function to move on to the next
 
def dec_type(turtle, image):
    turtle.shape(image)
    turtle.showturtle()
# this function contributes to the abstraction by using 2 parameters to change the shape of the decoration image based on the user input
# this function will be called in the 
 
def dec_options(): # this function asks for an input from the user to select a decoration type, print the decoration image, and then print Stylish! or Good choice!.
    writer.clear() # clear everything written before and give instructions and ask the user to type one of the decorations.
    writer.goto(-308, 150)
    writer.write("Choose one decoration: sunglasses / ribbon / santahat / wizardhat / heart / star", font = ("System", 13))
    dec_choice = input("Choose one decoration: sunglasses / ribbon / santahat / wizardhat / heart / star    ")
    writer.clear()
 
    if (dec_choice == 'sunglasses'): # calls the dec_type function to set the dec turtle image based on the user input.
        dec_type(dec, sg)
    elif (dec_choice == 'ribbon'):
        dec_type(dec, rb)
    elif (dec_choice == 'santahat'):
        dec_type(dec, sh)
    elif (dec_choice == 'wizardhat'):
        dec_type(dec, wh)
    elif (dec_choice == 'heart'):
        dec_type(dec, ht)
    else:
        dec_type(dec, st)
 # I changed the code from greeksforgreeks to check if an item is in the list.   Website link: https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/
    if dec_choice in decoration_1: # if the user input can be found in the decoration_1 list, it will write "Stylish!"
        comment.color('red')
        comment.goto(-220, 30)
        comment.write("Stylish!", font = ("System", 25))
    
    else: # if not, it will print "Good choice!"
        comment.color('blue')
        comment.goto(110, 30)
        comment.write("Good choice!", font = ("System", 22))
   
    writer.goto(-290, 140)
    # instructions for moving the dec turtle and how to move to the next step.
    writer.write("Use A, W, S, D to move the decorative item and press E when you are done!", font = ("System", 14))
 
def up(): # when the user presses the w key, the dec turtle will move 5 units up.
    dec.setheading(90)
    dec.forward(5)
def down(): # when the user presses the s key, the dec turtle will move 5 units down.
    dec.setheading(270)
    dec.forward(5)
def left(): # when the user presses the a key, the dec turtle will move 5 units left.
    dec.setheading(180)
    dec.forward(5)
def right(): # when the user presses the d key, the dec turtle will move 5 units right.
    dec.setheading(0)
    dec.forward(5)
 
def background(): # this function will let the users to choose the background image by asking for user input and set the background based on it.
    writer.clear()
    comment.clear() # give instructions and ask the user to choose from forest, castle, and beach.
    writer.write("Choose one background: forest / castle / beach", font = ("System", 13))
    back_choice = input("Choose one background: forest / castle / beach    ")
    if (back_choice == 'forest'): # set the background based on the user input.
            wn.bgpic("forest.gif")
    elif (back_choice == 'castle'):
            wn.bgpic("castle.gif")
    elif (back_choice == 'beach'):
            wn.bgpic("beach.gif")
    writer.clear()
    ask_name() # call the ask_name function

def ask_name(): # ask for user inputs for the pet name, iterate through the name_color list to change colors when writing the name, call the sparkling.gif image, and set the writer color to white.
    writer.clear()
    writer.color('white')
    writer.write("Name your pet!", font = ("System", 20, "bold"))
    pet_name = input("Name your pet:    ")
    writer.clear()
    for i in range(10):
        c=0
        for count in name_color:
            color = name_color[c]
            writer.color(color)
            writer.goto(-35, -180)
            writer.write(pet_name, font = ("System", 30, "bold"))
            c = c + 1
    sparkling.shape(sk)
    sparkling.showturtle()
    writer.write(pet_name, font = ("System", 30, "bold"))



#---function calls---
hideturtle(writer)
hideturtle(animal)
hideturtle(dec)
hideturtle(sparkling)
hideturtle(comment)

wn.onkeypress(clickg, "g")

wn.onkeypress(up, 'w')
wn.onkeypress(down, 's')
wn.onkeypress(left, 'a')
wn.onkeypress(right, 'd')
wn.onkeypress(background, 'e')
 
 
wn.listen()
 
wn.mainloop()

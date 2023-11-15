#---import---
import turtle as trtl
import random as rand
import keyboard

#---set screen---
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

#---turtles---
intro = trtl.Turtle() # write the title
start = trtl.Turtle() # when clicked, call procedure buttoncolor, and when the click is released, call procedure NumberOfBalls
writer = trtl.Turtle() # write intro's instruction to click on the green circle
instruction = trtl.Turtle() # writes instruction about setting the range and draws a blue box, and writes numbers
warning = trtl.Turtle() # writes a message to choose a number between 2~9
button = trtl.Turtle() # when clicked, call procedure test1
draw = trtl.Turtle() # draws and writes a filled circle with a random color and a random number
next = trtl.Turtle() # gives instruction to press N to move on, write THE END
back = trtl.Turtle() # gives instruction to press R to restart the number draw


#---lists---
alltrtl= [intro, start, writer, instruction, warning, button, draw, next, back] # all turtles
color_lst = ['red', 'orange', 'yellow', 'chartreuse', 'green', 'aqua', 'darkblue', 'mediumslateblue', 'darkviolet', 'hotpink'] # all available colors
colors = ['red', 'orange', 'yellow', 'chartreuse', 'green', 'aqua', 'darkblue', 'mediumslateblue', 'darkviolet', 'hotpink'] 
# the list colors is a backup list of colors to use to reset color_lst
# there is one more list named number_lst in procedure test1.

#---variables---
a = 0
b = 0

#---functions---

# used with a for loop iterating list alltrtl to clear the entire screen before moving on
def hideturtle(turtle): # hides and clears the turtle from the screen  
    turtle.hideturtle()
    turtle.penup()
    turtle.clear()

# opening scene of the program.
# title, instruction to move on given.
def introduction(): 
    intro.goto(-300, 50)
    intro.color('mediumslateblue')
    intro.write("Number Draw", font = ("Algerian", 70))
    start.shape("circle")
    start.goto(230,-40)
    start.shapesize(3,3,1)
    start.showturtle()
    start.color("palegoldenrod")
    writer.goto(-240, -60)
    writer.color("darkseagreen")
    writer.write("Click on the button to start.", font = ("System", 25))

# a procedure to draw a rectangle, used in procedure NumberOfBalls
def drawr(trtl, n):
    trtl.forward(n)
    trtl.left(90)

def NumberOfBalls(a,b):
    # clear all the turtles and writings from introduction
    for t in alltrtl:
        hideturtle(t)
    # write instruction of how to set the number range for the number draw
    instruction.goto(-600,300)
    instruction.write("How many numbers?", font = ("Times New Roman", 30))
    instruction.goto(-600,260)
    instruction.color("cadetblue")
    instruction.write("Type a number between 2~9.", font = ("Times New Roman", 30, "bold"))
    instruction.goto(-100, -130)
    instruction.pendown()
    instruction.width(3)
    instruction.color("cornflowerblue")
    instruction.speed(11)
    # draw a rectangle that a number that the user typed will appear
    drawr(instruction, 200)
    drawr(instruction, 260)
    drawr(instruction, 200)
    drawr(instruction, 260)
    instruction.penup()
    # call procedure choice to accept user input
    choice()
    # use the global variable assign which was assigned a number from procedure choice
    setrange(assign)

# this procedure allows to recieve the user input again
def error(a,b):
    # call procedure choice to accept user input
    choice()
    # use the global variable assign which was assigned a number from procedure choice
    setrange(assign)

# writes a number inside the rectangle
def writenum(k):
    instruction.goto(-30,-60)
    instruction.color("black")
    instruction.write(k, font = ('Times New Roman', 80))

# saves the range based on the user input
def setrange(n):
        global total
        # if user input was bigger than 1, the number that user typed will be written in the rectangle
        while n>1:    
            warning.clear()
            if n == 2:
                writenum('2')
            elif n==3:
                writenum('3')
            elif n==4:
                writenum('4')
            elif n==5:
                writenum('5')
            elif n==6:
                writenum('6')
            elif n==7:
                writenum('7')
            elif n==8:
                writenum('8')
            elif n==9:
                writenum('9')
            
            # a red button and a instruction to click on it in order to draw a number will appear on the screen
            button.color('orangered')
            button.goto(250,-17)
            button.write('← Click to draw a number!', font = ("Times New Roman", 25))
            button.goto(200,0)
            button.turtlesize(4)
            button.shape('circle')
            button.showturtle()
            total = int(n)
            break
        # if user input was smaller or equal to 1, a warning message will appear on the screen
        else:
            warning.clear()
            warning.goto(-260, 150)
            warning.color('red')
            warning.write("Please type a number between 2~9!!", font = ("Times New Roman", 30))
            # give another chance to put the input(choose another number)
            error(a,b)

# when button is clicked procedure called
def test1(x,y):
    # clear screen
    for t in alltrtl:
        hideturtle(t)
    # creates a global list with numbers from 1 to the maximum number the user chose    
    global number_lst
    number_lst = list(range(1,total+1))
    # calls procedure test2 to draw and write the number ball
    test2(x,y)


def test2(x,y):
    # when the number of items in the number_lst is bigger than 0
    while len(number_lst)>0:
        #draws a circle with a random number from number_lst and random color from color_lst
        currentc = rand.choice(color_lst)
        draw.speed(11)

        # Citing fillcolor(), begin_fill() from https://www.geeksforgeeks.org/draw-color-filled-shapes-in-turtle-python/#
        draw.fillcolor(currentc)
        draw.begin_fill()
        # end cited code

        draw.color(currentc)
        draw.goto(0,-200)
        draw.pendown()
        draw.circle(200)

        # Citing end_fill() from https://www.geeksforgeeks.org/draw-color-filled-shapes-in-turtle-python/#
        draw.end_fill()
        # end cited code
        currentn = rand.choice(number_lst)
        draw.goto(-35,-70)
        draw.color('black')
        draw.write(currentn, font = ('Times New Roman', 100, 'bold'))

        # used color and number are removed from the list
        color_lst.remove(currentc)
        number_lst.remove(currentn)
        
        # print the current list in order to check if errors are happening
        print(color_lst)
        print(number_lst)

        # gives instruction to press N to drag another number
        next.shape('circle')
        next.color('red')
        next.goto(315,285)
        next.write('Press N to move on.', font = ('Times New Roman', 20))
        next.goto(300,300)
        
        # gives instruction to press R to change the range and restatrt
        back.shape('triangle')
        back.color('green')
        back.goto(315, 235)
        back.write('Press R to restart.', font = ('Times New Roman', 20))
        back.goto(300,250)

        next.showturtle()
        back.showturtle()


        while True:
            # Citing keyboard.is_pressed() from https://pypi.org/project/keyboard/ (module download)
            # if the user presses n
            if keyboard.is_pressed('n'):
                #end cited code

                # calls procedure test2 to make another number ball appear
                for t in alltrtl:
                    hideturtle(t)
                test2(x,y)
                break

            # Citing keyboard.is_pressed() from https://pypi.org/project/keyboard/ (module download)
            # if the user presses r
            elif keyboard.is_pressed('r'):
                # end cited code

                # resets all the lists and calls procedure NumberOfBalls to ask for user input again 
                for t in alltrtl:
                    hideturtle(t)
                number_lst.clear()
                color_lst.clear()
                color_lst.extend(colors)
                NumberOfBalls(x,y)
                break
        break
    # when the number of items in the list is less than 1,
    # remove everything related to the turtle next
    hideturtle(next)
    # make the turtle next write the end
    next.goto(-100,0)
    next.color('hotpink')
    next.write("THE END", font = ('Times New Roman', 50))
    back.shape('triangle')
    back.color('green')
    back.goto(315, 235)
    # still give options to restart
    back.write('Press R to restart.', font = ('Times New Roman', 20))
    back.goto(300,250)
    while True:
        # Citing keyboard.is_pressed() from https://pypi.org/project/keyboard/ (module download)
        if keyboard.is_pressed('r'):
            # end cited code
            
            # resets all the lists and calls procedure NumberOfBalls to ask for user input again 
            for t in alltrtl:
                hideturtle(t)
            number_lst.clear()
            NumberOfBalls(x,y)
            break

# changes the button color when clicked
# in order to inform the user that the button is being clicked
def buttoncolor(x,y):
    start.fillcolor("darksalmon")

# procedure choice gathers the user input to set the range of numbers
def choice():
    global assign
    while True:

        # Citing keyboard.is_pressed() from https://pypi.org/project/keyboard/ (module download)
        # the number of keyboard the user presses will be assigned as the assign value
        if keyboard.is_pressed('2'):
            assign = 2
            break
        elif keyboard.is_pressed('3'):
            assign = 3
            break
        elif keyboard.is_pressed('4'):
            assign = 4
            break
        elif keyboard.is_pressed('5'):
            assign = 5
            break
        elif keyboard.is_pressed('6'):
            assign = 6
            break
        elif keyboard.is_pressed('7'):
            assign= 7
            break
        elif keyboard.is_pressed('8'):
            assign = 8
            break
        elif keyboard.is_pressed('9'):
            assign = 9
            break
        elif keyboard.is_pressed('1'):
            assign = 1
            break
        elif keyboard.is_pressed('0'):
            assign = 0
            break
        # end cited code
    

#---function calls---
for t in alltrtl: # clears the entire screen before moving on
    hideturtle(t)

introduction() # starts the number draw program

button.onclick(test1)

start.onclick(buttoncolor)
start.onrelease(NumberOfBalls)



wn.listen()
 
wn.mainloop()





# https://pypi.org/project/keyboard/
# https://www.geeksforgeeks.org/draw-color-filled-shapes-in-turtle-python/
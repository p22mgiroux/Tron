import turtle

# If the bikes arent moving, and the bike isnt facing left or already facing right, turn the orange bike to the right and update the lists
def right1(override = False):
    if moving[0] == 1 or override:
        if r1[0] != 1 and l1[0] != 1:
            if u1[0] == 1:
                u1[0] = 0
                r1[0] = 1
                toby.right(90)
            else:
                d1[0] = 0
                r1[0] = 1
                toby.left(90)

# If the bikes arent moving, and the bike isnt facing right or already facing left, turn the orange bike to the left and update the lists
def left1(override = False):
    if moving[0] == 1 or override:
        if l1[0] != 1 and r1[0] != 1:
            if u1[0] == 1:
                u1[0] = 0
                l1[0] = 1
                toby.left(90)
            else:
                d1[0] = 0
                l1[0] = 1
                toby.right(90)

# If the bikes arent moving, and the bike isnt facing down or already facing up, turn the orange bike up and update the lists
def up1(override = False):
    if moving[0] == 1 or override:
        if u1[0] != 1 and d1[0] != 1:
            if r1[0] == 1:
                r1[0] = 0
                u1[0] = 1
                toby.left(90)
            else:
                l1[0] = 0
                u1[0] = 1
                toby.right(90)

# If the bikes arent moving, and the bike isnt facing up or already facing down, turn the orange bike down and update the lists
def down1(override = False):
    if moving[0] == 1 or override:
        if d1[0] != 1 and u1[0] != 1:
            if r1[0] == 1:
                r1[0] = 0
                d1[0] = 1
                toby.right(90)
            else:
                l1[0] = 0
                d1[0] = 1
                toby.left(90)

# If the bikes arent moving, and the bike isnt facing right or already facing left, turn the blue bike to the left and update the lists
def right2(override = False):
    if moving[0] == 1 or override:
        if r2[0] != 1 and l2[0] != 1:
            if u2[0] == 1:
                u2[0] = 0
                r2[0] = 1
                twoby.right(90)
            else:
                d2[0] = 0
                r2[0] = 1
                twoby.left(90)

# If the bikes arent moving, and the bike isnt facing right or already facing left, turn the blue bike to the left and update the lists
def left2(override = False):
    if moving[0] == 1 or override:
        if l2[0] != 1 and r2[0] != 1:
            if u2[0] == 1:
                u2[0] = 0
                l2[0] = 1
                twoby.left(90)
            else:
                d2[0] = 0
                l2[0] = 1
                twoby.right(90)

# If the bikes arent moving, and the bike isnt facing down or already facing up, turn the blue bike up and update the lists
def up2(override = False):
    if moving[0] == 1 or override:
        if u2[0] != 1 and d2[0] != 1:
            if r2[0] == 1:
                r2[0] = 0
                u2[0] = 1
                twoby.left(90)
            else:
                l2[0] = 0
                u2[0] = 1
                twoby.right(90)

# If the bikes arent moving, and the bike isnt facing up or already facing down, turn the blue bike down and update the lists
def down2(override = False):
    if moving[0] == 1 or override:
        if d2[0] != 1 and u2[0] != 1:
            if r2[0] == 1:
                r2[0] = 0
                d2[0] = 1
                twoby.right(90)
            else:
                l2[0] = 0
                d2[0] = 1
                twoby.left(90)

# When enter is pressed, if the bikes are not moving, set moving to -1 so enter cant be pressed again, then set the bikes to face each other if they are not already
def enter():
    if moving[0] == 0:
        moving[0] = -1
        if r1[0] == 0:
            up1(True)
            right1(True)
        if l2[0] == 0:
            up2(True)
            left2(True)
# Lift the bikes pens and clear their lines
        toby.penup()
        twoby.penup()
        toby.clear()
        twoby.clear()
# Clear the list of coords and add the starting positions to it
        passed_coords.clear()
        passed_coords.extend([(-255,0),(255,0)])
# Set the speed of the bikes so the players can see them move
        toby.speed(5)
        twoby.speed(5)
# Clear the bg pic
        window.bgpic('nopic')
# Make the bikes smaller (from start screen), and move them to their starting positions
        toby.shapesize(.5)
        toby.goto(-255,0)
        twoby.shapesize(.5)
        twoby.goto(255,0)
# Make any turtle that wasnt visible before, visible
        toby.showturtle()
        twoby.showturtle()
# Raise the turtle speed back up and put their pens back down
        toby.speed(0)
        twoby.speed(0)
        toby.pendown()
        twoby.pendown()

# Countdown using a turtle in the center of the screem (window.ontimer(window.bgpic('img'))) wasnt working
        img.showturtle()
        window.ontimer(img.shape('three.gif'),1000)
        window.ontimer(img.shape('two.gif'),1000)
        window.ontimer(img.shape('one.gif'),1000)
        img.hideturtle()

# Allow the turtle to move again
        moving[0] = 1

    
# Initialize the screen with dimensions of 850x850
window = turtle.Screen()
window.setup(850,850)

# Set the bg color, and load the start screen
window.bgcolor("#202020")
window.bgpic('start.png')

# Load all the gifs for the counddown and win/tie screens
window.addshape('three.gif')
window.addshape('two.gif')
window.addshape('one.gif')
window.addshape('tie.gif')
window.addshape('blue.gif')
window.addshape('orange.gif')

# Register the bike as a valid turtle shape (146 points)
turtle.register_shape("tron", ((-50,0),(-49,5),(-45,5),(-49,5),(-48,10),(-46,10),(-44,11),(-25,11),(-23,10),(-15,9),(-12,6),(-11,7),(-11,4),(-8,4),(-6,3),(-5,1),(-5,-1),(-6,-3),(-8,-4),(-11,-4),(-11,-7),(-11,-4),(-15,-3),(-17,-2),(-18,0),(-17,2),(-15,3),(-11,4),(-11,7),(-13,11),(-23,15),(-26,14),(-26,11),(-30,11),(-30,13),(-31,13),(-31,11),(-34,11),(-34,12),(-33,12),(-33,14),(-30,14),(-31,16),(-28,21),(-26,21),(-23,19),(-11,16),(-7,13),(-4,9),(1,9),(3,8),(4,7),(4,6),(6,6),(5,12),(5,14),(6,16),(8,17),(10,17),(22,16),(23,17),(24,17),(25,18),(26,18),(26,19),(28,19),(28,11),(25,11),(23,10),(21,11),(19,10),(17,11),(12,11),(19,8),(20,10),(23,10),(25,11),(44,11),(46,10),(48,10),(50,0),(40,0),(50,0),(48,-10),(46,-10),(44,-11),(25,-11),(23,-10),(20,-10),(19,-8),(12,-11),(17,-11),(19,-10),(21,-11),(23,-10),(25,-11),(28,-11),(28,-19),(26,-19),(26,-18),(25,-18),(24,-17),(23,-17),(22,-16),(10,-17),(8,-17),(6,-16),(5,-14),(5,-12),(6,-6),(4,-6),(4,-7),(3,-8),(1,-9),(-4,-9),(-7,-13),(-11,-16),(-23,-19),(-26,-21),(-28,-21),(-31,-16),(-30,-14),(-33,-14),(-33,-12),(-34,-12),(-34,-11),(-31,-11),(-31,-13),(-30,-13),(-30,-11),(-26,-11),(-26,-14),(-23,-15),(-13,-11),(-11,-7),(-12,-6),(-15,-9),(-23,-10),(-25,-11),(-44,-11),(-46,-10),(-48,-10),(-49,-5),(-45,-5),(-49,-5),(-50,0)))
# Initialize all three turtles used and hide them
img = turtle.Turtle()
img.hideturtle()
toby = turtle.Turtle()
twoby = turtle.Turtle()
toby.hideturtle()
twoby.hideturtle()
# set the shapes, sizes and colors of the turtles
toby.shape("tron")
twoby.shape("tron")
toby.pensize(5)
twoby.pensize(5)
toby.shapesize(3)
twoby.shapesize(3)
toby.pencolor("gold")
twoby.pencolor("cyan")

# Pick the turtles pens up to move them into their proper positions on the start screen
toby.penup()
twoby.penup()
toby.speed(0)
twoby.speed(0)
# Set the tilt angle so the bikes face the correct ways
twoby.tiltangle(90)
toby.tiltangle(-90)
toby.goto(-210,80)
twoby.goto(210,80)
# Make the bikes visible
toby.showturtle()
twoby.showturtle()

# All lists that can be acessed globally
r1 = [1]
l1 = [0]
u1 = [0]
d1 = [0]
r2 = [0]
l2 = [1]
u2 = [0]
d2 = [0]
passed_coords = []
moving = [0]

# Button handlers
turtle.onkeypress(enter, "Return")
turtle.onkeypress(right1, "d")
turtle.onkeypress(left1, "a")
turtle.onkeypress(up1, "w")
turtle.onkeypress(down1, "s")
turtle.onkeypress(right2, "Right")
turtle.onkeypress(left2, "Left")
turtle.onkeypress(up2, "Up")
turtle.onkeypress(down2, "Down")

# Main gameloop
while True:
# If the bikes arent moving, always keep checking for updates
    if moving[0] == 0:
        toby.forward(0)
        twoby.backward(0)
        window.listen()

    if moving[0] == 1:
        
# Moves the bikes together
        toby.forward(15)
        twoby.backward(15)

# If a bikes position is already in the list, hide it
        if (round(toby.xcor()), round(toby.ycor())) in passed_coords:
            toby.hideturtle()
            moving[0] = 0
        if (round(twoby.xcor()), round(twoby.ycor())) in passed_coords:
            twoby.hideturtle()
            moving[0] = 0

# If a turtle goes out of bounds, hide it
        if round(toby.xcor()) <= -410 or round(toby.xcor()) >= 410:
            toby.hideturtle()
            moving[0] = 0
        if round(toby.ycor()) <= -410 or round(toby.ycor()) >= 410:
            toby.hideturtle()
            moving[0] = 0
        if round(twoby.xcor()) <= -410 or round(twoby.xcor()) >= 410:
            twoby.hideturtle()
            moving[0] = 0
        if round(twoby.ycor()) <= -410 or round(twoby.ycor()) >= 410:
            twoby.hideturtle()
            moving[0] = 0

# If both of the turtles are overlapping, hide them both
        if (round(toby.xcor()), round(toby.ycor())) == (round(twoby.xcor()), round(twoby.ycor())):
            toby.hideturtle()
            twoby.hideturtle()
            moving[0] = 0

# Append the current bikes coordinates to the list
        passed_coords.append((round(toby.xcor()), round(toby.ycor())))
        passed_coords.append((round(twoby.xcor()), round(twoby.ycor())))

# Handles win/tie screens based on which turtles are visible
        if toby.isvisible() and twoby.isvisible() == False:
            img.shape('orange.gif')
            img.showturtle()
        if twoby.isvisible() and toby.isvisible() == False:
            img.shape('blue.gif')
            img.showturtle()
        if toby.isvisible() == False and twoby.isvisible() == False:
            img.shape('tie.gif')
            img.showturtle()

# Listen for updates
        window.listen()
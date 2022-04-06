import turtle

def right1():
    if r1[0] != 1 and l1[0] != 1:
        if u1[0] == 1:
            u1[0] = 0
            r1[0] = 1
            toby.right(90)
        else:
            d1[0] = 0
            r1[0] = 1
            toby.left(90)


def left1():
    if l1[0] != 1 and r1[0] != 1:
        if u1[0] == 1:
            u1[0] = 0
            l1[0] = 1
            toby.left(90)
        else:
            d1[0] = 0
            l1[0] = 1
            toby.right(90)

def up1():
    if u1[0] != 1 and d1[0] != 1:
        if r1[0] == 1:
            r1[0] = 0
            u1[0] = 1
            toby.left(90)
        else:
            l1[0] = 0
            u1[0] = 1
            toby.right(90)

def down1():
    if d1[0] != 1 and u1[0] != 1:
        if r1[0] == 1:
            r1[0] = 0
            d1[0] = 1
            toby.right(90)
        else:
            l1[0] = 0
            d1[0] = 1
            toby.left(90)

def right2():
    if r2[0] != 1 and l2[0] != 1:
        if u2[0] == 1:
            u2[0] = 0
            r2[0] = 1
            twoby.right(90)
        else:
            d2[0] = 0
            r2[0] = 1
            twoby.left(90)


def left2():
    if l2[0] != 1 and r2[0] != 1:
        if u2[0] == 1:
            u2[0] = 0
            l2[0] = 1
            twoby.left(90)
        else:
            d2[0] = 0
            l2[0] = 1
            twoby.right(90)

def up2():
    if u2[0] != 1 and d2[0] != 1:
        if r2[0] == 1:
            r2[0] = 0
            u2[0] = 1
            twoby.left(90)
        else:
            l2[0] = 0
            u2[0] = 1
            twoby.right(90)

def down2():
    if d2[0] != 1 and u2[0] != 1:
        if r2[0] == 1:
            r2[0] = 0
            d2[0] = 1
            twoby.right(90)
        else:
            l2[0] = 0
            d2[0] = 1
            twoby.left(90)

def enter():
    window.bgpic('nopic')
    toby.pendown()
    twoby.pendown()
    toby.showturtle()
    twoby.showturtle()
    moving[0] = 1
    

window = turtle.Screen()
window.setup(850,850)
window.bgcolor("#202020")
window.bgpic('start.png')
twoby = turtle.Turtle()
toby = turtle.Turtle()
toby.hideturtle()
twoby.hideturtle()
turtle.register_shape("tron", ((-50,0),(-49,5),(-45,5),(-49,5),(-48,10),(-46,10),(-44,11),(-25,11),(-23,10),(-15,9),(-12,6),(-11,7),(-11,4),(-8,4),(-6,3),(-5,1),(-5,-1),(-6,-3),(-8,-4),(-11,-4),(-11,-7),(-11,-4),(-15,-3),(-17,-2),(-18,0),(-17,2),(-15,3),(-11,4),(-11,7),(-13,11),(-23,15),(-26,14),(-26,11),(-30,11),(-30,13),(-31,13),(-31,11),(-34,11),(-34,12),(-33,12),(-33,14),(-30,14),(-31,16),(-28,21),(-26,21),(-23,19),(-11,16),(-7,13),(-4,9),(1,9),(3,8),(4,7),(4,6),(6,6),(5,12),(5,14),(6,16),(8,17),(10,17),(22,16),(23,17),(24,17),(25,18),(26,18),(26,19),(28,19),(28,11),(25,11),(23,10),(21,11),(19,10),(17,11),(12,11),(19,8),(20,10),(23,10),(25,11),(44,11),(46,10),(48,10),(50,0),(40,0),(50,0),(48,-10),(46,-10),(44,-11),(25,-11),(23,-10),(20,-10),(19,-8),(12,-11),(17,-11),(19,-10),(21,-11),(23,-10),(25,-11),(28,-11),(28,-19),(26,-19),(26,-18),(25,-18),(24,-17),(23,-17),(22,-16),(10,-17),(8,-17),(6,-16),(5,-14),(5,-12),(6,-6),(4,-6),(4,-7),(3,-8),(1,-9),(-4,-9),(-7,-13),(-11,-16),(-23,-19),(-26,-21),(-28,-21),(-31,-16),(-30,-14),(-33,-14),(-33,-12),(-34,-12),(-34,-11),(-31,-11),(-31,-13),(-30,-13),(-30,-11),(-26,-11),(-26,-14),(-23,-15),(-13,-11),(-11,-7),(-12,-6),(-15,-9),(-23,-10),(-25,-11),(-44,-11),(-46,-10),(-48,-10),(-49,-5),(-45,-5),(-49,-5),(-50,0)))
toby.shape("tron")
twoby.shape("tron")
toby.pensize(5)
twoby.pensize(5)
toby.shapesize(.5)
twoby.shapesize(.5)
toby.pencolor("cyan")
twoby.pencolor("gold")

toby.penup()
twoby.penup()
twoby.tiltangle(90)
toby.tiltangle(-90)
twoby.speed(0)
toby.speed(0)
toby.goto(-300,0)
twoby.goto(300,0)


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


turtle.onkeypress(enter, "Return")
while moving[0] == 0:
    toby.forward(0)
    twoby.backward(0)
    window.listen()

while moving[0] == 1:
    turtle.onkeypress(right1, "d")
    turtle.onkeypress(left1, "a")
    turtle.onkeypress(up1, "w")
    turtle.onkeypress(down1, "s")
    turtle.onkeypress(right2, "Right")
    turtle.onkeypress(left2, "Left")
    turtle.onkeypress(up2, "Up")
    turtle.onkeypress(down2, "Down")

    toby.forward(15)
    twoby.backward(15)

    if (round(toby.xcor()), round(toby.ycor())) in passed_coords:
        toby.hideturtle()
        moving[0] = 0
    if (round(twoby.xcor()), round(twoby.ycor())) in passed_coords:
        twoby.hideturtle()
        moving[0] = 0
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
    if (round(toby.xcor()), round(toby.ycor())) == (round(twoby.xcor()), round(twoby.ycor())):
        toby.hideturtle()
        twoby.hideturtle()
        moving[0] = 0

    passed_coords.append((round(toby.xcor()), round(toby.ycor())))
    passed_coords.append((round(twoby.xcor()), round(twoby.ycor())))
        
    window.listen()
window.mainloop()

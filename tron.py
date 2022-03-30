import turtle

def right1():
    r1[0] = 1

def left1():
    l1[0] = 1

def right2():
    r2[0] = 1

def left2():
    l2[0] = 1
window = turtle.Screen()
window.setup(1000,1000)
window.bgcolor("#202020")
twoby = turtle.Turtle()
toby = turtle.Turtle()
turtle.register_shape("tron", ((-50,0),(-48,10),(-46,10),(-44,11),(-25,11),(-23,10),(-15,9),(-12,6),(-11,7),(-11,4),(-8,4),(-6,3),(-5,1),(-5,-1),(-6,-3),(-8,-4),(-11,-4),(-11,-7),(-11,-4),(-15,-3),(-17,-2),(-18,0),(-17,2),(-15,3),(-11,4),(-11,7),(-13,11),(-23,15),(-26,14),(-26,11),(-30,11),(-30,13),(-31,13),(-31,11),(-34,11),(-34,12),(-33,12),(-33,14),(-30,14),(-31,16),(-28,21),(-26,21),(-23,19),(-11,16),(-7,13),(-4,9),(1,9),(3,8),(4,7),(4,6),(6,6),(5,12),(5,14),(6,16),(8,17),(10,17),(22,16),(23,17),(24,17),(25,18),(26,18),(26,19),(28,19),(28,11),(25,11),(23,10),(21,11),(19,10),(17,11),(12,11),(19,8),(20,10),(23,10),(25,11),(44,11),(46,10),(48,10),(50,0),(48,-10),(46,-10),(44,-11),(25,-11),(23,-10),(20,-10),(19,-8),(12,-11),(17,-11),(19,-10),(21,-11),(23,-10),(25,-11),(28,-11),(28,-19),(26,-19),(26,-18),(25,-18),(24,-17),(23,-17),(22,-16),(10,-17),(8,-17),(6,-16),(5,-14),(5,-12),(6,-6),(4,-6),(4,-7),(3,-8),(1,-9),(-4,-9),(-7,-13),(-11,-16),(-23,-19),(-26,-21),(-28,-21),(-31,-16),(-30,-14),(-33,-14),(-33,-12),(-34,-12),(-34,-11),(-31,-11),(-31,-13),(-30,-13),(-30,-11),(-26,-11),(-26,-14),(-23,-15),(-13,-11),(-11,-7),(-12,-6),(-15,-9),(-23,-10),(-25,-11),(-44,-11),(-46,-10),(-48,-10),(-50,0)))
toby.shape("tron")
twoby.shape("tron")
toby.pensize(10)
twoby.pensize(10)
toby.shapesize(.5)
twoby.shapesize(.5)
toby.pencolor("cyan")
twoby.pencolor("gold")

twoby.tiltangle(-90)
toby.tiltangle(-90)
twoby.speed(0)
toby.speed(0)
toby.penup()
twoby.penup()
toby.goto(250,0)
toby.right(180)
twoby.goto(-250,0)
toby.pendown()
twoby.pendown()

r1 = [0]
l1 = [0]
r2 = [0]
l2 = [0]
passed_coords = []

while True:
    turtle.onkeypress(right1, "d")
    turtle.onkeypress(left1, "a")
    turtle.onkeypress(right2, "Right")
    turtle.onkeypress(left2, "Left")

    toby.forward(10)
    twoby.forward(10)

    if r1[0] == 1:
        toby.right(90)
        r1[0] = 0
    if l1[0] == 1:
        toby.left(90)
        l1[0] = 0

    if r2[0] == 1:
        twoby.right(90)
        r2[0] = 0
    if l2[0] == 1:
        twoby.left(90)
        l2[0] = 0

    if (int(toby.xcor()), int(toby.ycor())) in passed_coords:
        toby.backward(10)  
    if (int(twoby.xcor()), int(twoby.ycor())) in passed_coords:
        twoby.backward(10)  
    passed_coords.append((int(toby.xcor()), int(toby.ycor())))
    passed_coords.append((int(twoby.xcor()), int(twoby.ycor())))
    
    print(passed_coords)

        
    window.listen()
window.mainloop()

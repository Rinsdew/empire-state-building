import turtle
def draw_building():
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("black")

    t.speed(100)

    # Draw the base of the building
    t.penup()
    t.goto(-132, -400)
    t.pendown()
    t.color("gold")
    t.begin_fill()
    t.forward(150)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(20) # first layer
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(15) # second layer
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(10) # third layer
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(10) # 4th layer
    t.right(90)
    t.forward(80)
    t.left(90)
    t.forward(5) # 5th layer
    t.right(90)
    t.forward(80)
    t.left(90)
    t.forward(2) # summit
    t.left(90)
    t.forward(80)
    t.right(90)
    t.forward(5)  # 5th layer
    t.left(90)
    t.forward(80)
    t.right(90)
    t.forward(10)  # 4th layer
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(10)  # third layer
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(15)  # second layer
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(20)  # first layer
    t.left(90)
    t.forward(400)
    t.end_fill()

    # Draw the windows
    t.penup()
    t.color("white")
    
    # Base layer windows
    for y in range(-380, -40, 40):
        for x in range(-80, 40, 30):
            t.goto(x, y)
            t.pendown()
            t.begin_fill()
            for _ in range(4):
                t.forward(20)
                t.right(90)
            t.end_fill()
            t.penup()
    
    # First layer windows
    for y in range(20, 80, 30):
        for x in range(-66, 20, 30):
            t.goto(x, y)
            t.pendown()
            t.begin_fill()
            for _ in range(4):
                t.forward(15)
                t.right(90)
            t.end_fill()
            t.penup()
    
    t.hideturtle()
    turtle.done()

draw_building()

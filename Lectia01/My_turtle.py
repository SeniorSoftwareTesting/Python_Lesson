import turtle
turtle.shape("turtle")
turtle.shapesize(2,1)
turtle.color("green", "yellow")
turtle.speed(10)

def david():
    for step in range(6):
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(50)
            turtle.left(360 / 3)
        turtle.end_fill()
        
        turtle.forward(50)
        turtle.right(60)




david()
turtle.backward(200)
david()

turtle.hideturtle()

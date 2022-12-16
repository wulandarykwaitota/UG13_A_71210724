import turtle

turtle.setworldcoordinates(0, -650, 800, 700)

window = turtle.Screen()
window.title("Draw W724K")
window.bgcolor("white")

turtle.width(30)
t = turtle.Turtle()

# printing  letter W
t.up()
t.pensize(9)
t.color("red")
t.goto(0, 100)
t.down()
t.goto(50, 0)
t.goto(75, 100)
t.goto(100, 0)
t.goto(150, 100)
t.up()


t.goto(200, 100)
t.down()
t.forward(60)
t.goto(200,-50)
t.up()

t.goto(325, 100)
t.down()
t.right(90)
t.forward(100)
t.left(90)
t.forward(60)
t.left(90)
t.forward(100)
t.right(90)
t.right(90)
t.forward(200)
t.up()

t.goto(550, 100)

t.down()
t.forward(200)
t.backward(100)
t.left(45)
t.forward(100)
t.backward(100)
t.left(80)
t.forward(100)


window.mainloop()





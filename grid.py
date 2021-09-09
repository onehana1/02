import turtle

turtle.goto(0,100)

count = 5
while(count>0):
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(100)
    turtle.left(90)
    
    count = count -1

	
count2 = 4
while(count2>0):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(100)

    count2 = count2 -1

turtle.exitonclick()

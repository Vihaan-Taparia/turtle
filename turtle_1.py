import turtle 

#importing turtle...
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()#defined variable

num_sides=8#variable
side_length=70
angle = 360.0/num_sides
#iterateloop for number of sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()

 
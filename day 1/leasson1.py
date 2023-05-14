from turtle import *

print("davit gelashvili")
speed(30)
#step 1: draw a square

width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)


forward(200)
left(90)


forward(200)
left(90)
#end of square

#drawing a dor

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200 ,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#draw a window

color("purple")

penup()
goto(200 ,120)
pendown()

begin_fill()
color("green")
right(60)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()
color("purple")
left(90)
forward(20)
left(90)
forward(200)
begin_fill()
left(90)
forward(20)


color("green")
left(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()
exitonclick()
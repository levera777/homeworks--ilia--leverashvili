print("hello world")



from turtle import *
    
 # we want to paint house 
speed(5  )  
width(7)
color("green")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("red")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#end of a door

penup()
goto(200,200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing window
color("purple")
penup()
goto(200,0)
pendown()
left(180)
left(30)
color("green")
forward(170)
left(90)
color("blue")
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(200,200)
pendown()
left(90)
color("black")
forward(200)
left(90)
color("green")
forward(80)
left(90)
color("blue")
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#end

exitonclick()

  
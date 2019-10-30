import turtle 


#Gets the user's input(sides of the polygon) then calculates the value of the internal angle of the shape
sides_number = int(input("Number of sides:"))
internal_angules = ((sides_number-2)*180)/sides_number

#Length of the line
proportion = 500/sides_number

#Opens the window
window = turtle.Screen()

#Creates the object instance(arrow) for draw and changes it's line width
arrow = turtle.Turtle()
arrow.pensize(3)

#Draws the regular polygon and fills it
arrow.begin_fill()

for x in range(sides_number):
    arrow.forward(proportion)
    arrow.right(180-internal_angules)
    
arrow.end_fill()


print("Click on the screen to close it")
window.exitonclick()


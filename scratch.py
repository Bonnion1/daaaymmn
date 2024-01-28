import time
import turtle

screen = turtle.Screen()
screen.screensize(20, 20, "white")

pen = turtle.Turtle()
pen.shape("turtle")
pen.color("black")
pen.pensize(5)
pen.hideturtle()

text1 = ("\nWELCOME TO THE BEAR STATION"
         "\nLET'S FILL SOME BABY'S UP!!!!!")
for char in text1:
    print(char, end='', flush=True)
    time.sleep(0.1)

class BearParts:
    @staticmethod
    def draw_circle(pen, x, y, radius):
        pen.penup()
        pen.goto(x, y)
        pen.down()
        pen.circle(radius)

BearParts.draw_circle(pen, -155, -190, 60)  # Circle 1
BearParts.draw_circle(pen, 155, -190, 60)   # Circle 2
BearParts.draw_circle(pen, 0, -190, 150)     # Body
BearParts.draw_circle(pen, 0, 110, 80)       # Head
BearParts.draw_circle(pen, 100, 195, 50)     # Ear 1
BearParts.draw_circle(pen, -100, 195, 50)    # Ear 2
BearParts.draw_circle(pen, 100, -50, 60)     # Hand 1
BearParts.draw_circle(pen, -100, -50, 60)    # Hand 2

# Function to fill a circle with a given color
def fill_circle(pen, x, y, radius, color):
    pen.penup()
    pen.goto(x, y)
    pen.down()
    pen.begin_fill()
    pen.fillcolor(color)
    pen.circle(radius)
    pen.end_fill()

# Get user input for primary color
text3 = "\n****Select your primary color****"
for char in text3:
    print(char, end='', flush=True)
    time.sleep(0.050)

choices = int(input("\nFor RED press [1]"
                     "\nFor YELLOW press [2]"
                     "\nFor BLUE press [3]"
                     "\nEnter here:"))

def color_choice(choice):
    if choice == 1:
        return "red"
    elif choice == 2:
        return "yellow"
    elif choice == 3:
        return "blue"
    else:
        return "white"

primary_color = color_choice(choices)
print("The primary color is", primary_color)

# Loop to fill each shape individually
while True:
    part_selector = int(input("\nIn which part do you want to fill? (Enter the corresponding number)"
                              "\n[1] Feet"
                              "\n[2] Hand"
                              "\n[3] Body"
                              "\n[4] Head"
                              "\n[5] Ears"
                              "\n[0] Exit"
                              "\nEnter here:"))

    if part_selector == 0:
        print("Program Completed.")
        break

    tcolor = input("Enter color code:")

    if part_selector == 1:
        fill_circle(pen, -155, -190, 60, tcolor)
        fill_circle(pen, 155, -190, 60, tcolor)
    elif part_selector == 2:
        fill_circle(pen, 100, -50, 60, tcolor)
        fill_circle(pen, -100, -50, 60, tcolor)
    elif part_selector == 3:
        fill_circle(pen, 0, -190, 150, tcolor)
    elif part_selector == 4:
        fill_circle(pen, 0, 110, 80, tcolor)
    elif part_selector == 5:
        fill_circle(pen, 100, 195, 50, tcolor)
        fill_circle(pen, -100, 195, 50, tcolor)
    else:
        print("Invalid part selection. Please enter a valid part number.")

    screen.update()  # Update the turtle screen

# Close the turtle graphics window
turtle.done()

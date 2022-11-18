import turtle
import math
import random
import winsound


# Space Invaders
# Screen set up
s = turtle.Screen()
s.bgcolor("black")
s.title("Space Invaders")
s.bgpic("space_invaders_background.gif")
s.tracer(0)

# Register the shape
s.register_shape("invader.gif")
s.register_shape("player.gif")


# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

# Draw a square for the border
for square in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Set the score to 0
score = 0

# Draw the score (using turtle graphics)
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()


# Create the player using turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# .speed here is a variable while above is the method
player.speed = 0


# Create the player's shield wall
shield = turtle.Turtle()
shield.color("orange")
shield.shape("circle")
shield.penup()
shield.speed(0)
shield.setposition(0, -200)
shield.setheading(90)





# Move the player left and right by creating the functions needed. The player is x so left and right is just opposite.
def move_left():
    player.speed = -1
    
def move_right():
    player.speed = 1
   
def move_player():
    x = player.xcor()
    x += player.speed
# Loop keeps player from leaving border
    if x < -280:
        x= - 280
    if x > 280:
        x = 280
   
    player.setx(x)


# Creating a function to define the bullet's state, with global variable.
def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        winsound.PlaySound("Space Invaders_laser.wav", winsound.SND_ASYNC)
        bulletstate = "fire"
        # Moves the bullet just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

# Create a function that measures the distance of bullet to invader (not called yet) 
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False


# Create a keyboard bind for left and right
s.listen()
s.onkeypress(move_left, "Left")
s.onkeypress(move_right, "Right")
s.onkeypress(fire_bullet, "space")


# Choose a number of invaders
number_of_invaders = 30
# Create an empty list of invaders
invaders = []

# Add inavders to the list
for i in range(number_of_invaders):
	# Create the enemy
	invaders.append(turtle.Turtle())

invader_start_x = -225
invader_start_y = 250
invader_number = 0

for invader in invaders:
    invader.color("red")
    invader.shape("invader.gif")
    invader.penup()
    invader.speed(0)
    x = invader_start_x + (50 * invader_number)
    y = invader_start_y
    invader.setposition(x, y)
    # Update the invader number
    invader_number += 1
    if invader_number == 10:
        invader_start_y -= 50
        invader_number = 0


invaderspeed = 0.1


# Create the players weapon

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 1.5

# Define bullet state's
# ready - ready to fire
# fire - bullet is firing

bulletstate = "ready"



# Main game loop. Atrributes above exist outside the main

while True:
    
    s.update()
    move_player()

    # Adding list into main
    for invader in invaders:

        # Move the invader by getting the x cord and adding the speed
        x = invader.xcor()
        x += invaderspeed
        invader.setx(x)

        # Move the enemy back and down
        if invader.xcor() > 280:
            # Moves all the invaders down. Used I variable since invader variable is taken (nested loop)
            for i in invaders:
                y = i.ycor()
                y -= 40
                i.sety(y)
            # Change invader direction
            invaderspeed *= -1

        if invader.xcor() < -280:
            # Move all invaders down
            for i in invaders:
                y = i.ycor()
                y -= 40
                i.sety(y)
            # Change direction
            invaderspeed *= -1

        # Check for a collision between bullet and invader so function can be called
        if isCollision(bullet, invader):
            winsound.PlaySound("Space Invaders_explosion.wav", winsound.SND_ASYNC)
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Reset the invader
            invader.setposition(0, 10000)
            # Update the score
            score += 10
            scorestring = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))


        if isCollision(player, invader):
            player.hideturtle()
            invader.hideturtle()
            print ("Game Over")
            break

    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Checks if bullet has reached the top
    if bullet.ycor() > 275:
         bullet.hideturtle()
         bulletstate = "ready"
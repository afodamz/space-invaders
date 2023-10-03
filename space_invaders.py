import turtle
import random
import os
import math
import random


# We create the screen of the game
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space invaders")

# To add images to our work, that is setting the enemy,
# player and the background of the project to be images
# Image for background
# wn.bgpic("space_invaders_background.png")



# Register the shapes,:: This is done in other
# to be able to use the gif files as shapes of the objects
	# Image for invaders
# turtle.register_shape("invader.gif")
	# Image for player
# turtle.register_shape("player.gif")



# To draw the screen or geometry of the game
border = turtle.Turtle()
border.speed(0)
border.color('white')
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(3)
for side in range(4):
	border.fd(600)
	border.lt(90)
border.hideturtle()


#Create player turtle
player = turtle.Turtle()
player.color('yellow')
player.shape('triangle')
# player.shape('player.gif')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# Players bullet
bullet = turtle.Turtle()
bullet.color('blue')
bullet.shape('classic')
bullet.penup()
bullet.speed(0)
bullet.shapesize(0.5, 0.5)
bullet.setheading(90)
bullet.hideturtle()



#Enemies
# enemy = turtle.Turtle()
# enemy.color('red')
# enemy.shape('circle')
# enemy.penup()
# enemy.speed(0)
# enemy.setposition(-200, 250)
# bullet.setheading(90)


# To create many enemies
# Number of enemies
number_of_enemies = range(5)
# Create an empty ist of enemies
enemies = []

# Add enemies to the list
for i in number_of_enemies:
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.color('red')
	enemy.shape('circle')
	# enemy.shape('invader.gif')
	enemy.penup()
	enemy.speed(0)
	x_position = random.randint(-200, 200)
	y_position = random.randint(-100, 200)
	enemy.setposition(x_position, y_position)
	

# To add score
score = 0

score_t = turtle.Turtle()
score_t.color('white')
score_t.speed(0)
score_t.penup()
score_t.setposition(-290, 280)
scorestr = 'score %s' %score
score_t.write(scorestr, False, align='left', font=('Arial', 14, 'normal'))
score_t.hideturtle()



# Player movement
playerspeed = 15

# Bullet speed
bulletspeed = 20

#Enemy movement
enemyspeed = 2


# Define bullets state: we want to be able to fire when the bullet is:
# Ready to fire
# Fire bullets
bullet_state = 'ready'



# Player move left
def move_left():
	x = player.xcor() - playerspeed
	if player.xcor() < -280:
		x = -280
	player.setx(x)


# Player move right
def move_right():
	x = player.xcor() + playerspeed
	if player.xcor() > 280:
		x = 280
	player.setx(x)


# Bullet state
def fire_bullet():
	# Declare bullet_state global, so that any 
	#other further changes will arise in the 
	#change of the upper variable and every other part
	global bullet_state
	# We want to be aable to fire only when the bullet_state is ready
	# until the bullet passes or touches the boundary before it can reload
	if bullet_state == 'ready':
		bullet_state = 'fire'
		# set the position of the ball to be above the player
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition(x, y)
		bullet.showturtle()



# Creating a collison function: we use pythagoras theorem
def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
	if distance < 15:
		return True




# creating keyboard functions
turtle.listen()
turtle.onkey(move_left, 'Left')
turtle.onkey(move_right, 'Right')
turtle.onkey(fire_bullet, 'space')



# MAIN GAME LOOPING
while True:
	# To make the rest of the enemies to move
	for enemy in enemies:
		# enemy move
		x = enemy.xcor() + enemyspeed
		enemy.setx(x)


		#move enemy back and forth and collision
		if enemy.xcor() > 280:
			# Move all the enemies down
			for e in enemies:
				y = e.ycor() - 40
				# we do not need to change the position of the enemis as many times, rather once enemyspeed *= -1
				e.sety(y)
			# Cham=nge enemies position
			enemyspeed *= -1

		if enemy.xcor() < -280:
			# Move all the enemies down
			for e in enemies:
				y = e.ycor() - 40
				# we do not need to change the position of the enemis as many times, rather once enemyspeed *= -1
				e.sety(y)
			# Change enemies position
			enemyspeed *= -1

			

		# Check if there is collision between bullet and enemy
		if isCollision(enemy, bullet):
			bullet.hideturtle()
			bullet_state = 'ready'
		# Reset the enemy position when the bullets hits the enemy
			x_position = random.randint(-200, 200)
			y_position = random.randint(-50, 270)
			enemy.setposition(x_position, y_position)
			score +=10
			scorestr = 'score %s' %score
			score_t.clear()
			score_t.write(scorestr, False, align='left', font=('Arial', 14, 'normal'))
			score_t.hideturtle()



		# Enemy collide with player
		if isCollision(enemy, player):
			player.hideturtle()
			enemy.hideturtle()

			print('Game over')
			break

	


	# Creating bullets and its movement
	y = bullet.ycor() + bulletspeed
	bullet.sety(y)

	# Check to see if the bullet has passed the bar above
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bullet_state = 'ready'


	



delay = input("press enter to finish")
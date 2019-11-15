import turtle
import random
import time

# set background
screen=turtle.Screen()
screen.bgcolor('#867B89')
screen.tracer(0)

# Rules: Reach box 15 in four turns or less

# words
writer = turtle.Turtle()
writer.pencolor('white')
writer.hideturtle()
writer.penup()

writer.goto(-250,195)
writer.write('Turns Remaining: ', align='left', font=('Din Alternate', 15, 'bold'))

writer.goto(-250,220)
writer.write('Press \'R\' to Roll. ', align='left', font=('Din Alternate', 15, 'bold'))

writer.goto(-250,170)
writer.write('You Rolled: ', align='left', font=('Din Alternate', 15, 'bold'))

writer.goto(-250,85)
writer.write('Reach box 15 in 4 turns. --> ', align='left', font=('Din Alternate', 18, 'bold'))

# Board
x = -75
y = -200
z = 0
square = turtle.Turtle()
number = turtle.Turtle()
number.pencolor('black')
number.penup()
number.ht()
square.penup()
square.pencolor('black')
square.fillcolor('#f0f8ff')
square.hideturtle()
def box(x,y,z):
  for boxes in range(15):
    square.goto(x,y)
    number.goto(x+5,y+5)
    square.pendown()
    square.setheading(0)
    square.begin_fill()
    for sides in range(4):
      square.pendown()
      square.forward(50)
      square.left(90)
      square.penup()
    square.end_fill()
    number.write(boxes+1, align='left', font=('Din Alternate', 8, 'bold'))
    if z <=2:
      x += 55
      z += 1
    elif z == 3 or z == 4:
      y += 55
      z += 1
      square.fillcolor('#faebd7')
    elif z >=5 and z <= 7:
      x += -55
      z += 1
      square.fillcolor('#ffefdb')
    elif z == 8 or z == 9:
      y += 55
      z += 1
      square.fillcolor('#eedfcc')
    elif z >=10 and z <= 12:
      x += 55
      z += 1
      square.fillcolor('#cdc0b0')
    elif z == 13:
      y += 55
      z += 1
      square.fillcolor('#8b8378')

# special squares


    
#start square

first = turtle.Turtle()
first.ht()
first.fillcolor('white')
first.penup()
first.goto(-180, -200)
first.pendown()
first.setheading(0)
first.begin_fill()
for sides in range(2):
  first.forward(100)
  first.left(90)
  first.forward(50)
  first.left(90)
first.end_fill()
first.penup()
first.fillcolor('Black')
first.goto(-175, -185)
first.pendown()
first.write('Start', align='left', font=('Din Alternate', 15, 'bold'))

# Add Player Turtle

xs = -115
ys = -180
player = turtle.Turtle()
player.fillcolor('red')
player.ht()
def playershape():
  player.clear()
  player.penup()
  player.begin_fill()
  player.pendown()
  player.forward(20)
  player.left(90)
  player.forward(5)
  player.left(90)
  player.forward(5)
  player.right(90)
  player.forward(15)
  player.right(90)
  player.forward(2)
  player.left(90)
  player.circle(8,180)
  player.left(90)
  player.forward(2)
  player.right(90)
  player.forward(15)
  player.right(90)
  player.forward(5)
  player.left(90)
  player.forward(5)
  player.end_fill()
  player.penup()
  screen.update()

player.penup()
player.goto(xs,ys)
playershape()


box(x,y,z)

screen.update()

# hazards and special squares

# square 14 is a -5
snake1 = turtle.Turtle()
snake1.pencolor('red')
snake1.ht()
snake1.penup()
snake1.goto(125,35)
snake1.write('-5', align='right', font=('Din Alternate', 15, 'bold'))

#square 10 is a +1
snake1.pencolor('green')
snake1.goto(-40,-20)
snake1.write('+1', align='right', font=('Din Alternate', 15, 'bold'))

#square 7 is a lose a turn
snake1.pencolor('red')
snake1.goto(80,-64)
snake1.write('lose', align='right', font=('Din Alternate', 15, 'bold'))
snake1.goto(63,-75)
snake1.write('a', align='right', font=('Din Alternate', 15, 'bold'))
snake1.goto(85,-90)
snake1.write('turn', align='right', font=('Din Alternate', 15, 'bold'))

# keep track of the turns

turn = 4
rolling = turtle.Turtle()
rolling.pencolor('white')
rolling.hideturtle()
rolling.penup()
rolling.goto(-80,195)
rolling.write(turn, align='left', font=('Din Alternate', 15, 'bold'))
rolling.penup()
rolling.goto(-140,170)

# Game play:

# dice Roll

def rolldie():
  return random.randint(1,6)
  
def dice():
  global roll
  global turn
  turn += -1
  new = rolldie()
  roll += new
  rolling.clear()
  rolling.write(new, align='left', font=('Din Alternate', 15, 'bold'))
  rolling.goto(-80,195)
  rolling.write(turn, align='left', font=('Din Alternate', 15, 'bold'))
  rolling.goto(-140,170)
  screen.update()
  box_1 = -50,-180
  box_2 = 5,-180
  box_3 = 60,-180
  box_4 = 115,-180
  box_5 = 115,-125
  box_6 = 115,-70
  box_7 = 60,-70
  box_8 = 5, -70
  box_9 = -50, -70
  box_10 = -50, -15
  box_11 = -50, 40
  box_12 = 5, 40
  box_13 = 60, 40
  box_14 = 115, 40
  box_15 = 115, 95
  if roll == 1 and turn >= 0:
    player.goto(box_1)
    player.setheading(0)
    playershape()
    lose_detect()
  elif roll == 2 and turn >= 0: 
    player.goto(box_2)
    player.setheading(0)
    playershape()
    lose_detect()
  elif roll == 3 and turn >= 0:
    player.goto(box_3)
    player.setheading(0)
    playershape()
    lose_detect()
  elif roll == 4 and turn >= 0:
    player.goto(box_4)
    player.setheading(0)
    playershape()
    lose_detect()
  elif roll == 5 and turn >= 0:
    player.goto(box_5)
    player.setheading(0)
    playershape()
    lose_detect()
  elif roll == 6 and turn >= 0:
    player.goto(box_6)
    player.setheading(0)
    playershape()
    lose_detect()
  elif roll == 7 and turn >= 0:
    player.goto(box_7)
    player.setheading(0)
    playershape()
    time.sleep(1)
    turn += -1
    rolling.clear()
    rolling.goto(-80,195)
    rolling.write(turn, align='left', font=('Din Alternate', 15, 'bold'))
    rolling.goto(-140,170)
    rolling.write(new, align='left', font=('Din Alternate', 15, 'bold'))
    screen.update()
    lose_detect()
  elif roll == 8 and turn >= 0:
    player.goto(box_8)
    player.setheading(0)
    playershape()
    lose_detect()
  elif roll == 9 and turn >= 0:
    player.goto(box_9)
    player.setheading(0)
    playershape()
    lose_detect()
  elif roll == 10 and turn >= 0:
    player.goto(box_10)
    player.setheading(0)
    playershape()
    screen.update()
    time.sleep(1)
    player.goto(box_11)
    player.setheading(0)
    playershape()   
    screen.update()
    roll = 11
    lose_detect()
  elif roll == 11 and turn >= 0:
    player.goto(box_11)
    player.setheading(0)
    playershape()
    lose_detect()
  elif roll == 12 and turn >= 0:
    player.goto(box_12)
    player.setheading(0)
    playershape()
    lose_detect()
  elif roll == 13 and turn >= 0:
    player.goto(box_13)
    player.setheading(0)
    playershape()
    lose_detect()
  elif roll == 14 and turn >= 0:
    player.goto(box_14)
    player.setheading(0)
    playershape()
    screen.update()
    time.sleep(1)
    player.goto(box_9)
    player.setheading(0)
    playershape()
    screen.update()
    roll = 9
    lose_detect()
  elif roll >= 15 and turn >= 0:
    player.goto(box_15)
    player.setheading(0)
    playershape()
    screen.update()
    winner()
    time.sleep(.5)
    screen.update()
    newgame()
  screen.update()

roll = 0


def newgame():
  global roll
  global turn
  turn = 4
  roll = 0
  player.ht()
  player.goto(-115,-180)
  player.setheading(0)
  playershape()
  rolling.clear()
  rolling.goto(-80,195)
  rolling.write(turn, align='left', font=('Din Alternate', 15, 'bold'))
  rolling.goto(-140,170)
  screen.update()

def lose_detect():
  global turn
  time.sleep(1.5)
  t= 0
  if turn == 0:
    b = player.xcor()
    c = player.ycor()
    for spin in range(100):
      player.clear()
      player.goto(b,c)
      player.setheading(t)
      playershape()
      screen.update()
      t += 11
    player.setheading(0)
    playershape()
    screen.update()
    time.sleep(2)
    newgame()

def winner():
  win = turtle.Turtle()
  win.ht()
  win.pu()
  win.goto(30,175)
  win.pencolor('red')
  win.write('YOU WIN!', align = 'left', font=('Din Alternate', 35, 'bold'))
  screen.update()
  win.clear()
  time.sleep(1)
  win.clear()
  win.pencolor('white')
  win.write('YOU WIN!', align = 'left', font=('Din Alternate', 35, 'bold'))
  screen.update()
  time.sleep(1)
  win.clear()
  win.pencolor('blue')
  win.write('YOU WIN!', align = 'left', font=('Din Alternate', 35, 'bold'))
  screen.update()
  time.sleep(1)
  win.clear()
  screen.update()
  
screen.onkey(dice, 'r')
screen.listen()
screen.update()

import turtle
import time
import random
#setting up screen settings
screen = turtle.Screen()
screen.tracer(0)   
turtle.screensize(216, 500,"#33fff0")
turtle.setup(288, 512)
turtle.hideturtle()

#creating a turtle used for background decoration
ground = turtle.Turtle()
ground.penup()
ground.ht()
ground.goto(0,-300)
ground.shape("square")
ground.color("#2ed643")
ground.shapesize(20, 500,)
ground.st()

#object creation
bird = turtle.Turtle()
bird.penup()
bird.setpos(0,0)
bird.shape("square")
bird.left(90)
bird.color("yellow")


pipetop = turtle.Turtle()
pipetop.pu()
pipetop.goto(150,-220)
pipetop.shape("square")
pipetop.shapesize(15, 2)
pipetop.color("green")

pipebot = turtle.Turtle()
pipebot.pu()
pipebot.goto(150,180)
pipebot.shape("square")
pipebot.shapesize(15, 2)
pipebot.color("green")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(0, 50)

score = 0

scorepen = turtle.Turtle()
scorepen.hideturtle()
scorepen.pu()
scorepen.goto(-100,200)

def movepipe():
    #moves the top and bottom pipe 2 units to the left every single time it's called
    pipetop.goto(pipetop.xcor() -2,pipetop.ycor())
    pipebot.goto(pipebot.xcor()-2,pipebot.ycor())

def resetpipe(randheight):
    #set the variable global so it can be used inside the function and increase it
    global score
    score +=1
    #reset pipe position offscreen
    pipebot.goto(180,randheight-225)
    pipetop.goto(180,randheight+225)
    #removes the last score
    scorepen.undo()
    #write new score
    scorepen.write(score, move=False, align="center", font=("Arial", 16, "normal"))
    
def jump():
    #moves the bird up
    for i in range(40):
        bird.sety(bird.ycor()+1) 

#dectection for keypresses
screen.listen()
screen.onkey(jump, "space")

def gameover():
    #write score
    pen.pd()
    pen.write("Game Over", move=False, align="center", font=("Arial", 32, "normal"))
    #update the screen so they see the text without seeing the writing process
    screen.update()
    #wait 2 seconds
    time.sleep(2)
    #close screen
    screen.bye()

while True:
    #wait 0.01 seconds before updating the screen every fram
    time.sleep(0.01)
    #update the screen
    screen.update()
    
    movepipe()
    #gravity
    bird.sety(bird.ycor()-2.5)
    #dectection for top of pipe
    if abs(bird.xcor() - pipetop.xcor()) < 40:
        if abs(bird.ycor() - pipetop.ycor()) < 150:
            gameover()
    #dectection for bottom of pipe
    if abs(bird.xcor() - pipebot.xcor()) < 40:
        if abs(bird.ycor() - pipebot.ycor()) < 150:
            gameover()
    #dectection for if the bird touches the ground
    if bird.ycor() <= -250:
        gameover()
    #resets the pipe when offscreen
    if pipetop.xcor() <= -170:
        resetpipe(random.randint(-100,100))

    

screen.mainloop()
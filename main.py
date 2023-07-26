import turtle
import random
import time

delay=0.1
#Score
score=0
high_score=0
# Creating Screen
guiWindow=turtle.Screen()
guiWindow.bgcolor('green')
guiWindow.title('SNAKE GAME BY NEXAS')
guiWindow.setup(width=600, height=600)



#head of the snake
head=turtle.Turtle()
head.color('black')
head.shape('square')
head.speed(0)
head.goto(0,0)
head.penup()
head.direction="up"

#food for snake
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments=[]

#scores
pen=turtle.Turtle()
pen.color("Orange")
pen.shape("square")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score : 0 High Score : 0", align="center", font=("Verdana",23,"normal"))

#snake movement
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y + 20)
    if head.direction=="down":
        y=head.ycor()
        head.sety( y - 20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x - 20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x + 20)

#snake direction
def go_up():
    if head.direction != "down":
       head.direction="up"
def go_down():
    if head.direction != "up":
        head.direction="down"
def go_left():
    if head.direction != "right":
        head.direction="left"
def go_right():
    if head.direction != "down":
        head.direction="right"

# on Keypress of keyboard keys
guiWindow.listen()
guiWindow.onkeypress(go_up,'u')
guiWindow.onkeypress(go_down,'d')
guiWindow.onkeypress(go_left,'l')
guiWindow.onkeypress(go_right,'r')

#:creting a loop for the game
while True:
    guiWindow.update()
#movinment of food within the screen
    if head.distance(food) < 20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        # adding a new segment
        segment = turtle.Turtle()
        segment.color('gray')
        segment.shape("square")
        segment.penup()
        segment.speed(0)
        segments.append(segment)


        #increas the score
        score= score + 10

        if score > high_score:
            high_score= score
        pen.clear()
        pen.write("Score : {} High Score : {}".format(score,high_score),align="center",font=("Verdana",23,"normal"))

 #movement of turle in reverse way
    for index in range(len(segments) -1, 0, -1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
#moving for the head
    if len(segments) > 0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

#check for collision borders
    if head.xcor()>290 or head.xcor() <-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(0.5)
        head.goto(0,0)
        head.direction="stop"
    #hiding the segments
        for segment in segments:
            segment.goto(1000,1000)
    #clearing the segments
        segments.clear()

    #Reset the score
        score = 0
    #update the score display
        pen.clear()
        pen.write("Score : {} High Score : {}".format(score, high_score), align="center", font=("Verdana", 23, "normal"))

    move()
 #Checking collision with the body segment
    for segment in segments:
        if segment.distance(head)< 20:
            time.sleep(0.5)
            head.goto(0,0)
            head.direction="stop"

    # hiding the segments again
            for segment in segments:
                segment.goto(1000, 1000)
    # clearing the segments again
            segments.clear()

    time.sleep(delay)


guiWindow.mainloop()
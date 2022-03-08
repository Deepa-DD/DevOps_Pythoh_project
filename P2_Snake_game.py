import turtle
import time
import random
 
delay = 0.1                                                 # this variable is for speed 
score = 0                                                   # In this variable we will add user's current score
high_score = 0                                              # This is high score  
 
 
# Creating a window screen
main_screen = turtle.Screen()                               #  this is main screen by turtle.Screen
main_screen.title("****  Snake Game By Deepa  ****")        #  Adding tital on top of the screen
main_screen.bgcolor("#374151")                              #  Adding background color in main screen by using .bgcolor
main_screen.setup(width=600, height=600)                    #  Creating height and width by .setup
main_screen.tracer(0)                                       #----------------------------------------------------------
 

# In this part we are creating head of snake
head = turtle.Turtle()                                      #  Creating head by turtle
head.shape("square")                                        # Giving shape for head
head.color("#0284C7")                                       #  Color for head
head.penup()                                                #  It will not write line of movment
head.goto(0, 0)                                             #  position from where snake will start the game
head.direction = "Stop"                                     # Direction will be stop
 
# In this part we are creating food in the game methods will be almost same as head 
food = turtle.Turtle()                                      # Creating one tertle for food 
food.speed(0)                                               #   speed will bw zero because score will not move
food.shape("circle")                                        #  giving Shape 
food.color("black")                                         #  it will give color
food.penup()                                                #  It will not write line 
food.goto(0, 100)                                           # Position for starting point 


# Inthis part we are creatging the Score boad
score_for_scoreBoad = turtle.Turtle()                       # Creating one tertle for food 
score_for_scoreBoad.speed(0)                                #   speed will bw zero because score will not move
score_for_scoreBoad.shape("square")                         #  Shape will be square of score board
score_for_scoreBoad.color("white")                          # Here we are giving color
score_for_scoreBoad.penup()                                 #  It will not write line 
score_for_scoreBoad.hideturtle()                            # Here we are using hideturtle because we don't want turtle visible only text should be visible
score_for_scoreBoad.goto(0, 250)                            #  Giving position here text will be place 
score_for_scoreBoad.write("Score : 0  High Score : 0", align="center",font=("candara", 20, "bold"))  # Here we are giving text with some styling and position by using font and align
 
 
 
# Here we will bw creating some function for Assigning key directions
def move_up():                                              # function for up direction 
    if head.direction != "down":                            # We are checking if diection of head is not down 
        head.direction = "up"                               # Then the direction of head will be up
def move_down():                                            # function for down direction 
    if head.direction != "up":                              # We are checking if diection of head is not up
        head.direction = "down"                             # Then the direction of head will be down 
def move_left():                                            # function for left direction 
    if head.direction != "right":                           # We are checking if diection of head is not right
        head.direction = "left"                             # Then the direction of head will be left
def move_right():                                           # function for right direction 
    if head.direction != "left":                            # We are checking if diection of head is not left
        head.direction = "right"                            # Then the direction of head will be right

def move():                                                 # In this function we will give movment to our snake   
    if head.direction == "up":                              # Checking if head direction is up 
        y = head.ycor()                                     # if the contion is true the ycor of head will be store in y variable 
        head.sety(y+20)                                     # We will incease ycor of head by 20
    if head.direction == "down":                            # Checking if head direction is down
        y = head.ycor()                                     # if the contion is true the ycor of head will be store in y variable 
        head.sety(y-20)                                      # We will dicrease ycor of head by 20
    if head.direction == "left":                            #  Checking if head direction is left 
        x = head.xcor()                                     # if the contion is true the ycor of head will be store in x variable 
        head.setx(x-20)                                     # We will dicrease xcor of head by 20
    if head.direction == "right":                           #  Checking if head direction is right  
        x = head.xcor()                                     # if the contion is true the ycor of head will be store in x variable 
        head.setx(x+20)                                     # We will incease xcor of head by 20
 
# Here we will be giving some eventlitsners so that user can press those keys and can play the game
main_screen.listen()                                        # By this we are adding event litsner 
main_screen.onkey(move_up, "Up")                            # Up key will move our snake up side 
main_screen.onkey(move_down, "Down")                        # down key will move our snake down side 
main_screen.onkey(move_left, "Left")                        # left key will move our snake left side 
main_screen.onkey(move_right, "Right")                      # right key will move our snake right side 
 
Bodies = []                                                 # this list is for bodies
while True:
    try:    
        main_screen.update()                                # With .update() we will update our screen 
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290: # This condition is, if snake will touch any wall ( means if diffrence between head and wall is less) then further oprationns will happen 
            time.sleep(1)                                   # Sleep time will bw 0 
            head.goto(0, 0)                                 #  snake will be take starting from 0,0 position 
            head.direction = "Stop"                         # Direction will be stop 
            for body in Bodies:                             #  VAriable will be itrate on vodies
                body.goto(1000, 1000)                       # after updating screen ,od bodies will be not visile 
            Bodies.clear()                                  #  List of body will be clear so that new body can bbe add
            score = 0                                       # Score will be 0 again
            delay = 0.1                                     # Speed also will be 0.1 
            score_for_scoreBoad.clear()                     #  By this old score will be not visible on the screen
            score_for_scoreBoad.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))   # again we are writing score 0 with updated higest score


        # By this condition we will be creating new food 
        if head.distance(food) < 20:                        #  when distance between head and food will be less
            x = random.randint(-270, 270)                   #  x will be random number between -270 and 270
            y = random.randint(-270, 270)                   #  x will be random number between -270 and 270
            food.goto(x, y)                                 # new food will come on new X and y excess
    
            # Adding body Here
            new_body = turtle.Turtle()                      # for body we are creating turtles
            new_body.speed(0)                                   #  Speed will be 0
            new_body.shape("square")                        # giving shape with .shape
            new_body.color("orange")                        # tail colour
            new_body.penup()                                # Here we wre using penup for notmaking line 
            Bodies.append(new_body)                         # all new bidy will be append in list of bodies
            delay -= 0.001                                  #  Speed will be increase 
            score += 10                                     # here how many bodies will be added score will also increase by 10
            if score > high_score:                          # this condition will check is score is more then highscore or not 
                high_score = score                          #  if yes, then highscore will be update with score 
            score_for_scoreBoad.clear()                     # Score boad will be clear because we have to update that
            score_for_scoreBoad.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))    #  Scoreboad will be update with new values
        for index in range(len(Bodies)-1, 0, -1):           #  In this we will move body
            x = Bodies[index-1].xcor()                      # Here we are deciding velue of x
            y = Bodies[index-1].ycor()                      # Here we are deciding velue of y  
            Bodies[index].goto(x, y)                        # Position of bodies will by according x and y
        if len(Bodies) > 0:                                 #  In this we will move head 
            x = head.xcor()                                 #  Here we are deciding velue of x
            y = head.ycor()                                 # Here we are deciding velue of y  
            Bodies[0].goto(x, y)
        move()                                              #  Calling move function

        # Checking for head collisions with body Bodies 
        for body in Bodies:                                  #   checking position of every turtle of body
            if body.distance(head) < 20:                    #  if distance between body and head is less then 20 
                time.sleep(1)                               #  time will sleep 
                head.goto(0, 0)                             #  Position will reset 
                head.direction = "stop"                     #   head direction will be stop 
                for body in Bodies:                         #  Itrating on bodies
                    body.goto(1000, 1000)                   #  Changing position of body
                body.clear()                                #  Evry body will be clear

                score = 0                                   #  Score is 0
                delay = 0.1                                 # speed will be again 0.1
                score_for_scoreBoad.clear()                 # Scoread will be clear 
                score_for_scoreBoad.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))   #  Score boad be With this updated value 
        time.sleep(delay)                                   #  the time will be sleep sccording delay 
    except:                                                 #   We are using this because our main loop is while true so in that interpriter can go line number 161
        break
    
 
main_screen.mainloop()

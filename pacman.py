import turtle

board = '''
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# . . . . . . . . . . . . # # . . . . . . . . . . . . #
# . # # # # . # # # # # . # # . # # # # # . # # # # . #
# O # # # # . # # # # # . # # . # # # # # . # # # # O #
# . # # # # . # # # # # . # # . # # # # # . # # # # . #
# . . . . . . . . . . . . . . . . . . . . . . . . . . #
# . # # # # . # # . # # # # # # # # . # # . # # # # . #
# . # # # # . # # . # # # # # # # # . # # . # # # # . #
# . . . . . . # # . . . . # # . . . . # # . . . . . . #
# # # # # # . # # # # # . # # . # # # # # . # # # # # # 
          # . # # # # #   # #   # # # # # . #          
          # . # #                     # # . #
# # # # # # . # #   # # # _ _ # # #   # # . # # # # # #
            .       #             #       .            
# # # # # # . # #   #             #   # # . # # # # # # 
          # . # #   # # # # # # # #   # # . #          
          # . # #                     # # . #
# # # # # # . # #   # # # # # # # #   # # . # # # # # #
#           . # #   # # # # # # # #   # # .           #
# . . . . . . . . . . . . # # . . . . . . . . . . . . #
# . # # # # . # # # # # . # # . # # # # # . # # # # . # 
# . # # # # . # # # # # . # # . # # # # # . # # # # . #
#   . . # # . . . . . . . . . . . . . . . . # # . . . # 
# # # . # # . # # . # # # # # # # # . # # . # # . # # # 
# # # . # # . # # . # # # # # # # # . # # . # # . # # #
# . . . . . . # # . . . . # # . . . . # # . . . . . . #
# . # # # # # # # # # # . # # . # # # # # # # # # # . # 
# . # # # # # # # # # # . # # . # # # # # # # # # # . #
# . . . . . . . . . . . . . . . . . . . . . . . . . . #
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

'''
boardnum = board
boardnum = boardnum.replace("#", "0")
boardnum = boardnum.replace(".", "1")
boardnum = boardnum.replace("O", "2")
boardnum = boardnum.replace("_", "3")
boardnum.strip()

W = 1100
H = 1200
gameover = False
box_size = 14
food_size = 8

pacman = turtle.Turtle()
pacman.color("Yellow")
pacman.setheading(0)
pacman.penup()
pacman.speed(0)
pacman.shape("circle")

food = turtle.Turtle()
food.color("White")
food.penup()
food.goto(-400,475)
food.hideturtle()

pen = turtle.Turtle()
pen.color("Blue")
# pen.speed(0)

screen = turtle.Screen()
screen.bgcolor("Black")
screen.tracer(0)
screen.setup(W,H,1450,0)

def drawfood(boardnum, food_size):
    x = food.xcor()
    y = food.ycor()

    for f in boardnum:
        food.forward(15)
        if f ==  "1":
            food.dot(food_size, "White")
        elif f == "2":
            food.dot(food_size * 2, "White")
        elif f == "\n":
            food.goto(x,y-30)
            x = food.xcor()
            y = food.ycor()

def drawwall(w,h,x,y):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.begin_fill()
    for i in range(0,4):
        pen.forward(w)
        pen.left(90)
        pen.forward(h)
        pen.left(90)
    pen.end_fill()

drawfood(boardnum,food_size)
#         w,   h,   x,   y
drawwall(800, 15, -380, 435) # top wall
drawwall(800, 15,-380, -435) # bottom wall
drawwall(15, 330 , -395, -435) # bottom left side wall
drawwall(15, 290 , -395, 160) # top left side wall 
drawwall(160, 15, -395, 160) # left inner wall 1
drawwall(15, 115, -250, 60) # left inner wall 2
drawwall(160, 15, -395, 60) # left inner wall 3

while True: 
    screen.update()
turtle.mainloop()


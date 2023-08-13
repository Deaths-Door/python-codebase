import turtle as msLogo
msLogo.pendown

#draw circles
for x in range(5) :
    msLogo.circle(35)
    msLogo.forward(40)

#dashed lines
for x in range(5):
    msLogo.pendown
    msLogo.forward(50)
    msLogo.penup
    msLogo.forward(50)

#circle with not connection
msLogo.penup()
for i in range (2):
    msLogo.pendown()
    msLogo.circle(50)
    msLogo.penup()
    msLogo.forward(100)

#square
for x in range(4):
    msLogo.forward(50)
    msLogo.left(90)

#rectangle
for x in range(2):
    msLogo.forward(50)
    msLogo.left(90)
    msLogo.forward(100)
    msLogo.left(90) 

#canvas in 4 colums
msLogo.left(90)
msLogo.forward(200)
msLogo.backward(400)

msLogo.left(90)
msLogo.backward(100)
msLogo.right(90)
msLogo.forward(400)

msLogo.right(90)
msLogo.forward(100)
msLogo.right(90)
msLogo.forward(400)

#spikes
msLogo.left(30)
for x in range(6):
    msLogo.forward(100)
    msLogo.backward(100)
    msLogo.left(60)

#hexagon
for x in range(6):
    msLogo.forward(100)
    msLogo.right(60)

#draw x
msLogo.right(45)
msLogo.backward(200)
msLogo.forward(100)
msLogo.left(90)
msLogo.forward(100)
msLogo.backward(200)

#draw grid
def draw_hashed_axis():
    msLogo.pendown()
    for i in range(16):
        msLogo.forward(25)
        msLogo.right(90)
        msLogo.forward(10)
        msLogo.backward(20)
        msLogo.forward(10)
        msLogo.left(90)
msLogo.penup()
msLogo.setposition(0,200)
msLogo.right(90)
draw_hashed_axis()
msLogo.penup()
msLogo.setposition(-200,0)
msLogo.left(90)
draw_hashed_axis()

#braclet 
def circle():
    msLogo.circle(10)
    msLogo.right(10)
    msLogo.forward(20)

for x in range(36):
    circle
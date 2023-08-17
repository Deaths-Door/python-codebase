import turtle

class WoerterZeichner:
    def __init__(self,size = 100,startingPosition = 0,endingPosition = 0) -> None: 
        self._size = size
        self._startingPostion = startingPosition 
        self._endingPosition = endingPosition 

        self._t = turtle.Turtle()
        self._t.screen.screensize(500,500)
        self._t.goto(self._startingPostion,self._endingPosition)

    def currentPosition(self) : return self._t.position()
    def __reset__(self):
        self._t.goto(self.currentPosition())
    def E(self):
        _third = self._size/3
        self._t.left(90)
        self._t.forward(_third)
        self._t.right(90)
        self._t.forward(_third)
        self._t.penup()
        self._t.right(90)
        self._t.forward(_third)
        self._t.left(270)
        self._t.pendown()
        self._t.forward(_third)
        self._t.left(90)
        self._t.forward(_third)
        self._t.left(90)
        self._t.forward(_third)
    def L(self):
        self._t.down()
        self._t.right(90);
        self._t.forward(100)
        self._t.left(90)
        self._t.forward(50)
    def N(self):
        self._t.left(90)
        self._t.forward(100)
        self._t.right(155)
        self._t.forward(110)
        self._t.right(-155)
        self._t.forward(100)
   
wz = WoerterZeichner(100)
print(wz.currentPosition())
print(type(wz.currentPosition()))
wz.L()
wz.N()
wz.E()


while(True):
    wz._t.penup()
    wz._t.forward(10)
    wz._t.right(90)
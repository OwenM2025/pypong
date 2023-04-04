# Yes I am aware of how messy this is




import turtle
import random
#definition of gamepieces
l = turtle.Turtle();
r = turtle.Turtle();
b = turtle.Turtle();
s = turtle.Screen();
t = turtle.Turtle();
m = turtle.Turtle();
sw = turtle.Turtle();
ylist = [-50, -79, -27, 15, 34, 41, 6, 84, 119, 28]



s.title("Ping!")
font=("Arial", 25, "normal")
#def setscreen1():


def setgamescreen():
  s.setup(width=650, height=650)
  rectCors = ((-40,10),(40,10),(40,-10),(-40,-10))
  s.register_shape('rectangle',rectCors)
  linecors = ((-350,-350),(-350,350),(-550,350),(-550,-350))
  s.register_shape('line',linecors)
  mcors = ((-500, -1), (500, -1), (-500, 1), (500, 1))
  s.register_shape('mid', mcors)
  m.shape('mid')
  l.shape('rectangle')
  r.shape('rectangle')
  b.shape('circle')
  t.shape('line')
  s.bgcolor(0,0,0)
  l.color("white")
  r.color("white")
  b.color("white")
  t.color("white")
  m.color("white")
  m.penup()
  t.penup()
  l.penup()
  r.penup()
  b.penup()
  sw.penup()


b.speed(5)
p1s = 0
p2s = 0
sw.setpos(380, -150)
sw.write(p1s, False, align = "center")
sw.setpos(380, 150)
sw.write(p2s, False, align = "center")

def reset():
  b.sety(random.choice(ylist))
  b.setx(40)

b.setpos(40, 100)
l.setpos(-350, 0)
r.setpos(350, 0)

def moveL():
  s.onkeypress(moveUl, 'w')
  s.onkeypress(moveDl, 's')
  s.listen()
def printx():
  s.onkey(px, "e")
  s.listen()
def px():
  print(l.ycor())
def moveR():
  s.onkeypress(moveUr, "Up")
  s.onkeypress(moveDr, "Down")
  s.listen()
  
def deff1():
  s.onkey(setgamescreen, "p")

def moveUl():
  l.sety(lypos + 10)

def moveDl():
  l.sety(lypos - 10)

def moveUr():
  r.sety(rypos + 10)

def moveDr():
  r.sety(rypos - 10)
  
def limit(lefty, righty):
  if (lefty < -320):
    l.sety(-320)
  elif (righty < -320):
    r.sety(-320)
  elif (lefty > 300):
    l.sety(300)
  elif (righty > 300):
    r.sety(300)
    
#end defining functions

while True:
  
  if (b.xcor() < -400):
    reset()
    b.left(random.randint(0,180))
    print("player 1 scored")
    p1s = int(p1s + 1)
    print("score is", p1s, "to", p2s)
    sw.setpos(380, -150)
    sw.write(p1s, False, align = "center")
  elif (b.xcor() > 400):
    reset()
    b.right(random.randint(-180,0))
    print("player 2 scored")
    p2s = int(p2s + 1)
    print("score is", p1s, "to", p2s)
    sw.setpos(380, 150)
    sw.write(p2s, False, align = "center")
  else:
    lypos = l.ycor()
    rypos = r.ycor()
    dl = b.distance(l.xcor(), l.ycor())
    dr = b.distance(r.xcor(), r.ycor())
    moveL()
    moveR()
    deff1()
    limit(lypos, rypos)
    if (dl < 30):
      b.left(160)
    elif (dr < 30):
      b.right(160)
    else:
      pass
    

    b.fd(3)
    printx()
  if (b.ycor() <= -320):
    b.left(90)
  elif (b.ycor() >= 300):
    b.right(90)
  else:
      pass
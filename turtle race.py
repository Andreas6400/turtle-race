#import von 
from turtle import *
from random import randint

#geschwindkeit des Stiftes zum Zeichnen, eingefügt aus turtle
speed(10)
#stift aus
penup()
#postionswechsel zu x -140 y 140
goto(-140,140)

#erstellung des koordinatensystems
for step in range(15):
    #zahlen werden mittig an jede Spaltenstich angesetzt
    write(step, align='center')
    right(90)
    #Stiche der Spalten werden unterbrochen dargestellt
    for num in range(7):
        penup()
        forward(15)
        pendown()
        forward(15)
    penup()
    backward(210)
    left(90)
    forward(20)

#Schildkröten werden erstellt und eigentschaften zugewiesen
schildk1 = Turtle()
schildk1.color('red')
schildk1.shape('turtle')

#stift an/ aus; postionswechsel
schildk1.penup()
schildk1.goto(-160, 100)
schildk1.pendown()

#drehung einer schildkröte - range(10) 0-9
#drehung der schildkröte hier 10 mal 36 Grad = 360 Grad
for turn in range(10):
    schildk1.right(36)

schildk2 = Turtle()
schildk2.color('blue')
schildk2.shape('turtle')

schildk2.penup()
schildk2.goto(-160, 70)
schildk2.pendown()

#drehung einer schildkröte - range(10) 0-9
#drehung der schildkröte hier 72 mal 5 Grad = 360 Grad
for turn in range(72):
    schildk2.right(5)

schildk3 = Turtle()
schildk3.color('yellow')
schildk3.shape('turtle')

schildk3.penup()
schildk3.goto(-160, 40)
schildk3.pendown()

for turn in range(10):
    schildk3.right(36)

schildk4 = Turtle()
schildk4.color('green')
schildk4.shape('turtle')

schildk4.penup()
schildk4.goto(-160, 10)
schildk4.pendown()

for turn in range(10):
    schildk4.right(36)

schildk5 = Turtle()
schildk5.color('brown')
schildk5.shape('turtle')

schildk5.penup()
schildk5.goto(-160, -20)
schildk5.pendown()

for turn in range(10):
    schildk5.right(36)

schildk6 = Turtle()
schildk6.color('black')
schildk6.shape('turtle')

schildk6.penup()
schildk6.goto(-160, -50)
schildk6.pendown()

for turn in range(10):
    schildk6.right(36)

#die schildk bewegt sich jede Runde zwischen 
for turn in range(100):
    schildk1.forward(randint(1,5))
    schildk2.forward(randint(1,5))
    schildk3.forward(randint(1,5))
    schildk4.forward(randint(1,5))
    schildk5.forward(randint(1,5))
    schildk6.forward(randint(1,5))
    
#schildkroten= [schildk1,schildk2, schildk3, schildk4, schildk5, schildk6]
    #if(schildkroten.getscreen()==schildkroten.goto(null,-60):
    #   for turn in range(1):
    #   schildkroten.right(360)

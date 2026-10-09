#Forfatter Patrick W. Hedegaard
# 09/10-2026
# Mini projekt analog ur

import turtle
import time
import datetime

#Kunne ikke få pygames til at fungere, ved ikke hvorfor så prøver en anden løsning.

#display setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Analog Clock")
screen.tracer(0) #Slukker for animationen så viseren flytter sig med det samme.

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

#ur funktion
def draw_clock():
    pen.clear() 
    
    #urskive
    pen.penup()
    pen.goto(0, -150) #centrer cirklen
    pen.setheading(0) 
    pen.pendown()
    pen.pensize(3)
    pen.circle(150)
   
    
    #time markeringer
    for i in range(12):
        pen.penup()
        pen.goto(0, 0)
        pen.setheading(i * 30)
        pen.forward(135)
        pen.pendown()
        pen.pensize(5)
        pen.forward(15)
    
    #nuværende tid
    now = datetime.datetime.now()
    h = now.hour % 12
    m = now.minute
    s = now.second
    
    #Timeviser drejer 30 grader i timen
    hour_angle = 90 - ((h + m / 60) * 30)
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(hour_angle)
    pen.pendown()
    pen.pensize(6)
    pen.forward(70)
    
    
    #Minut viser drejer 6 grader i minuttet
    minute_angle = 90 - ((m + s / 60) * 6)
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(minute_angle)
    pen.pendown()
    pen.pensize(4)
    pen.forward(110)
    
    
    #Sekund viser drejer 6 grader per sekund
    second_angle = 90 - (s * 6)
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(second_angle)
    pen.pendown()
    pen.pensize(2)
    pen.pencolor("red")
    pen.forward(130)
    
    pen.pencolor("black") #genstarter farven til den næste frame
    screen.update() #pusher tegningen til vinduet

def update_clock():
    draw_clock()
    screen.ontimer(update_clock, 1000)

update_clock()
screen.mainloop()
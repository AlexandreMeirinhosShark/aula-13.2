from time import sleep
from turtle import *

ad = Screen()
ad.bgcolor("skyblue")
ad.title("As Aventuras de Turtle")
char = RawTurtle(ad)
char.pu()
bg = RawTurtle(ad, "arrow", False)
bg.hideturtle()
sleep(1)


def forwarder():
    if moving:
        char.fd(3)
    ad.ontimer(forwarder, 20)


moving = False


# Define the function to start moving the turtle
def start_move():
    global moving
    moving = True


# Define the function to stop moving the turtle
def stop_move():
    global moving
    moving = False


ad.listen()
ad.onkeypress(start_move, "Up")
ad.onkey(stop_move, "Up")
forwarder()
ad.mainloop()

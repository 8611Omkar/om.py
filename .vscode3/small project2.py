# from codecs import getdecoder
# from fcntl import F_GETFD
import turtle


def draw_square(some_turtle):
    
    for i in range(1,5):
        some_turtle.forward(200)
        some_turtle.right(90)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    #Turtle Brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(8)
    brad.pensize(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    window.exitonclick()
    
# GETFD draw_art:
            
get draw.art
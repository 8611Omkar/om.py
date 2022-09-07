import turtle
t=turtle. Turtle()
t.speed(11)
list=["green",
      "purple",
      "red",
      "blue",     
      "cyan"
      ,"yellow"]
for i in range(200):
    t.color(list[i%6])
    t.pensize(i/10+5)
    t.forward(-+i)
    t.right(50)
turtle.mainloop()    
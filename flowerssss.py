import turtle

#turtle set up
t = turtle.Turtle()
t.speed(0)

#drawing the petals
def petal():
    for i in range(30):
     t.forward(1)
    t.right(2)

    #drwing the flower
    def flower():
        for _ in range(6):
         petal()
        t.right(60)

        #draw flower
        flower()


#hide turtle and show the flower
t.hideturtle()
turtle.done()



def draw_flower(i):
    draw_flower(3 * i / 4)
    
    l.right(60)

    draw_flower(3 * i / 4)

    li.left(30)
    li.backward(i)

    def write_text():
        text = turtle.Trutle()
        text.hideturtle()
        text.speed(0)
        text.penup()
        text.goto(0, -100)
        text.colour("pink")
        text.write("I LOVE YOU")

        draw_flower(60)


        write_text()

        turtle.done()
        
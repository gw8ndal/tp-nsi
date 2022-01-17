import turtle

height = 400
width = 400
turtle.screensize(canvwidth=width, canvheight=height, bg="black")
t = turtle.Turtle()
t.speed(0)
t.pencolor("white")
t.penup()
t.sety(0)
t.setx(0)
t.pendown()

def koch (n, longueur):
    if n == 0:
        t.forward(longueur)
    else:
        koch(n-1, longueur/3)
        t.left(60)
        koch(n-1, longueur/3)
        t.right(120)
        koch(n-1, longueur/3)
        t.left(60)
        koch(n-1, longueur/3)


for i in range(3):
    koch(3, 3**5)
    t.right(120)
a = input("Fermer la fenêtre\n")
if a:
    turtle.bye()

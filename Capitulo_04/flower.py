import turtle
from polygon import arc


def petal(t, r, angle):
    """Dibuja un pétalo usando dos arcos."""
    for i in range(2):
        arc(t, r, angle)     # dibuja un arco
        t.lt(180-angle)      # gira para colocar el siguiente

def flower(t, n, r, angle):
    """Dibuja una flor con n pétalos."""
    for i in range(n):
        petal(t, r, angle)   # dibuja un pétalo
        t.lt(360.0/n)        # gira para repartirlos en círculo

def move(t, length):
    """Mueve la tortuga sin dibujar."""
    t.pu()
    t.fd(length)
    t.pd()


bob = turtle.Turtle()

# tres flores distintas
move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

bob.hideturtle()
turtle.mainloop()

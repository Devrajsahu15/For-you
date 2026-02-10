import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return (12 * math.cos(k)
            - 5 * math.cos(2 * k)
            - 2 * math.cos(3 * k)
            - math.cos(4 * k))

speed(0)
bgcolor("black")
pencolor("red")

# ---- TEXT UPPER HEART ----
penup()
goto(0, 250)   # upar position
pendown()
color("white")
write("     THIS IS FOR YOU🫀❤️", align="center", font=("Arial", 24, "bold"))
penup()
goto(0, 0)
pendown()

for i in range(6000):
    goto(hearta(i) * 20, heartb(i) * 20)
    for j in range(1):
        color("red")
        goto(0, 0)

done()

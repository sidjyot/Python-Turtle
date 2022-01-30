from turtle import *

speed(0)

def quarter_circle(size):
  for i in range(30):
    forward(size)
    right(3)


def petal(size):
  for i in range(2):
    quarter_circle(size)
    right(90)

def flower(petals, size):
  pencolor('red')
  pensize(3)
  pendown()
  for i in range(petals):
    petal(size)
    right(360/petals)

def stem(size):
  pencolor('green')
  pensize(5)
  pendown()
  right(90)
  forward(80)
  right(90)
  petal(size)
  right(270)
  forward(40)
  left(180)
  petal(1.5*size)
  right(180)
  forward(40)
  penup()
  backward(180)

s = int(3)
p = int(12)

stem(s)
flower(p, s)


import turtle

win = turtle.Sceen()
win.title("Pong Tutorial")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)

# Paddle B

# Ball

while True: 
  win.update()

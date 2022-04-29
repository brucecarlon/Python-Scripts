'''
This program shows a visual representation of a moving ball trapped in a room
under the asumptions that the ball-room system is isolated and the ball
doesnt lose any energy when bouncing off the walls

@author Bruce Mvubele
'''


from vpython import *



##objects
ball = sphere(pos=vector(-5,0,0), radius=0.5, color=color.cyan)
wallR = box(pos=vector(6,0,0), size=vector(1,12,12), color=color.green)
wallL = box(pos=vector(-6,0,0), size=vector(1,12,12), color=color.green)
wallbk = box(pos=vector(0,0,-6), size=vector(12,12,1), color=color.green)
wallTop = box(pos=vector(0,6,0), size=vector(12,1,12), color=color.green)
wallbottom = box(pos=vector(0,-6,0), size=vector(12,1,12), color=color.green)
ball.trail = curve(color=color.white)



## intial values
velocity = input('Enter initial velocity in form a b c: \n')
velocity = velocity.split()

## break velocity into components
a = eval(velocity[0])
b = eval(velocity[1])
c = eval(velocity[2])

## dynamic variables
ball.velocity = vector(a,b,c)
deltat = 0.005
t = 0
vscale = 0.1
#varr = arrow(pos=vector(ball.pos), axis=vector(vscale*ball.velocity), color=color.yellow)
                   
## calculations: reverse direction of ball if it touches the balls
scene.autoscale = 0
while t<10:
    rate(100)
    if ball.pos.x > wallR.pos.x:
        ball.velocity.x = -ball.velocity.x
    if ball.pos.x < wallL.pos.x:
        ball.velocity.x = -ball.velocity.x
    if ball.pos.y > wallTop.pos.y:
        ball.velocity.y = -ball.velocity.y
    if ball.pos.y < wallbottom.pos.y:
        ball.velocity.y = -ball.velocity.y
    if ball.pos.z > 6:
        ball.velocity.z= -ball.velocity.z
    if ball.pos.z < -6:
        ball.velocity.z = -ball.velocity.z
    ball.pos=ball.pos+ball.velocity*deltat
    ball.trail.append(pos=ball.pos)
    t = t + deltat
   # varr.pos = ball.pos
   # varr.axis=vscale*ball.velocity
    
    

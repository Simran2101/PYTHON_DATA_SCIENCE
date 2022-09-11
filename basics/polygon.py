from turtle import *

speed('slowest')
pencolor('red')
bgcolor('yellow')

side = 3
size = 200
for i in range(side):
    fd(size)
    lt(360/side)

mainloop()
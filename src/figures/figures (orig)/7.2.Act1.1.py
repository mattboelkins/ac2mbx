from figures import *

dx = 23
margin = 5
width = 8*dx + 2*margin
height = 5*dx + 2*margin

beginfigure("7.2.Act1.1", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -2, 7, 3])

Grid([-1,1,7], [-2,1,3], color=lightgray).draw()

axes = Axes()
axes.draw()
axes.setticks([-1,1,7], [-2,1,3])
axes.drawticks()
axes.setlabels([-1,1,7], [-2,1,3])
axes.drawlabels()


Label(r"$y$", [7,0], offset=[-3,3], alignment="rb").draw()
Label(r"$\frac{dy}{dt}$", [0,3], offset=[3,-3], alignment="lt").draw()


endfigure()

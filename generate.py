import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

x=0
y=0
z=0.5

length = 1
width = 1
height = 1

for j in range(0, 5):
    for i in range(0, 5):
        for t in range(0, 10):
            pyrosim.Send_Cube(name="Box", pos = [x, y, z + (t*1)] , size=[length, width, height])
            length = length * .9
            width = width * .9
            height = height * .9

        y = (y + 1)
        length = 1
        width = 1
        height = 1
    y = 0
    x = x + 1

pyrosim.End()
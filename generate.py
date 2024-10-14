import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

x=0
y=0
z=0.5

length = 1
width = 1
height = 1

for t in range(0, 10):
    pyrosim.Send_Cube(name="Box", pos=[x,y, z + (t*1)] , size=[length * (t*1), width, height])

pyrosim.End()
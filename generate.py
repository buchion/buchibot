import pyrosim.pyrosim as pyrosim


x=0
y=0
z=1.5

length = 1
width = 1
height = 1

# print(dir(pyrosim))
# dir(pyrosim)
print(pyrosim.Send_Joint.__doc__)


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="box", pos = [3, 3, z] , size=[length, width, height])
    pyrosim.End()



def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    # pyrosim.Send_Cube(name="Torso", pos = [0, 0, 1.5] , size=[length, width, height])

    # pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -0.5, 1])
    # # pyrosim.Send_Joint(name = "Torso_BackLeg", parent= "Torso", child = "BackLeg" , type = "revolute", position = [0,0,0])
    # pyrosim.Send_Cube(name="BackLeg", pos = [0, 1, 0.5], size=[length, width, height])

    # # pyrosim.Send_Joint(name = "Torso_FrontLeg", parent= "Torso", child = "FrontLeg", type = "revolute", position = [0,0,0])
    # pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 0.5, 1])
    # pyrosim.Send_Cube(name="FrontLeg", pos = [0, -1, 0.5], size=[length, width, height])


    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.4] , size=[length, width, height])  # Center torso at z=1

    # BackLeg Joint: Attach at the bottom of the torso, centered at (0, -0.5, 0.5)
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -0.5, 0.5])
    pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[length, width, height])  # Shifted to align with joint

    # FrontLeg Joint: Attach at the bottom of the torso, centered at (0, 0.5, 0.5)
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 0.5, 0.5])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[length, width, height])  # Shifted to align with joint


    pyrosim.End()

Create_World()
Create_Robot()

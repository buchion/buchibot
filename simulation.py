# import pybullet as p
# import time
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import numpy as np
# import os

# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())

# p.setGravity(0, 0, -9.8)
# robotId = p.loadURDF("body.urdf")
# planeId = p.loadURDF("plane.urdf")
# p.loadSDF("world.sdf")

# pyrosim.Prepare_To_Simulate(robotId)

# os.makedirs("data", exist_ok=True)

# num_steps = 1000

# amplitude_BackLeg = np.pi / 4
# frequency_BackLeg = 2
# phaseOffset_BackLeg = 0

# amplitude_FrontLeg = np.pi / 4
# frequency_FrontLeg = 2
# phaseOffset_FrontLeg = 0


# targetAngles_BackLeg = amplitude_BackLeg * np.sin(np.linspace(0, 2 * np.pi * frequency_BackLeg, num_steps) + phaseOffset_BackLeg)
# targetAngles_FrontLeg = amplitude_FrontLeg * np.sin(np.linspace(0, 2 * np.pi * frequency_FrontLeg, num_steps) + phaseOffset_FrontLeg)

# np.save("data/targetAngles_BackLeg.npy", targetAngles_BackLeg)
# np.save("data/targetAngles_FrontLeg.npy", targetAngles_FrontLeg)

# backLegSensorValues = np.zeros(num_steps)
# frontLegSensorValues = np.zeros(num_steps)

# for i in range(num_steps):
#     p.stepSimulation()

#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg") or 0
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg") or 0

#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex=robotId,
#         jointName=b"Torso_BackLeg",
#         controlMode=p.POSITION_CONTROL,
#         targetPosition=targetAngles_BackLeg[i],
#         maxForce=30
#     )

#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex=robotId,
#         jointName=b"Torso_FrontLeg",
#         controlMode=p.POSITION_CONTROL,
#         targetPosition=targetAngles_FrontLeg[i],
#         maxForce=30
#     )

#     time.sleep(1 / 60)

# np.save("data/backLegSensorValues.npy", backLegSensorValues)
# np.save("data/frontLegSensorValues.npy", frontLegSensorValues)

# print("Data Saved Successfully!")
# p.disconnect()


import pybullet as p
import pybullet_data
import time
import constants as c
from world import WORLD
from robot import ROBOT
from pyrosim.neuralNetwork import NEURAL_NETWORK

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, c.GRAVITY)

        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for t in range(c.NUM_STEPS):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
            time.sleep(1 / 60)

    def __del__(self):
        p.disconnect()

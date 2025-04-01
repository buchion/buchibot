import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import os

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setGravity(0, 0, -9.8)
robotId = p.loadURDF("body.urdf")
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

os.makedirs("data", exist_ok=True)

num_steps = 1000

amplitude_BackLeg = np.pi / 4
frequency_BackLeg = 2
phaseOffset_BackLeg = 0
 
amplitude_FrontLeg = np.pi / 4
frequency_FrontLeg = 2
phaseOffset_FrontLeg = 0


targetAngles_BackLeg = amplitude_BackLeg * np.sin(np.linspace(0, 2 * np.pi * frequency_BackLeg, num_steps) + phaseOffset_BackLeg)
targetAngles_FrontLeg = amplitude_FrontLeg * np.sin(np.linspace(0, 2 * np.pi * frequency_FrontLeg, num_steps) + phaseOffset_FrontLeg)

np.save("data/targetAngles_BackLeg.npy", targetAngles_BackLeg)
np.save("data/targetAngles_FrontLeg.npy", targetAngles_FrontLeg)

print("Motor command data saved. Exiting before simulation for analysis.")

backLegSensorValues = np.zeros(num_steps)
frontLegSensorValues = np.zeros(num_steps)

print("Starting Simulation...")

for i in range(num_steps):
    p.stepSimulation()

    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg") or 0
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg") or 0

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b"Torso_BackLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAngles_BackLeg[i],
        maxForce=30
    )

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b"Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAngles_FrontLeg[i],
        maxForce=30
    )

    time.sleep(1 / 60)

np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)

print("Data Saved Successfully!")
p.disconnect()

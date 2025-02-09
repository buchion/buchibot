import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import os

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
robotId = p.loadURDF("body.urdf")
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

os.makedirs("data", exist_ok=True)

num_steps = 200
backLegSensorValues = np.zeros(num_steps)
frontLegSensorValues = np.zeros(num_steps)  # Adding front leg sensor

print("Starting Simulation...")


for i in range(num_steps):
    p.stepSimulation()
    
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")


    print(f"{i}: Back Leg = {backLegTouch}, Front Leg = {frontLegTouch}")

    backLegSensorValues[i] = backLegTouch if backLegTouch is not None else 0
    frontLegSensorValues[i] = frontLegTouch if frontLegTouch is not None else 0
    
    time.sleep(1/60)


print("Simulation Complete. Saving Data...")

np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
print("Saved files:", os.listdir("data"))

print("Data Saved Successfully!")

p.disconnect()

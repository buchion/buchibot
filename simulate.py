import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import os

# Connect to physics simulation
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Set up environment
p.setGravity(0, 0, -9.8)
robotId = p.loadURDF("body.urdf")
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

# Prepare simulation
pyrosim.Prepare_To_Simulate(robotId)

# Ensure data directory exists BEFORE simulation starts
os.makedirs("data", exist_ok=True)

# Initialize sensor value storage
num_steps = 200
backLegSensorValues = np.zeros(num_steps)
frontLegSensorValues = np.zeros(num_steps)  # Adding front leg sensor

print("Starting Simulation...")

# Run simulation loop
for i in range(num_steps):
    p.stepSimulation()
    
    # Read sensor values
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # Debugging prints
    print(f"Step {i}: Back Leg Sensor = {backLegTouch}, Front Leg Sensor = {frontLegTouch}")

    # Ensure values are not None
    backLegSensorValues[i] = backLegTouch if backLegTouch is not None else 0
    frontLegSensorValues[i] = frontLegTouch if frontLegTouch is not None else 0
    
    time.sleep(1/60)  # Maintain simulation timing

# Print collected sensor values
print("Simulation Complete. Saving Data...")

# Save sensor values
np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
print("Saved files:", os.listdir("data"))

print("Data Saved Successfully!")

# Disconnect from simulation
p.disconnect()

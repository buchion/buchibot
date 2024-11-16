import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setGravity(0,0,-9.8)
robotId = p.loadURDF("body.urdf")
planeId = p.loadURDF("plane.urdf")

p.loadSDF("world.sdf")

print("robotId")
print(robotId)
pyrosim.Prepare_To_Simulate(robotId)


for t in range(0, 1000):
    
    p.stepSimulation()
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    print("BackLeg Touch Sensor Value:", backLegTouch)
    time.sleep(1/60)
    # print(t)

p.disconnect()




# import pybullet as p
# import time
# import pybullet_data
# import pyrosim.pyrosim as pyrosim  # Import pyrosim for sensor access

# # Connect to physics client in GUI mode
# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())

# # Set gravity for the simulation
# p.setGravity(0, 0, -9.8)

# # Load URDF models for the plane and robot
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")

# # Load an SDF world
# p.loadSDF("world.sdf")

# # Print the robot ID
# print("robotId")
# print(robotId)

# # Prepare Pyrosim for sensor simulation
# pyrosim.Prepare_To_Simulate(robotId)

# # Run the simulation loop
# for t in range(0, 1000):
#     # Step the simulation
#     p.stepSimulation()
    
#     # Get the touch sensor value for the BackLeg link
#     backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    
#     # Print the sensor value (optional, to verify it's working)
#     print("BackLeg Touch Sensor Value:", backLegTouch)
    
#     # Pause for real-time simulation speed
#     time.sleep(1/60)

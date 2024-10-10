import pybullet as p
import time

physicsClient = p.connect(p.GUI)
# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.loadSDF("box.sdf")
for t in range(0, 1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(t)


p.disconnect()
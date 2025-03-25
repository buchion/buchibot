import pybullet as p

class WORLD:
    def __init__(self):
        p.loadSDF("world.sdf")
        p.loadURDF("plane.urdf")

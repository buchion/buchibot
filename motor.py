import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as np

class MOTOR:
    def __init__(self, jointName):
        if isinstance(jointName, bytes):
            jointName = jointName.decode("utf-8")
        
        self.jointName = jointName
        self.amplitude = c.AMPLITUDE
        self.frequency = c.FREQUENCY / 2 if "BackLeg" in jointName else c.FREQUENCY
        self.offset = c.PHASE_OFFSET

        # Optional: rhythmic motor values if used later
        self.motorValues = self.amplitude * np.sin(
            np.linspace(0, 2 * np.pi * self.frequency, c.NUM_STEPS) + self.offset
        )

    def Set_Value(self, robotId, targetPosition): 
        joint_name_bytes = self.jointName.encode("utf-8")

        if joint_name_bytes not in pyrosim.jointNamesToIndices:
            raise KeyError(
                f"Joint name '{self.jointName}' not found in pyrosim.jointNamesToIndices.\n"
                f"Available keys: {[k.decode('utf-8') for k in pyrosim.jointNamesToIndices.keys()]}"
            )

        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=joint_name_bytes,
            controlMode=p.POSITION_CONTROL,
            targetPosition=targetPosition,
            maxForce=10
        )

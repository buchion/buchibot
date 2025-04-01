
import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        numJoints = p.getNumJoints(self.robotId)
        print("Joint Names from PyBullet:")
        for i in range(numJoints):
            jointInfo = p.getJointInfo(self.robotId, i)
            print(f"Index: {i}, Name: {jointInfo[1]}")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.sensors = {}
        self.motors = {}

        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        self.nn = NEURAL_NETWORK("brain.nndf")

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            print(f"jointName: {jointName}, Type: {type(jointName)}") 
            jointName = jointName.decode("utf-8") if isinstance(jointName, bytes) else jointName
            self.motors[jointName] = MOTOR(jointName)

    def Sense(self, t):
        for sensor in self.sensors.values():
            sensor.Get_Value(t)

    def Think(self):
        self.nn.Update()
        self.nn.Print()
        

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                print(neuronName)
        for motor in self.motors.values():
            motor.Set_Value(self.robotId, t)

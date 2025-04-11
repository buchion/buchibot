import math
import pyrosim.pyrosim as pyrosim
import pyrosim.constants as c

class NEURON: 

    def __init__(self, line):
        self.Determine_Name(line)
        self.Determine_Type(line)
        self.Search_For_Link_Name(line)
        self.Search_For_Joint_Name(line)
        self.Set_Value(0.0)

    def Add_To_Value(self, value):
        self.Set_Value(self.Get_Value() + value)

    def Get_Joint_Name(self):
        if not hasattr(self, 'jointName'):
            raise AttributeError(f"Motor neuron '{self.name}' is missing a jointName. Check your .nndf definition.")
        return self.jointName

    def Get_Link_Name(self):
        return getattr(self, 'linkName', None)

    def Get_Name(self):
        return self.name

    def Get_Value(self):
        return self.value

    def Set_Value(self, value):
        self.value = value

    def Is_Sensor_Neuron(self):
        return self.type == c.SENSOR_NEURON

    def Is_Hidden_Neuron(self):
        return self.type == c.HIDDEN_NEURON

    def Is_Motor_Neuron(self):
        return self.type == c.MOTOR_NEURON

    def Update_Sensor_Neuron(self):
        if not hasattr(self, 'linkName'):
            raise AttributeError(f"Sensor neuron '{self.name}' is missing a linkName. Check your .nndf definition.")
        self.Set_Value(pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName))
    
    def Update_Hidden_Or_Motor_Neuron(self):
        self.value = math.pi / 4.0

    def Threshold(self):
        self.value = math.tanh(self.value)

    def Print(self):
        self.Print_Value()

# -------------------------- Private methods -------------------------

    def Determine_Name(self, line):
        if "name" in line:
            splitLine = line.split('"')
            self.name = splitLine[1]
        else:
            raise ValueError(f"Neuron line missing 'name': {line}")

    def Determine_Type(self, line):
        if "sensor" in line:
            self.type = c.SENSOR_NEURON
        elif "motor" in line:
            self.type = c.MOTOR_NEURON
        else:
            self.type = c.HIDDEN_NEURON

    def Search_For_Joint_Name(self, line):
        if "jointName" in line:
            splitLine = line.split('"')
            if len(splitLine) >= 6:
                self.jointName = splitLine[5]
            else:
                raise ValueError(f"Malformed jointName line: {line}")
        elif self.Is_Motor_Neuron():
            raise ValueError(f"Motor neuron '{self.name}' is missing jointName in: {line}")

    def Search_For_Link_Name(self, line):
        if "linkName" in line:
            splitLine = line.split('"')
            if len(splitLine) >= 6:
                self.linkName = splitLine[5]
            else:
                raise ValueError(f"Malformed linkName line: {line}")
        elif self.Is_Sensor_Neuron():
            raise ValueError(f"Sensor neuron '{self.name}' is missing linkName in: {line}")

    def Print_Name(self):
        print(self.name)

    def Print_Type(self):
        print(self.type)

    def Print_Value(self):
        print(self.value, " ", end="")

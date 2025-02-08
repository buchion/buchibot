# import numpy as np
# import matplotlib.pyplot as plt

# # Load sensor values
# backLegSensorValues = np.load("data/backLegSensorValues.npy")

# # Print the loaded values
# print(backLegSensorValues)

# # Plot the sensor values
# plt.plot(backLegSensorValues, label="Back Leg Sensor Values")
# plt.xlabel("Time (index)")
# plt.ylabel("Sensor Reading")
# plt.title("Back Leg Sensor Values Over Time")
# plt.legend()
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Load sensor values
backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")

# Print the loaded values
print("Back Leg Sensor Values:", backLegSensorValues)
print("Front Leg Sensor Values:", frontLegSensorValues)

# Plot sensor values
plt.plot(backLegSensorValues, label="Back Leg Sensor", linewidth=2)  # Thicker line
plt.plot(frontLegSensorValues, label="Front Leg Sensor")  # Default width

# Add labels and title
plt.xlabel("Time (index)")
plt.ylabel("Sensor Reading")
plt.title("Sensor Values Over Time")

# Add a legend to differentiate the lines
plt.legend()

# Show the plot
plt.show()

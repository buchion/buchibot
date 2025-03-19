# import numpy as np
# import matplotlib.pyplot as plt

# targetAngles_BackLeg = np.load("data/targetAngles_BackLeg.npy")
# targetAngles_FrontLeg = np.load("data/targetAngles_FrontLeg.npy")


# plt.figure(figsize=(10, 5))
# plt.plot(targetAngles_BackLeg, label="BackLeg Motor Command", color="blue")
# plt.plot(targetAngles_FrontLeg, label="FrontLeg Motor Command", color="red")
# plt.xlabel("Time Step")
# plt.ylabel("Target Angle (radians)")
# plt.title("Motor Commands Over Time")
# plt.legend()
# plt.grid()
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

targetAngles_BackLeg = np.load("data/targetAngles_BackLeg.npy")
targetAngles_FrontLeg = np.load("data/targetAngles_FrontLeg.npy")

time_steps = np.arange(len(targetAngles_BackLeg))

plt.figure(figsize=(10, 5))
plt.plot(time_steps, targetAngles_BackLeg, label="Back Leg", color="blue")
plt.plot(time_steps, targetAngles_FrontLeg, label="Front Leg", color="red", linestyle="dashed")
plt.xlabel("Time Step")
plt.ylabel("Target Angle (radians)")
plt.title("Motor Command Sinusoids")
plt.legend()
plt.grid()
plt.show()

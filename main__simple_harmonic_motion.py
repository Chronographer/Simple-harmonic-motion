import SimpleHarmonicMotion_euler
import SimpleHarmonicMotion_eulercromer
import matplotlib.pyplot as plt
import numpy as np

initialTheta = np.pi / 4
initialOmega = 0.0
initialAlpha = 0.0
initialTime = 0.0

timeStep = 0.01
maxTime = 20.0
gravity = 9.8
pendulumLength = 2.0
mass = 2
plotType = "velocity"

if plotType == "energy":
    yAxisLabel = "Energy"
elif plotType == "angle":
    yAxisLabel = "Angle (radians)"
elif plotType == "velocity":
    yAxisLabel = "Velocity (m/s)"
elif plotType == "acceleration":
    yAxisLabel = "Acceleration (m/s^2)"

SimpleHarmonicMotion_euler.euler(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, plotType)
SimpleHarmonicMotion_eulercromer.eulercromer(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, plotType)

plt.legend(loc="upper right")
plt.grid(True)
plt.suptitle("SHM as computed using the Euler and Euler-Cromer methods")
plt.xlabel("Time (sec)")
plt.ylabel(yAxisLabel)
plt.show()

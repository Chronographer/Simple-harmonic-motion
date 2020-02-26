import SimpleHarmonicMotion_euler
import SimpleHarmonicMotion_eulercromer
import matplotlib.pyplot as plt
import numpy as np

initialTheta = np.pi / 4
initialOmega = 0.0
initialAlpha = 0.0
initialTime = 0.0

timeStep = 0.1
maxTime = 20.0
gravity = 9.8
pendulumLength = 2.0
mass = 2
plotType = "phaseSpace"

if plotType == "energy":
    xAxisLabel = "Time (sec)"
    yAxisLabel = "Energy"
elif plotType == "angle":
    xAxisLabel = "Time (sec)"
    yAxisLabel = "Angle (radians)"
elif plotType == "velocity":
    xAxisLabel = "Time (sec)"
    yAxisLabel = "Velocity (m/s)"
elif plotType == "acceleration":
    xAxisLabel = "Time (sec)"
    yAxisLabel = "Acceleration (m/s^2)"
elif plotType == "phaseSpace":
    xAxisLabel = "Velocity (m/s)"
    yAxisLabel = "Angle (radians)"

SimpleHarmonicMotion_euler.euler(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, plotType)
SimpleHarmonicMotion_eulercromer.eulercromer(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, plotType)

plt.legend(loc="upper right")
plt.grid(True)
plt.suptitle("SHM as computed using the Euler and Euler-Cromer methods")
plt.xlabel(xAxisLabel)
plt.ylabel(yAxisLabel)
plt.show()

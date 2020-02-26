import SimpleHarmonicMotion_euler
import SimpleHarmonicMotion_eulercromer
import matplotlib.pyplot as plt
import numpy as np

timeStep = 0.01
maxTime = 40.0
gravity = 9.8
pendulumLength = 2.0
mass = 2
plotType = "phaseSpace"  # this tells the program which kind of plot it should make. It accepts 'energy', 'angle', 'velocity', 'acceleration', and 'phaseSpace'

initialTheta = np.pi / 4
initialOmega = np.sqrt(gravity/pendulumLength)
initialAlpha = 0.0
initialTime = 0.0

if plotType == "energy":  # this automatically sets the x and y axis labels to the appropriate values based on what you are plotting.
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
plt.grid()
plt.suptitle("SHM as computed using the Euler and Euler-Cromer methods")
plt.xlabel(xAxisLabel)
plt.ylabel(yAxisLabel)
plt.show()

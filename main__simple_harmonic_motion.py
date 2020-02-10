import SimpleHarmonicMotion_euler
import SimpleHarmonicMotion_eulercromer
import matplotlib.pyplot as plt
import numpy as np

gravity = 9.8
pendulumLength = 0.2

initialTheta = np.pi / 4
initialOmega = 0.0
initialAlpha = 0.0
initialTime = 0.0

mass = 2

timeStep = 0.01
maxTime = 20.0

#SimpleHarmonicMotion_euler.euler(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass)
SimpleHarmonicMotion_eulercromer.eulercromer(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, "angle")
SimpleHarmonicMotion_eulercromer.eulercromer(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, "velocity")

plt.legend(loc="upper right")
plt.grid(True)
plt.suptitle("SHM as computed using the Euler and Euler-Cromer methods")
plt.xlabel("Time (sec)")
plt.ylabel("Energy")
plt.show()

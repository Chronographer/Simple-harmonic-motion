import SimpleHarmonicMotion_euler
import SimpleHarmonicMotion_eulercromer
import matplotlib.pyplot as plt
import numpy as np

gravity = 9.8
pendulumLength = 1.0

initialTheta = np.pi / 4
initialOmega = 0.0
initialAlpha = 0.0
initialTime = 0.0

timeStep = 0.01
maxTime = 20.0

SimpleHarmonicMotion_euler.euler(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime)
SimpleHarmonicMotion_eulercromer.eulercromer(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime)

plt.legend()
plt.grid(True)
plt.show()

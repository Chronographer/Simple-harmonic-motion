import matplotlib.pyplot as plt
import numpy as np

gravity = 9.8
pendulumLength = 1.0

initialTheta = np.pi/4
initialOmega = 0.0
initialAlpha = 0.0
initialTime = 0.0

currentTheta = initialTheta
currentOmega = initialOmega
currentAlpha = initialAlpha
currentTime = initialTime

timeStep = 0.01
maxTime = 2.0

thetaTable = []
omegaTable = []
alphaTable = []
timeTable = []

while currentTime <= maxTime:
    print("time is: " + str(currentTime))
    print("theta is: " + str(currentTheta))
    print("omeaga is: " + str(currentOmega))

    currentAlpha = (gravity*currentTheta)/pendulumLength
    currentTheta = currentTheta + currentOmega*timeStep
    currentOmega = currentOmega - currentAlpha*timeStep
    currentTime = currentTime + timeStep

    alphaTable.append(currentAlpha)
    omegaTable.append(currentOmega)
    thetaTable.append(currentTime)
    timeTable.append(currentTime)

plt.plot(timeTable, omegaTable)
plt.grid(True)
plt.show()

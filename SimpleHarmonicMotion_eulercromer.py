import matplotlib.pyplot as plt
import numpy as np


def eulercromer():
    gravity = 9.8
    pendulumLength = 1.0

    initialTheta = np.pi / 4
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
        currentAlpha = (gravity * currentTheta) / pendulumLength
        currentOmega = currentOmega - currentAlpha * timeStep
        currentTheta = currentTheta + currentOmega * timeStep
        currentTime = currentTime + timeStep

        alphaTable.append(currentAlpha)
        omegaTable.append(currentOmega)
        thetaTable.append(currentTime)
        timeTable.append(currentTime)

    plt.plot(timeTable, omegaTable, label="eulerCromer")
    plt.grid(True)
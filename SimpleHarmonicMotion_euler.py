import matplotlib.pyplot as plt


def euler(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime):
    currentTheta = initialTheta
    currentOmega = initialOmega
    currentTime = initialTime

    thetaTable = []
    omegaTable = []
    alphaTable = []
    timeTable = []

    while currentTime <= maxTime:
        currentAlpha = (gravity*currentTheta)/pendulumLength
        currentTheta = currentTheta + currentOmega*timeStep
        currentOmega = currentOmega - currentAlpha*timeStep
        currentTime = currentTime + timeStep

        alphaTable.append(currentAlpha)
        omegaTable.append(currentOmega)
        thetaTable.append(currentTime)
        timeTable.append(currentTime)

    plt.plot(timeTable, omegaTable, label="euler")

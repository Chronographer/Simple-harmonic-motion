import matplotlib.pyplot as plt


def euler(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, plotType):
    currentTheta = initialTheta
    currentOmega = initialOmega
    currentTime = initialTime

    initialEnergy = (0.5) * mass * pendulumLength**2 * (currentOmega**2 + (gravity / pendulumLength) * currentTheta**2)
    currentEnergy = initialEnergy

    thetaTable = []
    omegaTable = []
    alphaTable = []
    timeTable = []
    energyTable = []

    while currentTime <= maxTime:
        currentAlpha = (gravity * currentTheta) / pendulumLength
        currentTheta = currentTheta + currentOmega * timeStep
        currentOmega = currentOmega - currentAlpha * timeStep
        currentEnergy = currentEnergy + (0.5) * ((mass * pendulumLength * (currentOmega**2 + (gravity / pendulumLength) * currentTheta**2))) * (timeStep)**2
        currentTime = currentTime + timeStep


        alphaTable.append(currentAlpha)
        omegaTable.append(currentOmega)
        thetaTable.append(currentTime)
        timeTable.append(currentTime)
        energyTable.append(currentEnergy)

    plt.plot(timeTable, omegaTable, label="euler")

import matplotlib.pyplot as plt


def eulercromer(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, plotType):
    currentTheta = initialTheta
    currentOmega = initialOmega
    currentTime = initialTime

    thetaTable = []
    omegaTable = []
    alphaTable = []
    timeTable = []
    energyTable = []

    plotTable = []

    initialEnergy = (0.5) * mass * pendulumLength**2 * (currentOmega**2 + (gravity / pendulumLength) * currentTheta**2)
    currentEnergy = initialEnergy

    while currentTime <= maxTime:
        currentAlpha = (gravity * currentTheta) / pendulumLength
        currentOmega = currentOmega - currentAlpha * timeStep
        currentTheta = currentTheta + currentOmega * timeStep
        currentEnergy = currentEnergy + (0.5) * ((mass * pendulumLength * (currentOmega**2 + (gravity / pendulumLength) * currentTheta**2))) * (timeStep)**2 # this is currently incorrect.
        currentTime = currentTime + timeStep

        alphaTable.append(currentAlpha)
        omegaTable.append(currentOmega)
        thetaTable.append(currentTime)
        timeTable.append(currentTime)
        energyTable.append(currentEnergy)

        if plotType == "energy":
            plotTable.append(currentEnergy)
        elif plotType == "angle":
            plotTable.append(currentTheta)
        elif plotType == "velocity":
            plotTable.append(currentOmega)
        elif plotType == "acceleration":
            plotTable.append(currentAlpha)
        else:
            print(str(plotType) + " is not a valid plot type!")

    plt.plot(timeTable, plotTable, label="eulerCromer")

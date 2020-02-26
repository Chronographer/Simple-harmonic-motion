import matplotlib.pyplot as plt


def euler(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, plotType):
    currentTheta = initialTheta
    currentOmega = initialOmega
    currentTime = initialTime

    initialEnergy = (0.5) * mass * pendulumLength**2 * (currentOmega**2 + (gravity / pendulumLength) * currentTheta**2)
    currentEnergy = initialEnergy

    xAxisList = []
    yAxisList = []

    while currentTime <= maxTime:
        currentAlpha = (gravity * currentTheta) / pendulumLength
        currentTheta = currentTheta + currentOmega * timeStep
        currentOmega = currentOmega - currentAlpha * timeStep
        currentEnergy = 0.5 * mass * pendulumLength**2 * currentOmega**2 + 0.5 * mass * gravity * pendulumLength * currentTheta**2
        currentTime = currentTime + timeStep

        if plotType == "energy":
            xAxisList.append(currentEnergy)
            yAxisList.append(currentTime)
        elif plotType == "angle":
            xAxisList.append(currentTheta)
            yAxisList.append(currentTime)
        elif plotType == "velocity":
            xAxisList.append(currentOmega)
            yAxisList.append(currentTime)
        elif plotType == "acceleration":
            xAxisList.append(currentAlpha)
            yAxisList.append(currentTime)
        elif plotType == "phaseSpace":
            xAxisList.append(currentOmega)
            yAxisList.append(currentTheta)
        else:
            exit("Error: '" + str(plotType) + "' is not a valid plot type!")

    plt.plot(yAxisList, xAxisList, label="Euler: " + plotType)

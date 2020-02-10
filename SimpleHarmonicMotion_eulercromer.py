import matplotlib.pyplot as plt


def eulercromer(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass):
    currentTheta = initialTheta
    currentOmega = initialOmega
    currentTime = initialTime

    thetaTable = []
    omegaTable = []
    alphaTable = []
    timeTable = []
    energyTable = []

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

    plt.plot(timeTable, energyTable, label="eulerCromer")

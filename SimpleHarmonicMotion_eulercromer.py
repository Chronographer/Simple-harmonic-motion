import matplotlib.pyplot as plt


def eulercromer(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime):
    currentTheta = initialTheta
    currentOmega = initialOmega
    currentTime = initialTime

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

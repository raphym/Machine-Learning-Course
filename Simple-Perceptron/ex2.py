"""
Raphael Mazouz
This is a program that simulates the action of an artificial neuron perceptron
"""

# IMPORT
from pylab import plt
import warnings


# Globals variables
speedLearning = 8  # its is the speed of the learning
t = 0.5  # for the function threshold
count = 0  # counter for the loop until there is no error
prevWeightVector = [0.7, 0.4, 0.7]  # preview vector of weight for the loop until there is no error


def removewarning(message, category, filename, lineno, file=None, line=None):
    """
    for the warning
    """
warnings.showwarning = removewarning


def calculate(axeofx, weightvect):
    """ function that calculate the position x and y of the line for the graph
    """
    res = [1, 1]
    res[0] = - ((weightvect[0]*1) + (weightvect[1]*axeofx[0]) + t)/(weightvect[2])
    res[1] = - ((weightvect[0]*1) + (weightvect[1]*axeofx[1]) + t)/(weightvect[2])
    return res


def draw(weightvect):
    """ function that draw the graph so the line that separate the points from the special point
    """
    axeofx = [-1, 2]
    axeofy = calculate(axeofx, weightvect)

    plt.xlim(-1, 2)
    plt.ylim(-1, 2)
    plt.plot(axeofx, axeofy, color="black")
    pointx = [0, 0, 1]
    pointy = [0, 1, 0]
    plt.scatter(pointx, pointy, color="blue")
    plt.scatter(1, 1, color="red")
    plt.ylabel("x2")
    plt.xlabel("x1")
    title1 = "Weight Vector : " + str(weightvect)
    plt.title(title1, backgroundcolor ="green",color="black")
    plt.pause(0.2)
    plt.cla()

    return 0


def threshold(vectx, weightvect):
    """ function which multiplies each input by a weight, sum and return the result.
        return 1 if the result is > t
        otherwise return 0
    """
    thesum = p = 0
    while p < len(vectx):
        thesum = thesum + vectx[p] * weightvect[p]
        p += 1

    if thesum > t:
        return 1
    else:
        return 0


def learningProcess(vectx, z, weightvect):
    """ function that modify the values of weigh to learn about the input.
        if the result of the 'threshold' is equal to the desired result 'z' so do nothing
        and if the result of the 'threshold' is different from the desired result 'z' so modify the
        values of the vector weight
    """

    n = threshold(vectx, weightvect)
    er = z-n  # error
    d = speedLearning*er

    p = 0
    while p < len(vectx):
        weightvect[p] += d * vectx[p]
        p += 1

    global count
    if prevWeightVector[0] == weightvect[0] and prevWeightVector[1] == weightvect[1] \
            and prevWeightVector[2] == weightvect[2]:
        count += 1
    else:
        count = 0

    prevWeightVector[0] = weightvect[0]
    prevWeightVector[1] = weightvect[1]
    prevWeightVector[2] = weightvect[2]

    if weightvect[2] != 0:
        draw(weightvect)
    return


if __name__ == "__main__":
    weightVector = [0.7, 0.4, 0.7]
    train_vector = [[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    result = [1, 1, 1, 0]

    while count <= 3:
        i = 0
        while i < len(train_vector):
            learningProcess(train_vector[i], result[i], weightVector)
            i += 1


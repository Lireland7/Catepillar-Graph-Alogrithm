import math
import this

caterpillar = []
with open('inputfile') as f:
    contents = f.read()
    print(contents)
    ls = list(contents.split(", "))
    print(ls)
    for i in range(0, len(ls)):
        caterpillar.append(int(ls[i]))
hasChecked = [False for i in caterpillar]


def greedyCaterpillarAlgorithm():
    findLinearEmbedding()


def findLinearEmbedding():
    bandwidth = bandwidthAlgorithm(findMax())
    print("the bandwidth is:")
    print(math.floor(bandwidth + 1))
    linearEmbedding = [0 for i in range(len(caterpillar))]
    for i in range(len(caterpillar)):
        remainingSpace = bandwidth - linearEmbedding[i]
        if caterpillar[i] > remainingSpace:
            caterpillar[i] -= remainingSpace
            linearEmbedding[i] = bandwidth
            linearEmbedding[i + 1] = caterpillar[i]
            caterpillar[i] = 0
        else:
            linearEmbedding[i] += caterpillar[i]
            caterpillar[i] = 0
    return linearEmbedding


def bandwidthAlgorithm(maxVertex):
    bandwidth = findBandwidth(maxVertex)
    possibleProblemNodes = findNextMaxes(bandwidth)
    checking = True
    i = 0
    while checking:
        if len(possibleProblemNodes) == 0:
            checking = False
        elif findBandwidth(possibleProblemNodes[i]) > bandwidth:
            bandwidth = bandwidthAlgorithm(possibleProblemNodes[i])
            checking = False
        i = i + 1
        if i == len(possibleProblemNodes):
            checking = False
    return bandwidth


def findBandwidth(startingNode):
    leftCheckCount = 0
    rightCheckCount = 0
    spineCount = 1
    leafCount = caterpillar[startingNode]
    calculating = True
    bandwidthReturn = (leafCount / (spineCount + 1)) + 1

    while calculating:
        bandwidth = (leafCount / (spineCount + 1)) + 1
        leftCheck = startingNode - leftCheckCount
        rightCheck = startingNode + rightCheckCount

        if leftCheck < 0 and rightCheck == len(caterpillar):
            return (leafCount / (spineCount + 1)) + 1
        elif leftCheck < 0:
            if caterpillar[rightCheck] > bandwidth:
                hasChecked[rightCheck] = True
                rightCheckCount = rightCheckCount + 1
                spineCount = spineCount + 1
                leafCount += caterpillar[rightCheck]
            else:
                return (leafCount / (spineCount + 1)) + 1
        elif rightCheck == len(caterpillar):
            if caterpillar[leftCheck] > bandwidth:
                hasChecked[leftCheck] = True
                leftCheckCount += 1
                spineCount += 1
                leafCount += caterpillar[leftCheck]
            else:
                return (leafCount / (spineCount + 1)) + 1
        else:
            if caterpillar[rightCheck] > caterpillar[leftCheck and caterpillar[rightCheck] > bandwidth]:
                hasChecked[rightCheck] = True
                rightCheckCount += 1
                spineCount += 1
                leafCount += caterpillar[rightCheck]
            elif caterpillar[rightCheck] < caterpillar[leftCheck and caterpillar[leftCheck] > bandwidth]:
                hasChecked[leftCheck] = True
                leftCheckCount += 1
                spineCount += 1
                leafCount += caterpillar[leftCheck]
            else:
                return (leafCount / (spineCount + 1)) + 1
    return bandwidthReturn


def findMax():
    maxDegreeVertex = 0
    maxDegree = 0
    for i in range(len(caterpillar)):
        if caterpillar[i] > maxDegree:
            maxDegreeVertex = i
            maxDegree = caterpillar[i]
    return maxDegreeVertex


def findNextMaxes(bandwidth):
    maximums = []
    for i in range(len(caterpillar)):
        if caterpillar[i] > bandwidth and hasChecked[i] == False:
            maximums.append(i)
    return maximums


greedyCaterpillarAlgorithm()

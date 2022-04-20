import math
import this

from pathfinder import Graph

# Read graph in from file
caterpillar = []
with open('inputfile') as f:
    contents = f.read()
    print(contents)
    ls = list(contents.split(", "))
    print(ls)
    # Build tuple to represent caterpillar
    for i in range(0, len(ls)):
        caterpillar.append(int(ls[i]))
hasChecked = [False for i in caterpillar]


def greedyCaterpillarAlgorithm():
    print(findLinearEmbedding())


# Helper function to find the linear embedding of caterpillar graph
# Print the bandwidth
# Print the embedding
def findLinearEmbedding():
    # Get the bandwidth of the caterpillar
    bandwidth = math.ceil(bandwidthAlgorithm(findMax()))
    print("the bandwidth is:")
    print(math.ceil(bandwidth + 1))

    # Tracks the number of vertices to the left of each spine vertex
    linearEmbedding = [0 for i in range(len(caterpillar) + 1)]

    # Loop through each spine vertex
    for i in range(len(caterpillar)):

        # Track the remaining space between spine vertices
        remainingSpace = bandwidth - linearEmbedding[i]

        # If there is no remaining space to the left of the spine vertex
        # Put remaining vertices to the right of the spine
        if caterpillar[i] > remainingSpace:
            caterpillar[i] -= remainingSpace
            linearEmbedding[i] = bandwidth
            linearEmbedding[i + 1] = caterpillar[i]
            caterpillar[i] = 0

        # Else put all the vertices in the space
        else:
            linearEmbedding[i] += caterpillar[i]
            caterpillar[i] = 0

    return linearEmbedding


# Helper function to find the bandwidth of the graph
# Parameters:
#   maxVertex -> the number vertices attached to the max spine vertex or problem vertex
def bandwidthAlgorithm(maxVertex):
    # Find the bandwidth of a subgraph centered on the max spine vertex
    bandwidth = findBandwidth(maxVertex)

    # Find other problem vertices in the graph
    possibleProblemNodes = findNextMaxes(bandwidth)

    checking = True
    i = 0

    # Checking through list of problem vertices
    while checking:

        # If there are no problem vertices then done
        if len(possibleProblemNodes) == 0:
            checking = False

        # If the bandwidth of the next problem vertex is greater than
        # the bandwidth of the current vertex
        # run algorithm on that vertex now
        elif findBandwidth(possibleProblemNodes[i]) > bandwidth:
            bandwidth = bandwidthAlgorithm(possibleProblemNodes[i])
            checking = False
        i = i + 1

        # If all problem vertices have been checked then done
        if i == len(possibleProblemNodes):
            checking = False

    return bandwidth


# Find the bandwidth of a subgraph
# Parameters:
#   startingNode -> The problem vertex to start at
def findBandwidth(startingNode):
    # Number of vertices checked to the left and right of the starting vertex
    leftCheckCount = 0
    rightCheckCount = 0

    # Number of spine vertices in subgraph
    spineCount = 1
    # Number of leaf vertices in subgraph
    leafCount = caterpillar[startingNode]
    calculating = True

    # Formula to calculate bandwidth of subgraph
    bandwidthReturn = (leafCount / (spineCount + 1)) + 1

    # Loop while checking vertices to the left and right of the subgraph
    while calculating:
        bandwidth = (leafCount / (spineCount + 1)) + 1

        # Which node to check on the left and right
        leftCheck = startingNode - leftCheckCount
        rightCheck = startingNode + rightCheckCount

        # If there are no more vertices to check then return bandwidth
        if leftCheck < 0 and rightCheck == len(caterpillar):
            return (leafCount / (spineCount + 1)) + 1

        # If there are no more vertices to check on the left
        elif leftCheck < 0:
            # If the vertex on the right has more leaf vertices than the bandwidth
            # Mark spine vertex as checked
            # Increment counts
            if caterpillar[rightCheck] > bandwidth:
                hasChecked[rightCheck] = True
                rightCheckCount = rightCheckCount + 1
                spineCount = spineCount + 1
                leafCount += caterpillar[rightCheck]

            # Else done
            # Return bandwidth
            else:
                return (leafCount / (spineCount + 1)) + 1

        # If all vertices on the right have been checked
        elif rightCheck == len(caterpillar):

            # If the vertex on the left has more leaf vertices than the bandwidth
            # Mark spine vertex as checked
            # Increment counts
            if caterpillar[leftCheck] > bandwidth:
                hasChecked[leftCheck] = True
                leftCheckCount += 1
                spineCount += 1
                leafCount += caterpillar[leftCheck]

            # Else done
            # Return Bandwidth
            else:
                return (leafCount / (spineCount + 1)) + 1

        # Else have to check both
        else:
            # If the right vertex has more leaves than the left
            # And it has more leaves than the bandwidth
            # Increment counts
            if caterpillar[rightCheck] > caterpillar[leftCheck] and caterpillar[rightCheck] > bandwidth:
                hasChecked[rightCheck] = True
                rightCheckCount += 1
                spineCount += 1
                leafCount += caterpillar[rightCheck]

            # If the left has more leaves than the right
            # And it has more leaves than the bandwidth
            # Increment counts
            elif caterpillar[rightCheck] < caterpillar[leftCheck] and caterpillar[leftCheck] > bandwidth:
                hasChecked[leftCheck] = True
                leftCheckCount += 1
                spineCount += 1
                leafCount += caterpillar[leftCheck]

            # Else done
            # Return bandwidth
            else:
                return (leafCount / (spineCount + 1)) + 1
    return bandwidthReturn


# Find the max Vertex of the graph
def findMax():
    maxDegreeVertex = 0
    maxDegree = 0
    # Simple loop to check
    for i in range(len(caterpillar)):
        if caterpillar[i] > maxDegree:
            maxDegreeVertex = i
            maxDegree = caterpillar[i]
    return maxDegreeVertex


# Find all problem vertices
# Parameters:
#   bandwidth -> current bandwidth estimate
def findNextMaxes(bandwidth):
    maximums = []
    # SImple loop to check
    for i in range(len(caterpillar)):
        if caterpillar[i] > bandwidth and hasChecked[i] == False:
            maximums.append(i)
    return maximums






greedyCaterpillarAlgorithm()

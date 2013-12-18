# http://projecteuler.net/problem=68
from collections import deque

def solve(allNums, tempSolution):
    """ Backtrack to find all solutions. """
    if len(tempSolution) == 10:
        yield getSolutionSet(tempSolution)

    for n in allNums:
        if reject(n, tempSolution):
            continue

        tempSolution.append(n)
        for solution in solve(allNums, tempSolution):
            yield solution
        tempSolution.pop()


def reject(n, tempSolution):
    """
    Checks whether the current number should be rejected.

    A number should be rejected if it has already been used in the current
    temporary solution.  It should also be rejected if the number, when placed,
    does not give a valid sum.  See # http://projecteuler.net/problem=68 for details.
    """
    if n in tempSolution:
        return True

    numPlaced = len(tempSolution)
    if numPlaced == 4:
        return sum(tempSolution[:3]) != n + tempSolution[2] + tempSolution[3]
    elif numPlaced == 6:
        return sum(tempSolution[:3]) != n + tempSolution[4] + tempSolution[5]
    elif numPlaced == 8:
        return sum(tempSolution[:3]) != n + tempSolution[6] + tempSolution[7]
    elif numPlaced == 9:
        return sum(tempSolution[:3]) != n + tempSolution[1] + tempSolution[8]
    else:
        return False

def getSolutionSet(solution):
    """ 
    Given a solution, rotate it so that the smallest outer node is first. The 
    remaining numbers follow clockwise. See problem statement for details.
    """
    fullSolution = solution[:3]
    fullSolution.extend([solution[3], solution[2], solution[4]])
    fullSolution.extend([solution[5], solution[4], solution[6]])
    fullSolution.extend([solution[7], solution[6], solution[8]])
    fullSolution.extend([solution[9], solution[8], solution[1]])
    solutionDeque = deque(fullSolution)

    smallest = min([solution[0], solution[3], solution[5], solution[7], solution[9]])
    if smallest == solution[3]:
        solutionDeque.rotate(-3)
    elif smallest == solution[5]:
        solutionDeque.rotate(-6)
    elif smallest == solution[7]:
        solutionDeque.rotate(-9)
    elif smallest == solution[9]:
        solutionDeque.rotate(-12)

    return ''.join(map(str, solutionDeque))


uniqueSolutions = set(solve(range(1, 11), []))
print max(solution for solution in uniqueSolutions if len(str(solution)) == 16)

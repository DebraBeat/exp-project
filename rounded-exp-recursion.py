import sys
from sympy import *

realStartNumber = float(sys.argv[1])
imaginaryStartNumber = float(sys.argv[2])
rangeLength = int(sys.argv[3])

sequenceList = [[] for _ in range(rangeLength)]
sequenceList[0].append(realStartNumber)
sequenceList[0].append(imaginaryStartNumber)
loopList = range(rangeLength)

print "0: " + str(sequenceList[0])

for j in loopList[1:]:
    nextMember = exp( (I * sequenceList[j-1][0]) - sequenceList[j-1][1])

    sequenceList[j].append(round(re(nextMember),3))
    sequenceList[j].append(round(im(nextMember),3))

    print str(j) + ": " + str(sequenceList[j])
    if sequenceList[j][0] == (sequenceList[j-1][0] + 0.001 or sequenceList[j-1][0] - 0.001):
        if sequenceList[j][1] == (sequenceList[j-1][1] + 0.001 or sequenceList[j-1][1] - 0.001):
            break
            

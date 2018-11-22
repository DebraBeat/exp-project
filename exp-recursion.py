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

    #unrounded version
    sequenceList[j].append(re(nextMember))
    sequenceList[j].append(im(nextMember))


    print str(j) + ": " + str(sequenceList[j])

print "Length of mysterious number: " + str(sqrt( (sequenceList[rangeLength-1][0] * sequenceList[rangeLength-1][0]) + (sequenceList[rangeLength-1][1]* sequenceList[rangeLength-1][1]) ))

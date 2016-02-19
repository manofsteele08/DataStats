__author__ = 'chris'

import plotly
import math
import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')

filename = ""
print "*** WELCOME TO MY AWESOME ANALYTICAL STATISTICS CALCULATOR! ***"
user = raw_input("Are you ready to begin? Y/N: ")
if user == "Y" or user == 'y':
    filename = raw_input("Please type the name of the .csv file you would like to use (include .csv): ")
else:
    print "Ok see ya!"
    exit()

file = open(filename, 'r')

mainData = []
for line in file:
    tempTupe = line.split(',')
    tempTupe = map(lambda s: s.strip(), tempTupe)
    mainData.append(tempTupe)
labels = mainData.pop(0)
calcs = ['Labels', 'Sum', 'Maximum', 'Minimum', 'Mean', 'Median', 'Mode', 'Range', 'Count', 'Standard Deviation',
         'Standard Error', 'Sample Variance', 'Kurtosis', 'Skewness']


def standDev(a, b):
    total_sum = 0
    for i in range(len(a)):
        total_sum += ((float(a[i]) - b) ** 2)

    myRoot = total_sum / len(a)
    return math.sqrt(myRoot)


def standErr(a, b):
    total_sum = 0
    for i in range(len(a)):
        total_sum += ((float(a[i]) - b) ** 2)

    myRoot = total_sum / len(a)
    SD = math.sqrt(myRoot)
    return SD / math.sqrt(len(a))


def sampVariance(a, b):
    total_sum = 0
    for i in range(len(a)):
        total_sum += ((float(a[i]) - b) ** 2)
    return total_sum / len(a)


def kurtosis(a, b):
    temp = []
    s = standDev(a, b)
    n = len(a)
    for i in xrange(len(a)):
        temp.append(((float(a[i]) - float(b)) ** 4) / float(n))

    k = sum(temp) / (s ** 4)
    return k - 3


def skew(a, b):
    temp = []
    s = standDev(a, b)
    n = len(a)
    for i in xrange(len(a)):
        temp.append(((float(a[i]) - float(b)) / float(s)) ** 3)
    val = ((float(n)) / ((float(n) - 1) * (float(n) - 2)))
    result = val * sum(temp)
    return result


def median(a):
    sorts = sorted(a)
    length = len(sorts)
    if not length % 2:
        return float(float(sorts[length / 2]) + float(sorts[length / 2 - 1])) / 2.0
    return float(sorts[length / 2])


def mode(a):
    return float(max(set(a), key=a.count))


dataTupe = []


def processData(a):
    for i in xrange(len(labels)):
        tempList = []
        for e in mainData:
            tempList.append(e[i])

        mySum = sum(float(e[i]) for e in mainData)
        myMax = max(float(e[i]) for e in mainData)
        myMin = min(float(e[i]) for e in mainData)
        myMean = sum(float(e[i]) for e in mainData) / len(a)
        myMedian = median(tempList)
        myMode = mode(tempList)
        myRange = max(float(e[i]) for e in mainData) - min(float(e[i]) for e in mainData)
        myCount = len(a)
        myStandDev = standDev(tempList, myMean)
        myStandErr = standErr(tempList, myMean)
        mySampleVar = sampVariance(tempList, myMean)
        myKurtosis = kurtosis(tempList, myMean)
        mySkew = skew(tempList, myMean)
        dataTupe.append((mySum, myMax, myMin, myMean, myMedian, myMode, myRange, myCount, myStandDev, myStandErr,
                         mySampleVar, myKurtosis, mySkew))
    return dataTupe


def printData():
    myFile = open("Statistics.txt", 'w')
    dataTupe = processData(mainData)
    for name in calcs:
        myFile.write('%16s' % name)
    myFile.write('\n')
    for i in xrange(len(labels)):
        myFile.write('%16s' % (labels[i]), )
        for j in xrange(len(dataTupe[i])):
            myFile.write('%16.3f' % (dataTupe[i][j]), )
        myFile.write('\n')


printData()
oilTupe = []
homeTupe = []
for i in xrange(len(mainData)):
    oilTupe.append(mainData[i][2])
    homeTupe.append(mainData[i][5])

# Create a trace
trace = go.Scatter(
    x=homeTupe,
    y=oilTupe,
    mode='markers'
)

data = [trace]
plot_url = py.plot(data, filename='Scatter-Plot')

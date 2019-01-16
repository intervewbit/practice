def hit(freqMap, remainingQueriesMap, queryMap, textList, index):
    if index >= len(textList):
        return False
    remainingQueriesMap.pop(textList[index], 0)
    if textList[index] in queryMap:
        prevFreq = freqMap.pop(textList[index], 0)
        freqMap[textList[index]] = prevFreq + 1
    return len(remainingQueriesMap) == 0


def remove(freqMap, remainingQueriesMap, queryMap, textList, index):
    if index >= len(textList):
        return False
    if textList[index] in queryMap:
        prevFreq = freqMap.pop(textList[index], 0)
        if prevFreq > 1:
            freqMap[textList[index]] = prevFreq - 1
        else:
            remainingQueriesMap[textList[index]] = True
    return len(remainingQueriesMap) == 0


def updateMin(end, start, minDistance):
    distance = end - start + 1
    return min(minDistance, distance)


def cover(textList, queryList):
    if len(textList) <= 0:
        return -1
    freqMap = {}
    start, end = 0, 1
    remainingQueriesMap = {x: True for x in queryList}
    queryMap = {x: True for x in queryList}
    minDistance = len(textList) + 1
    #  skip the first letters which do not match
    while textList[start] not in remainingQueriesMap and start < len(textList):
        start = start + 1
    end = start
    if hit(freqMap, remainingQueriesMap, queryMap, textList, start):
        return 1

    while start < len(textList) and end < len(textList):
        # increase end if there are queries remaining else incr start
        if len(remainingQueriesMap) > 0:
            end = end + 1
            if hit(freqMap, remainingQueriesMap, queryMap, textList, end):
                minDistance = updateMin(end, start, minDistance)
        else:
            start = start + 1
            if remove(freqMap, remainingQueriesMap, queryMap, textList, start - 1):
                minDistance = updateMin(end, start, minDistance)
    return minDistance


#textList = ["apple", "coke", "ban", "ban", "ban", "orange", "apple", "coke"]
textList = []
queryList = ["apple", "orange", "coke", "du"]
minDistance = cover(textList, queryList)
print("Minimum distance ", minDistance)

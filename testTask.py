import time


def getMinNumber(data):
    print(f'The minimal number in the file - {min(data)}')


def getMaxNumber(data):
    print(f'The maximal number in the file - {max(data)}')


def getAverage(data):
    print(f'The Average in the file - {sum(data) // len(data)}')


def getMedian(data):
    index = len(data) // 2
    print(f'The Median in the file - {sorted(data)[index]}')


def getLargestPositiveSequence(data):
    largeSeq = []
    largeSeqLen = 0
    tempSeq = []
    tempSeqLen = 0

    for i in data:
        if tempSeq == [] or i > tempSeq[-1]:
            tempSeq.append(i)
            tempSeqLen += 1
        else:
            if tempSeqLen > largeSeqLen:
                largeSeq = tempSeq
                largeSeqLen = tempSeqLen
            tempSeq = [i]
            tempSeqLen = 1

    if tempSeqLen > largeSeqLen:
        largeSeq = tempSeq

    print(f'The Largest positive Sequence {largeSeq}')


def getLargestNegativeSequence(data):
    largeSeq = []
    largeSeqLen = 0
    tempSeq = []
    tempSeqLen = 0

    for i in data:
        if tempSeq == [] or i < tempSeq[-1]:
            tempSeq.append(i)
            tempSeqLen += 1
        else:
            if tempSeqLen > largeSeqLen:
                largeSeq = tempSeq
                largeSeqLen = tempSeqLen
            tempSeq = [i]
            tempSeqLen = 1

    if tempSeqLen > largeSeqLen:
        largeSeq = tempSeq

    print(f'The Largest negative Sequence {largeSeq}')


def start():
    start_time = time.time()
    with open('10m.txt', 'r') as f:
        data = [int(x) for x in f.readlines()]  # Reformat type of objects in file str - int
    getMaxNumber(data)  # Get maximum number by basic function in Python max()
    getMinNumber(data)  # Get minimum number by basic function in Python min()
    getAverage(data)  # Get Average numbers by math formula and basic functions in Python len() and sum()
    getMedian(data)  # Get Median numbers by basic function in Python sorted which returns sorted list and cut list
    # of numbers by 2 side
    print(f'Time taken to run basic tasks: {time.time() - start_time} seconds')
    getLargestPositiveSequence(data)  # Get the largest positive sequence by cycle for and some list for save and
    # check results
    getLargestNegativeSequence(data)  # Get the largest negative sequence by cycle for and some list for save and
    # check results
    print(f'Time taken to run basic and additional tasks: {time.time() - start_time} seconds')


if __name__ == '__main__':
    start()

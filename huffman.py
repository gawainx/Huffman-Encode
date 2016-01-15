# coding=utf-8
from heapq import heapify, heappush, heappop
from itertools import count
from Tree import *

from dice import *


def calcWeight(ll):
    '''
    This func set to calculate the weight of each code
    :param ll: ll is the source of
    :return:
    '''
    weightRes = []
    # two lines below is to get all the unique code from source
    tmplist = list(set(ll))
    length = float(len(ll))
    for i in tmplist:
        num, count = i, ll.count(i)
        lweight = count / length
        weightRes.append(lweight)
    return tmplist, weightRes


def createHuffTree(seq, frq):
    num = count()
    trees = list(zip(frq, num, seq))
    heapify(trees)
    while len(trees) > 1:
        # two lines below aim to find the most min node of tree
        fa, _, a = heappop(trees)
        fb, _, b = heappop(trees)
        n = next(num)
        heappush(trees, (fa + fb, n, [a, b]))
    # print trees
    return trees[0][-1]

def avelength(dict,freq,seq):
    """
    to calculate the averaage length of huffman code
    :param dict:
    :return:
    """
    length=0.0
    for i in range(len(seq)):
        length+=len(dict[seq[i]])*freq[i]
    return length


def HuffEncode(srcLst, huffDict):
    """

    :param srcStr:
    :param huffDict:
    :return:
    """
    dest = ''
    for i in srcLst:
        dest += huffDict[i]
    return dest


def HuffDecode(srcStr, huffDict):
    # Reverse the key and value of HuffDict.Let value be key and key be value
    decodeDict = {value: key for key, value in huffDict.items()}
    tmpStr = ''
    result = []
    for i in srcStr:
        tmpStr += i
        if tmpStr in decodeDict.keys():
            result.append(decodeDict[tmpStr])
            tmpStr = ''
        else:
            pass
    return result


def test():
    '''
    test func
    :return: none
    '''


test()

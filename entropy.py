# this file aim to calc entropy
from math import log


def calcEnt(freq):
    """

    :param freq: freqency list
    :return: the entropy of the given freqency list
    """
    entropy = 0.0
    for p in freq:
        entropy += p * log(p, 2)
    return -entropy

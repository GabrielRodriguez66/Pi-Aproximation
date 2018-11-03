# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 16:57:41 2018

@author: Gabriel
"""

import numpy as np


def PiSeries1(error):
    relativeError = error+1
    termsProduct = 1
    term = 0
    i1 = 1
    i2 = 1
    estimateVector = []
    errorVector = []
    
    while relativeError > error:
        term += 1
        if term % 2 != 0:
            termsProduct *= (i1 * 2) / (2 * i1 - 1)
            i1 += 1
        else:
            termsProduct *= (i2 * 2) / (2 * i2 + 1)
            i2 += 1

        estimate = 2 * termsProduct
        relativeError = 100 * abs((estimate - np.pi)/np.pi)
        
        estimateVector.append(estimate)
        errorVector.append(relativeError)
        
    return term, estimate, relativeError, estimateVector, errorVector


def PiSeries2(error):
    relativeError = error+1
    termsSum = 0
    i = 0
    estimateVector = []
    errorVector = []
    
    while relativeError > error:
        i += 1
        termsSum += ((-1) ** (i + 1) / (2 * i - 1))
        estimate = 4 * termsSum
        relativeError = 100 * abs((estimate - np.pi)/np.pi)

        estimateVector.append(estimate)
        errorVector.append(relativeError)

    return i, estimate, relativeError, estimateVector, errorVector


def PiSeries3(error):
    relativeError = error+1
    termsSum = 0
    term = 0
    i = 1
    estimateVector = []
    errorVector = []
    
    while relativeError > error:
        term += 1

        oddNum = (2 * i + 1)
        denominator = oddNum * (oddNum - 2)
        termsSum += (1 / denominator)

        estimate = 8 * termsSum
        relativeError = 100 * abs((estimate - np.pi)/np.pi)
        
        estimateVector.append(estimate)
        errorVector.append(relativeError)

        i += 2

    return term, estimate, relativeError, estimateVector, errorVector
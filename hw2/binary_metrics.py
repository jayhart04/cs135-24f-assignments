'''
calc_binary_metrics

Provides implementation of common metrics for assessing a binary classifier's
hard decisions against true binary labels, including:
* accuracy
* true positive rate and true negative rate (TPR and TNR)
* positive predictive value and negative predictive value (PPV and NPV)
'''

import numpy as np

def calc_TP_TN_FP_FN(ytrue_N, yhat_N):
    ''' Count the four possible states of true and predicted binary values.
    
    Args
    ----
    ytrue_N : 1D array, shape (n_examples,) = (N,)
        All values must be either 0 or 1. Will be cast to int dtype.
        Each entry represents the binary 'true' label of one example
        One entry per example in current dataset
    yhat_N : 1D array, shape (n_examples,) = (N,)
        All values must be either 0 or 1. Will be cast to int dtype.
        Each entry represents a predicted label for one example
        One entry per example in current dataset.
        Needs to be same size as ytrue_N.

    Returns
    -------
    TP : int
        Number of true positives
    TN : int
        Number of true negatives
    FP : int
        Number of false positives
    FN : int
        Number of false negatives

    Examples
    --------
    >>> N = 8
    >>> ytrue_N = np.asarray([0., 0., 0., 0., 1., 1., 1., 1.])
    >>> yhat_N  = np.asarray([0., 0., 1., 0., 1., 1., 0., 0.])
    >>> TP, TN, FP, FN = calc_TP_TN_FP_FN(ytrue_N, yhat_N)
    >>> TP
    2
    >>> TN
    3
    >>> FP
    1
    >>> FN
    2
    >>> np.allclose(TP + TN + FP + FN, N)
    True
    '''
    # Cast input to integer just to be sure we're getting what's expected
    ytrue_N = np.asarray(ytrue_N, dtype=np.int32)
    yhat_N = np.asarray(yhat_N, dtype=np.int32)
    
    # TODO fix by calculating the number of true pos, true neg, etc.
    assert ytrue_N.shape == yhat_N.shape
    TP  = int(np.sum(ytrue_N & yhat_N))
    TN = int(np.sum((1-ytrue_N) & (1-yhat_N)))
    FP = int(np.sum((1-ytrue_N) & yhat_N))
    FN = int(np.sum(ytrue_N & (1-yhat_N)))
    return TP, TN, FP, FN


def calc_ACC(ytrue_N, yhat_N):
    ''' Compute the accuracy of provided predicted binary values.
    
    Args
    ----
    ytrue_N : 1D array of floats, shape (n_examples,) = (N,)
        All values must be either 0.0 or 1.0.
        Each entry represents the binary 'true' label of one example
        One entry per example in current dataset
    yhat_N : 1D array of floats, shape (n_examples,) = (N,)
        All values must be either 0.0 or 1.0.
        Each entry represents a predicted label for one example
        One entry per example in current dataset.
        Needs to be same size as ytrue_N.

    Returns
    -------
    acc : float
        Accuracy = ratio of number correct over total number of examples

    Examples
    --------
    >>> N = 8
    >>> ytrue_N = np.asarray([0., 0., 0., 0., 1., 1., 1., 1.])
    >>> yhat_N  = np.asarray([0., 0., 1., 0., 1., 1., 0., 0.])
    >>> acc = calc_ACC(ytrue_N, yhat_N)
    >>> print("%.3f" % acc)
    0.625
    '''
    TP, TN, FP, FN = calc_TP_TN_FP_FN(ytrue_N, yhat_N)
    # You should *use* your calc_TP_TN_FP_FN function from above
    # Hint: make sure denominator will never be exactly zero
    # by adding a small value like 1e-10
    return (TP + TN)/(TP + TN + FP + FN + 1e-10)



def calc_TPR(ytrue_N, yhat_N):
    ''' Compute the true positive rate of provided predicted binary values.

    Also known as the recall.

    Args
    ----
    ytrue_N : 1D array of floats, shape (n_examples,) = (N,)
        All values must be either 0.0 or 1.0.
        Each entry represents the binary 'true' label of one example
        One entry per example in current dataset
    yhat_N : 1D array of floats, shape (n_examples,) = (N,)
        All values must be either 0.0 or 1.0.
        Each entry represents a predicted label for one example
        One entry per example in current dataset.
        Needs to be same size as ytrue_N.

    Returns
    -------
    tpr : float
        TPR = ratio of true positives over total labeled positive

    Examples
    --------
    >>> N = 8
    >>> ytrue_N = np.asarray([0., 0., 0., 0., 1., 1., 1., 1.])
    >>> yhat_N  = np.asarray([0., 0., 1., 0., 1., 1., 0., 0.])
    >>> tpr = calc_TPR(ytrue_N, yhat_N)
    >>> print("%.3f" % tpr)
    0.500

    # Verify what happens with empty input
    >>> empty_val = calc_TPR([], [])
    >>> print("%.3f" % empty_val)
    0.000
    '''
    
    # You should *use* your calc_TP_TN_FP_FN function from above
    # Hint: make sure denominator will never be exactly zero
    # by adding a small value like 1e-10
    TP, TN, FP, FN = calc_TP_TN_FP_FN(ytrue_N, yhat_N)
    return (TP/(TP + FN + 1e-10))


def calc_PPV(ytrue_N, yhat_N):
    ''' Compute positive predictive value of provided predicted binary values.

    Also known as the precision.
    
    Args
    ----
    ytrue_N : 1D array of floats, shape (n_examples,) = (N,)
        All values must be either 0.0 or 1.0.
        Each entry represents the binary 'true' label of one example
        One entry per example in current dataset
    yhat_N : 1D array of floats, shape (n_examples,) = (N,)
        All values must be either 0.0 or 1.0.
        Each entry represents a predicted label for one example
        One entry per example in current dataset.
        Needs to be same size as ytrue_N.

    Returns
    -------
    ppv : float
        PPV = ratio of true positives over total predicted positive.

    Examples
    --------
    >>> N = 8
    >>> ytrue_N = np.asarray([0., 0., 0., 0., 1., 1., 1., 1.])
    >>> yhat_N  = np.asarray([0., 0., 1., 0., 1., 1., 0., 0.])
    >>> ppv = calc_PPV(ytrue_N, yhat_N)
    >>> print("%.3f" % ppv)
    0.667

    # Verify what happens with empty input
    >>> empty_val = calc_PPV([], [])
    >>> print("%.3f" % empty_val)
    0.000
    '''
    # TODO compute PPV
    # You should *use* your calc_TP_TN_FP_FN function from above
    # Hint: make sure denominator will never be exactly zero
    # by adding a small value like 1e-10
    TP, TN, FP, FN = calc_TP_TN_FP_FN(ytrue_N, yhat_N)
    return (TP/(TP + FP + 1e-10))

# N = 8
# ytrue_N = np.asarray([0., 0., 0., 0., 1., 1., 1., 1.])
# yhat_N  = np.asarray([0., 0., 1., 0., 1., 1., 0., 0.])
# TP, TN, FP, FN = calc_TP_TN_FP_FN(ytrue_N, yhat_N)
# print(TP)
# print(TN)
# print(FP)
# print(FN)
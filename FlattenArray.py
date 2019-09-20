import itertools


def flatten(init_array):
    """
    Takes an array which may contain nested arrays and returns a
    flattened one dimensional array.
    :param init_array: the array to be flattened.
    :return: the flattened one dimensional array.
    """
    return list(itertools.chain.from_iterable(init_array))


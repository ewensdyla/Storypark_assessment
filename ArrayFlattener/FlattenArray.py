def flatten(init_array):
    """
    Takes an array which may contain nested arrays and returns a
    flattened one dimensional array.
    :param init_array: the array to be flattened.
    :return: the flattened one dimensional array.
    """
    # initialise the array to be returned
    flat_array = []

    # determine whether the value is an int or a list then either append or recurse
    for elem in init_array:
        if isinstance(elem, int):
            flat_array.append(elem)

        elif isinstance(elem, list):
            flat_array += flatten(elem)

    return flat_array


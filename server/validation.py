

def is_empty(value):
    """
    Check if the given value is empty.
    """
    return value is None or value == ""

def is_too_long(value, max_length=5000): # TODO: Handle chunking for larger texts
    """
    Check if the given value exceeds the maximum length.
    """
    return len(value) > max_length
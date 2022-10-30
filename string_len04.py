def main(s):
    """
    A string variable s is given. Return the "*" sign that is equal to the length of this variable.
    Args:
        s: string
    Returns:
        string
    """
    if len(s) > 0:
        return len(s) * "*"
    else:
        return None

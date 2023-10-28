
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    x = str(x)
    return x == x[::-1]
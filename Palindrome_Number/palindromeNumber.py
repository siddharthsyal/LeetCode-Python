def isPalindrome(x: int) -> bool:
    initialCopy: int = x
    reversedCopy: int = 0
    if x < 0:
        return False
    while x > 0:
        reversedCopy = (reversedCopy * 10) + (x%10)
        x //=10
    return reversedCopy == initialCopy

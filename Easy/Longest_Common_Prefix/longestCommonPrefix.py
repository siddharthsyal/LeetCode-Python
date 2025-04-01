from typing import List


def minLengthoFStrings(input: List[str]) -> int:
    minLength: int = len(input[0])
    for i in input:
        if minLength > len(i):
            minLength = len(i)
        if i == "":
            return 0
    return minLength

def longestCommonPrefix( strs: List[str]) -> str:
    longestPrefix: str = ""
    lengthOfInput = minLengthoFStrings(strs)
    print(lengthOfInput)
    if lengthOfInput == 0:
        return longestPrefix
    for i in range(lengthOfInput):
        if strs[0][i] == "":
            return longestPrefix
        testCharacter = strs[0][i]
        for j in range(len(strs)):
            if strs[j][i] != testCharacter:
                return longestPrefix
            if j == len(strs)-1:
                longestPrefix += testCharacter
    return longestPrefix
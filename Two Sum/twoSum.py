from email.charset import add_codec
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    tracker = {}
    returnData: List[int] = []
    for i in range(len(nums)):
        tracker[nums[i]] = i
        if (i == 0):
            continue
        else:
            result = tracker.get(target - nums[i])
            if result != None:
                returnData.append(result)
                returnData.append(i)
                return returnData

    return returnData

from email.charset import add_codec
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    tracker = {}
    returnData: List[int] = []
    for i in range(len(nums)):
        if (i == 0):
            tracker[nums[i]] = i
            continue
        else:
            result = tracker.get(target - nums[i])
            if result != None:
                returnData.append(result)
                returnData.append(i)
                return returnData
            else:
                tracker[nums[i]] = i
    return returnData

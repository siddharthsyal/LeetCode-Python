from collections import deque

def isValid(input: str) -> bool:
    tracker = deque([])
    for i in range (len(input)):
        if input[i] == "{":
            tracker.append("}")
        elif input[i] == "[":
            tracker.append("]")
        elif input[i] == "(":
            tracker.append(")")
        else:
            try:
                buffer = tracker.pop()
                if buffer != input[i]:
                    tracker.append(buffer)
                    return False
            except IndexError:
                return False
    return len(tracker) == 0

print(isValid("([])"))
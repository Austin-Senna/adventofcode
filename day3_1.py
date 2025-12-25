inputs = []

while True:
    try:
        inputs.append(input())
    except:
        break
currSum = 0
for input in inputs:
    currMax = [0, 0]
    maxIndex = -1
    for i in range(len(input)):
        curr = int(input[i])
        
        if curr > currMax[0]:
            if i == len(input) - 1:
                currMax[1] = curr
            else:
                currMax[0] = curr
                maxIndex = i

    if currMax[1] == 0:
        for i in range(maxIndex+1, len(input)):
            curr = int(input[i])
            if curr > currMax[1]:
                currMax[1] = curr
    
    currSum += currMax[0] * 10 + currMax[1]
    # print(currSum)

print(currSum)
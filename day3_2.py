import heapq
def bestNodes(start, end, n, input, res, used):
    oriInput = input 
    input = input[start:end]
    heapq.heapify(input)
    
    while n > 0:
        
        val, index = heapq.heappop(input)
        print(n)
        print(val, index)
        if not used[index]:
            nextVal, nextIndex = input[0]
            used[index] = True
            n-=1
            print("Before", result)
            result[index] = -1 * val
            print("After", result)
            if val != nextVal:
                if index <= end + 1 - n:
                    bestNodes(index + 1, end, n, oriInput, res, used)
                    break
                else:
                    end = index
                    print(end)
            
    
        

inputs = []

while True:
    try:
        inputs.append(input())
    except:
        break

currSum = 0

for input in inputs:
    n = 12
    used = [False] * len(input)
    input = [(-1 * int(x), i) for i,x in enumerate(input)]
    result = [0] * len(input)
    bestNodes(0, len(input), n, input, result, used)
    text = ""
    
    for n in result:
        if n != 0:
            text += str(n)

    print(int(text))
    currSum += int(text)

print(currSum)


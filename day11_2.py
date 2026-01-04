from collections import deque

adjacencyLists = {}
while True:
    try:
        key, val = input().split(": ")
        valArr = list(val.split(" "))
        adjacencyLists[key] = valArr
    except:
        break

# print(adjacencyLists)
# pathLists = []
count = 0 

def dfs(curr, target, usedFFT, usedDAC):
    
    if curr == "fft":
        usedFFT = True
    elif curr == "dac":
        usedDAC = True

    if curr == target:
        if usedFFT and usedDAC:
            # pathLists.append(list(path))
            count += 1
        return 
    
    if curr not in adjacencyLists:
        return
    valArr = adjacencyLists[curr]
    

    for val in valArr:
        # path.append(val)
        # dfs(list(path), val, target, usedFFT, usedDAC)
        dfs(val, target, usedFFT, usedDAC)
        # path.pop()

# dfs(["svr"], "svr", "out", False, False)
dfs("svr", "out", False, False)
print(count)
# dfs(["fft"], "fft", "dac", False, False)
# dfs(["dac"], "dac", "fft", False, False)
# print(pathLists)
# print(len(pathLists))


    
        



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
pathLists = []

def dfs(path, curr, target):
    
    if curr == target:
        pathLists.append(list(path))
        return 
    
    valArr = adjacencyLists[curr]

    for val in valArr:
        path.append(val)
        dfs(list(path), val, target)
        path.pop()

dfs(["you"], "you", "out")
print(len(pathLists))
print(pathLists)
# count = 0
# for path in pathLists:
#     foundFFT = False
#     foundDAC = False
#     for x in path:
#         if x == "fft":
#             foundFFT = True
#         elif x == "dac":
#             foundDAC = True
    
#     if foundDAC and foundFFT:
#         count += 1

# print(count)


    
        



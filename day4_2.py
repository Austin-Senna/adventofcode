from collections import deque
inputs = deque([])
while True:
    try:
        inputs.append(deque(input()))
    except:
        break

for i in range(len(inputs)):
    inputs[i].appendleft(".")
    inputs[i].append(".")

inputs.appendleft(["."]*len(inputs[0]))
inputs.append(["."]*len(inputs[0]))

def check(grid, i, j):
    dirs = [-1,0,1]
    count = 0 
    for dir in dirs:
        for dir2 in dirs:
            if dir == 0 and dir2 == 0:
                continue
            if grid[i+dir][j+dir2] == "@":
                count+=1
    
    return True if count < 4 else False

count = 0 
while True:
    changes = 0
    for i in range(1, len(inputs)):
        for j in range(1, len(inputs[0])):
            if inputs[i][j] == "@":
                if check(inputs, i, j):
                    inputs[i][j] = "."
                    count+=1
                    changes+=1
    if changes == 0:
        break
print(count)
# for input in copyInputs:
#     print("".join(input))

inputs = []

while True:
    try:
        inputs.append(list(input()))
    except:
        break

splits = 0

for i in range(len(inputs)):
    for j in range(len(inputs[0])):
        if inputs[i][j] == "S":
           inputs[i+1][j] = "|"
        elif inputs[i][j] == "^":
            if inputs[i-1][j] == "|":
                splits += 1
                if j-1 >= 0:
                    inputs[i][j-1] = "|"
                    if i+1 <len(inputs):
                        inputs[i+1][j-1] = "|"
                if j+1 < len(inputs[0]):
                    inputs[i][j+1] = "|"
                    if i+1 < len(inputs):
                        inputs[i+1][j+1] = "|"
        elif inputs[i][j] == "|":
            if i+1 < len(inputs) and inputs[i+1][j] == ".":
                inputs[i+1][j] = "|"

print(splits)
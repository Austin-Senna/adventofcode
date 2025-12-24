inputs = []

while True:
    try:
        inputs.append(input().split(" "))
    except:
        break

for i in range(len(inputs)-1):
    inputs[i] = [int(x) for x in inputs[i] if x!= ""]
inputs[-1] = [x for x in inputs[-1] if x!= ""]

grandtot = 0 
for j in range(len(inputs[0])):
    operation = inputs[-1][j]
    cumsum = inputs[0][j]

    
    grandtot += cumsum

print(grandtot)
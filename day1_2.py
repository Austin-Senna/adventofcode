inputs = []
while True:
    try:
        inputs.append(input())
    except:
        break

count = 0 
curr = 50

for line in inputs:
    num = int(line[1:])
    # print(num)
    if line[0] == "R":
        while num > 0:
            curr += 1

            if curr == 0:
                count += 1
            
            if curr == 100:
                curr = 0 
                count += 1

            num -= 1
    if line[0] == "L":
        while num > 0:
            curr -= 1
            
            if curr == 0:
                count += 1
            if curr == -1:
                curr = 99

            num -= 1
    
print(count)

    
    

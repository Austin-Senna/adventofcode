maxNum = 0 

inputs = []

def check(n):
    s = str(n)
    if s[:len(s)//2] != s[len(s)//2:]:
        return False
    return True
    
inputs = input().split(",")
inputsChanged = []

for input in inputs:
    if len(input) == 0:
        continue
    lo, hi = map(int, input.split("-"))  
    inputsChanged.append((lo, hi))
    if hi > maxNum:
        maxNum = hi    

nums = [0] * (maxNum + 1)

for i in range(maxNum + 1):
    if len(str(i)) % 2 == 1:
        nums[i] = nums[i-1]
    nums[i] = nums[i-1] + 1 if check(i) else nums[i-1]
    if i % 1000 == 0:
        print(f"Processed up to {i}")

currSum = 0
for lo, hi in inputsChanged:
    currSum += nums[hi] - nums[lo-1]

print(currSum)
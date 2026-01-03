import bisect
ranges = []
ingredients = []

while True:
    try:
        curr = input()
        if len(curr) == 0:
            continue
        if "-" in curr:
            ranges.append(list((map(int, curr.split("-")))))
        else:
            ingredients.append(int(curr))
    except:
        break

ranges.sort(key = lambda x : x[1])
ingredients.sort()

rangesMerged = []

for currRange in ranges:
    lowestStart = currRange[0]
    end = currRange[1]

    if len(rangesMerged) == 0:
        rangesMerged.append((lowestStart, end))
        continue

    if rangesMerged[-1][1] >= lowestStart:
        lowestStart = min(rangesMerged[-1][1], lowestStart)

        while len(rangesMerged) >0 and rangesMerged[-1][1] >= lowestStart:
            prevStart, prevEnd = rangesMerged.pop()
            lowestStart = min(lowestStart, prevStart)
        
    rangesMerged.append((lowestStart, end))

count = 0 
for ingre in ingredients:
    index = bisect.bisect_right(rangesMerged, (ingre, 0))
    index -=1
    if index in range(len(rangesMerged)):
        curr = rangesMerged[index]
        if ingre >= curr[0] and ingre <= curr[1]:
            count += 1

# print(count)
total = 0 
for range in rangesMerged:
    total += range[1] - range[0] + 1
print(total)
# print(rangesMerged)
# print(ingredients)

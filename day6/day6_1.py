from day6_data import data

test = [3,4,3,1,2]

currFishes = [*test]
for i in range(18):
    newFishies = 0
    for f in range(len(currFishes)):
        if currFishes[f]:
            currFishes[f] -= 1
        else:
            currFishes[f] = 6
            newFishies += 1
    for n in range(newFishies):
        currFishes.append(8)

print(len(currFishes))

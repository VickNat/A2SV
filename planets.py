testCases = int(input())

for test in range(testCases):
  numOfPlanets, secondMachCost = list(map(int, input().split()))
  orbitDict = dict()
  cost = 0

  orbit = list(map(int, input().split()))

  for idx in range(numOfPlanets):
    if orbit[idx] in orbitDict.keys():
      orbitDict[orbit[idx]] += 1
    else:
      orbitDict[orbit[idx]] = 1
  
  for orbKey in orbitDict.keys():
    if orbitDict[orbKey] < secondMachCost:
      cost += orbitDict[orbKey]
    else:
      cost += secondMachCost
  
  print(cost)

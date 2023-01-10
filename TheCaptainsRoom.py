# Enter your code here. Read input from STDIN. Print output to STDOUT
familySize = int(input())

roomNums = list(map(int, input().split()))
families = dict()
captain = 0

for fam in roomNums:
    if fam not in families.keys():
        families[fam] = 1
    elif fam in families.keys():
        families[fam] += 1

for cap in families.keys():
    if families[cap] == 1:
        captain = cap
        break

print(captain)

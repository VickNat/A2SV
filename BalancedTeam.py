studs = int(input())
 
team = list(map(int, input().split()))
 
right = studs - 1
 
team.sort()
maxSt = 0
 
right = studs - 1
left = right - 1
 
while left >= 0:
    if team[right] - team[left] <= 5:
        left -= 1
    else:
        maxSt = max((right-left), maxSt)
        right -= 1
        left -= 1
 
maxSt = max((right-left), maxSt)
 
print(maxSt)

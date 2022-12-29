# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())
indexOf = defaultdict(list)

for idx in range(n):
    ch = input()
    indexOf[ch].append(idx+1)

for elm in range(m):
    groupB = input()
    
    if groupB in indexOf:
        print(*indexOf[groupB])
    else:
        print(-1)




# groupA = []
# groupB = []
# from collections import defaultdict

# n, m = map(int, input().split())

# indexOf = defaultdict(list)

# for idx in range(n):
#     indexOf[input()].append(idx+1)

# for elm in range(m):
#     ch = input()
#     if ch in indexOf:
#         print(*indexOf[ch])
#     else:
#         print(-1)
# for elm in range(n):
#     temp = input()
#     groupA.append(temp)
    
# for elm in range(m):
#     tmp = input()
    
#     groupB.append(tmp)
    
# # grpA = dict(groupA)
# # grpB = dict(groupB)

# for index in range(len(groupB)):
#     tmpo = []
#     for element in range(len(groupA)):
#         if groupB[index] == groupA[element]:
#             tmpo.append(element+1)
#     print(*tmpo)

# # print(idxA)

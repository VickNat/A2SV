# Enter your code here. Read input from STDIN. Print output to STDOUT
k_group = input()
room_nums = list(map(int, input().split()))
groups = set()
captain = set()

for idx in room_nums:
    if idx not in groups:
        groups.add(idx)
        captain.add(idx)
    else:
        captain.discard(idx)

captain = list(captain)
print(captain[0])

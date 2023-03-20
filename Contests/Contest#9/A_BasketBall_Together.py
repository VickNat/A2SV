'''
list(map(int, input().split()))
int(input)
'''

N, D = list(map(int, input().split()))
powers = list(map(int, input().split()))

powers.sort()
wins = 0
l = 0
r = N-1

while l <= r:
    sum_ = powers[r]
    temp = [sum_]
    
    while l < r and sum_ <= D and D >= powers[r]*len(temp):
        sum_ += powers[l]
        temp.append(powers[l])
        l += 1
    
    
    if sum_ > D or powers[r]*len(temp) > D:
        wins += 1
    
    r -= 1

print(wins)

size = int(input())

cards = list(map(int, input().split()))

wCards = 0
hCards = 0
counts = 0

left = 0
right = size - 1

while left < right:
    if cards[left] > cards[right]:
        wCards += cards[left]
        left += 1
        counts += 1
    else:
        wCards += cards[right]
        right -= 1
        counts += 1
    
    if cards[left] > cards[right]:
        hCards += cards[left]
        left += 1
        counts += 1    
    else:
        hCards += cards[right]
        right -= 1
        counts += 1
        
if counts < size :
    wCards += cards[left]

print(wCards, hCards)

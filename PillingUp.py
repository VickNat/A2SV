# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for inputs in range(T):
    n = int(input())
    blocks = list(map(int, input().split()))
    
    left = 0
    right = n-1
    prev = max(blocks)
    answer = "Yes"
    
    while(right>=left):
        if blocks[right]>=blocks[left]:
            hold = blocks[right]
            right-=1
        else:
            hold = blocks[left]
            left+=1
        
        if prev >= hold:
            prev = hold
        else:
            answer = "No"
            break
    
    print(answer)

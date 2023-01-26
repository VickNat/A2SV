testCases = int(input())

for tests in range(testCases):
    size = int(input())
    subSeq = list(map(int, input().split()))
    
    subPtr = 0
    maxSum = 0

    while subPtr < size:
        maxVal = subSeq[subPtr]
        
        if subSeq[subPtr] > 0:
            while subPtr < size and subSeq[subPtr] > 0:
                if maxVal < subSeq[subPtr]:
                    maxVal = subSeq[subPtr]
                
                subPtr += 1
            

        else:
            while subPtr < size and subSeq[subPtr] < 0:
                if maxVal < subSeq[subPtr]:
                    maxVal = subSeq[subPtr]
                
                subPtr += 1
            
        maxSum += maxVal
    
    print(maxSum)

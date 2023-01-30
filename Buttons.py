testCases = int(input())

for tests in range(testCases):
    string = list(input())
    
    res = set()
    ptr = 0
    
    while ptr < len(string):
        if ptr + 1 == len(string) or string[ptr] != string[ptr+1]:
            res.add(string[ptr])
            ptr += 1
        elif string[ptr] == string[ptr+1]:
            ptr += 2
        else:
            ptr += 1
    
    result = list(res)
    result.sort()
    
    ans = "".join(result)
    
    print(ans)

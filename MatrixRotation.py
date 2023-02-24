tests = int(input())
 
for _ in range(tests):
    r1 = list(map(int, input().split()))
    r2 = list(map(int, input().split()))
    
    if r1[0] < r1[1] and r1[0] < r2[0] and r1[1] < r2[1] and r2[0] < r2[1]:
        print("YES")
    elif r2[0] < r1[0] and r2[0] < r2[1] and r1[0] < r1[1] and r2[1] < r1[1]:
        print("YES")
    elif r2[1] < r2[0] and r2[1] < r1[1] and r2[0] < r1[0] and r1[1] < r1[0]:
        print("YES")
    elif r1[1] < r2[1] and r1[1] < r1[0] and r2[1] < r2[0] and r1[0] < r2[0]:
        print("YES")
    else:
        print("NO")

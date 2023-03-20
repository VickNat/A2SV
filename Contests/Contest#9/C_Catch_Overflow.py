'''
list(map(int, input().split()))
int(input)
'''

l = int(input())
com = []

for _ in range(l):
    temp = input()
    com.append(temp)

stack = [[1,0]]

for elm in com:
    if elm == "add":
        stack[-1][1] += 1
    elif elm == "end":
        loop, add = stack.pop()
        stack[-1][1] += loop*add
    else:
        _, loop = elm.split()
        stack.append([int(loop), 0])

if stack[-1][1] > 2**32 -1:
    print("OVERFLOW!!!")
else:
    print(stack[-1][1])
    
    
        
        

# Enter your code here. Read input from STDIN. Print output to STDOUT
superSet = list(map(int, input().split()))
size = int(input())
result = []
result.append("True")
for elm in range(size):
    theList = list(map(int, input().split()))
    
    if len(superSet)<=len(theList):
        result.append("False")
        
    else:
        for index in range(len(theList)):
            if theList[index] in superSet:
                continue
            else:
                result.append("False")
    
print(result[-1])

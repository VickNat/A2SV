# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

size = int(input())
distinctWords = defaultdict(int)

for word in range(size):
    temp = input()
    
    if temp in distinctWords:
        distinctWords[temp]+=1
    else:
        distinctWords[temp]=1
        
print(len(distinctWords))
print(*distinctWords.values())

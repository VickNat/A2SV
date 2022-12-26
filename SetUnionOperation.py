# Enter your code here. Read input from STDIN. Print output to STDOUT
englishTotal = input()
englishSub = set(map(int, input().split()))
frenchTotal = input()
frenchSub = set(map(int, input().split()))

answer = englishSub.union(frenchSub)

print(len(answer))

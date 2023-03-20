'''
list(map(int, input().split()))
int(input())
'''

n, m, k = list(map(int, input().split()))
emotes = list(map(int, input().split()))
emotes.sort(reverse=True)

chunk = k+1

full = (emotes[0]*k + emotes[1])*(m//chunk)
remains = m%chunk

# Calculate how much of the larger bunch to add to the answer
part = remains*emotes[0]

print(full + part)


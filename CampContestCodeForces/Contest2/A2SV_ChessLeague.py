'''
list(map(int, input().split()))
int(input())
'''
rating = []
 
def merge(lArr, rArr, K):
  l = 0
  r = 0
  ans = []
 
  while r < len(rArr) and rating[lArr[0]] - rating[rArr[r]] > K:
    r += 1
  
  while l < len(lArr) and rating[rArr[0]] - rating[lArr[l]] > K:
    l += 1
  
  while l < len(lArr) and r < len(rArr):
    if rating[lArr[l]] <= rating[rArr[r]]:
      ans.append(lArr[l])
      l += 1
    else:
      ans.append(rArr[r])
      r += 1
    
  while l < len(lArr):
    ans.append(lArr[l])
    l += 1
  
  while r < len(rArr):
    ans.append(rArr[r])
    r += 1
  
  return ans
 
def mergeSort(left, right, K):
  if left == right:
    return [left]
  
  mid = left + (right-left)//2
 
  leftAns = mergeSort(left, mid, K)
  rightAns = mergeSort(mid+1, right, K)
  
  return merge(leftAns, rightAns, K)
 
def main():
  global rating
  N, K = list(map(int, input().split()))
  players = 2**N
  rating = list(map(int, input().split()))
 
  winners = mergeSort(0, players-1, K)
  ans = [elm+1 for elm in winners]
  ans.sort()
  print(*ans)
 
main()

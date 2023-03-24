'''
list(map(int, input().split()))
int(input())
'''
 
counts = 0
 
def merge(left, right):
  ans = left + right
 
  if left[0] > right[0]:
    ans = right + left
    global counts
    counts += 1
  
  return ans
 
def mergeSort(left, right, nums):
  if left == right:
    return [nums[left]]
  
  mid = left + (right-left)//2
 
  leftAns = mergeSort(left, mid, nums)
  rightAns = mergeSort(mid+1, right, nums)
  
  return merge(leftAns, rightAns)
 
def main():
  global counts
  t = int(input())
 
  for _ in range(t):
    m = int(input())
    nums = list(map(int, input().split()))
    ans = mergeSort(0, m-1, nums)
    nums.sort()
 
    if ans == nums:
      print(counts)
    else:
      print(-1)
    
    counts = 0
 
main()
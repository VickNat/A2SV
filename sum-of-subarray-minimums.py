class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        ptr = 0
        size = len(arr)
        total = 0

        while ptr < size:
            
            while stack and arr[stack[-1]] > arr[ptr]:
                temp = stack[-1]
                stack.pop()
                right = ptr - temp
                left = 0
                if stack:
                    left = temp - stack[-1]
                else:
                    left = temp + 1
                                    
                total += arr[temp]*left*right

            stack.append(ptr)    
            ptr += 1
        
        print(total)
        while stack:
            temp = stack[-1]
            stack.pop()
            right = ptr - temp
            left = 0
            if stack:
                left = temp - stack[-1]
            else:
                left = temp + 1
            
            total += arr[temp]*left*right

        return total % (10**9 + 7)
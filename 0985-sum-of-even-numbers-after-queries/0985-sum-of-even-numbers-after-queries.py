class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        sumEven = 0
        is_even = lambda a: a % 2 == 0
        
        for sums in range(len(nums)):
            if nums[sums]%2==0:
                sumEven += nums[sums]
        
        for query in queries:
            num_to_add = query[0]
            cur_index = query[1]
            cur_num = nums[cur_index]
            tmp = 0
            
            if not is_even(cur_num) and not is_even(num_to_add):
                tmp = cur_num + num_to_add
                
            elif is_even(cur_num) and not is_even(num_to_add):
                tmp = -cur_num
                
            elif is_even(cur_num) and is_even(num_to_add):
                tmp = num_to_add
            
            
#             if num_to_add%2!=0:
#                 if cur_num%2==0:
#                     sumEven-=cur_num
#                     cur_num+=num_to_add
#                 else:
#                     cur_num+=num_to_add
#                     sumEven+=cur_num
                
#             else:
#                 if cur_num%2==0:
#                     sumEven+=num_to_add
#                     cur_num+=num_to_add
#                 else:
#                     cur_num += num_to_add
            
            nums[cur_index] += num_to_add
            sumEven += tmp
            answer.append(sumEven)
        
        return answer
            
#             if idx[0]%2!=0:
                
#                 if nums[idx[1]]%2==0:
#                     sumEven+=nums[idx[1]]
#                     answer.append(sumEven)
#                 else:
#                     answer.append(sumEven)
                    
#             elif nums[idx[1]]%2==0 and idx[0]%2!=0:
#                 sumEven-=nums[idx[1]]
#                 answer.append(sumEven)
#             elif nums[idx[1]]%2==0 and idx[0]%2==0:
#                 sumEven+=idx[0]
#                 answer.append(sumEven)
            
#             nums[idx[1]]+=idx[0]

            
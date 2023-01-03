n = int(input())
 
for idx in range(n):
    word=input()
    stutter=word[0]+word[1]+"... "
    
    answer=stutter+word+"?"
    
    print(answer)

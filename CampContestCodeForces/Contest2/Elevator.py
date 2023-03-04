n = int(input())
 
for _ in range(n):
    walk, elv, elf = list(map(int, input().split()))
    
    opt1 = walk*4
    opt2 = walk*elf + elv*(4-elf)
    opt3 = elf*elv + elv*4
    
    print(min(opt1, opt2, opt3))

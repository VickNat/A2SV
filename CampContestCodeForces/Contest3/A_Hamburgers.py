x = str(input())
ptr = 0
ans = ''
 
while ptr < len(x):
    if 9-int(x[ptr]) < int(x[ptr]):
        ans += str(9-int(x[ptr]))
    else:
        ans += x[ptr]
    ptr += 1
    
temp = list(ans)
if temp[0] == '0':
    temp[0] = x[0]
 
print(int("".join(temp)))

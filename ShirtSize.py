size = int(input())

for idx in range(size):
    compare = list(map(str, input().split()))
    
    shirt1 = compare[0]
    shirt2 = compare[1]
    answer = ""
    
    if (shirt1[-1]=="S" and (shirt2[-1]=="M" or shirt2[-1]=="L")) or (shirt1[-1]=="M" and shirt2[-1]=="L"):
        answer = "<"
    elif (shirt1[-1]=="S" and shirt1[-1]==shirt2[-1]) and (len(shirt1)>len(shirt2)):
        answer = "<"
    elif (shirt1[-1]=="L" and (shirt2[-1]=="M" or shirt2[-1]=="S")) or (shirt1[-1]=="M" and shirt2[-1]=="S"):
        answer = ">"
    elif (shirt1[-1]=="L" and shirt1[-1]==shirt2[-1]) and (len(shirt1)>len(shirt2)):
        answer = ">"
    elif (shirt1[-1]=="L" and shirt1[-1]==shirt2[-1]) and (len(shirt1)<len(shirt2)):
        answer = "<"
    elif (shirt1[-1]=="S" and shirt1[-1]==shirt2[-1]) and (len(shirt1)<len(shirt2)):
        answer = ">"
    elif shirt1[-1]==shirt2[-1] and (len(shirt1)==len(shirt2)):
        answer = "="
        
    print(answer)

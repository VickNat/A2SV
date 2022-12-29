def wrap(string, max_width):
    strList = list(string)
    index = 0
    result=[]
    
    while(index<len(strList)):
        
        if index==0:
            result.append(strList[index])
        elif index%max_width!=0:
            result.append(strList[index])
        else:
            result.append("\n")
            result.append(strList[index])
            
        index+=1
            
    return ''.join(result)

if __name__ == '__main__':

if __name__ == '__main__':
    N = int(input())
    accept = []
    for elm in range(N):
        tmp = input().split()
        
        if tmp[0]=="insert":
            accept.insert(int(tmp[1]), int(tmp[2]))
        elif tmp[0]=="print":
            print(accept)
        elif tmp[0]=="remove":
            accept.remove(int(tmp[1]))
        elif tmp[0]=="append":
            accept.append(int(tmp[1]))
        elif tmp[0]=="sort":
            accept.sort()
        elif tmp[0]=="reverse":
            accept.reverse()
        elif tmp[0]=="pop":
            accept.pop()

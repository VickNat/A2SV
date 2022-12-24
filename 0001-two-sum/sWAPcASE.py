def swap_case(s):
    temp = ""
    for i in s:
        if i.isupper():
            temp+=i.lower()
        else:
            temp += i.upper()
    return temp

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

def swap_case(s):
    ans = ""
    
    for letter in range(len(s)):
        if s[letter].isupper():
            ans+=s[letter].lower()
        elif s[letter].islower():
            ans+=s[letter].upper()
        else:
            ans+=s[letter]
            
    return ans

if __name__ == '__main__':

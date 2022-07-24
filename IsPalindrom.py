def palindrom(string):
    lftstr,rhtstr=0,len(string)-1
    while(lftstr<rhtstr):
        if string[lftstr]!=string[rhtstr]:
            return False
        lftstr+=1
        rhtstr-=1
    return True
    
print(palindrom("abcdba"))

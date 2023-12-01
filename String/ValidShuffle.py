def validShuffle(concat, shuffle):
    if(len(concat) != len(shuffle)): return False
    concatDict = {}

    for i in concat:
        if(i in concatDict):
            concatDict[i] += 1
        else:
            concatDict[i] = 1

    for i in shuffle:
        if(i in concatDict and concatDict[i] > 0):
            concatDict[i] -= 1
        else:
            return False
        
    return True
        


s1 = "abc"
s2 = "def"
shuffle = "fecbad"
if(validShuffle(s1+s2, shuffle)):
    print("valid shuffle")
else:
    print("Invalid shuffle")
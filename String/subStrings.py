# get all possible Substring 
subStrings = []
a = "abcd"
for indx, val in enumerate(a):
    temp = ""
    for j in range(indx, len(a), 1):
        temp += a[j]
        subStrings.append(temp)

    print(subStrings)
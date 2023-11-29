# // Odd Sum
# // Question Name: Odd Sum

# // Problem Statement

# // Antonio got an array A consisting of N integers as his christmas present.

# // Antonio likes an array if and only if the sum of all elements of that array is odd. Like Antonio likes arrays [4,1,4], [2,2,1] etc. but not arrays [4,4], [2,6,2] etc.

# // Now to make array A of his likeness he can perform the belows operations on it :

# // Operation 1:
# // Remove exactly one element from the array.
# // Operation 2:
# // Divide every element of the array by 2.
# // Given array A, print the minimum number of above operations required to make array A of Antonio’s likeness(i.e. To make the sum of all elements of array A odd).

# // Input Format

# // First line contains a single integer denoting N.
# // Next line contains N space separated integers denoting the elements of array A.
# // Output Format

# // Print the minimum number of above operations required to make array A of Antonio’s likeness(i.e. To make the sum of all elements of array A odd).
# // Constraints

# // 1<=N<=105
# // 1<=Ai<=109
# // Sample Input 1

# // 3

# // 6 4 10

# // Sample Output 1

# // 2

# // Explanation of Sample 1

# [6,4,10]

# 3, 2


# op1
def op1(a):
    oddCount = 0
    for i in range(len(a)):
        if(a[i] == -1): continue
        if(oddCount == 0 and a[i]&1):
            oddCount += 1
        elif(a[i]&1):
            a[i] = -1
            break
    return a


# op 2
def op2(a):
    for i in range(len(a)):
        if(a[i] == -1): continue
        a[i] = a[i] // 2
    return a

def chaeckOdd(a):
    sum = 0
    for i in a:
        if(i == -1): continue
        sum += i

    if(sum&1):
        return True
    else:
        return False


def oddSum(a):
    operations = 0
    while(True):
        if(chaeckOdd(a)):
            return operations
        count = 0
        for i in a:
            if(i == -1): continue
            if(i&1):
                count+=1

        if(count > 1):
            a = op1(a)
        elif(count == 0):
            a = op2(a)

        operations += 1
        

a = [6,4,10]
print("Minimum Operations", oddSum(a))
# Even Odd 
# a = input("Enter a Number: ")
# a = int(a) 
# if(a%2 == 0):
#     print("Even")
# else:
#     print("Odd")


# Max Number

# print(list(range(1, 101, 1)))
# a = [2,3,4,8,7]
# max = a[0]
# for i in a:
#     if(max < i):
#         max = i

# print(max)

# 1. SUM of all Entered Numbers
# sum = 0
# for i in [1,2,3,4,5]:
      
#     sum = sum + i

# print(sum)

# Reverse String
# str = "Hello"
# strLen = len(str)

# for i in range(strLen-1, -1, -1):
#     print(str[i], end="")    


# Reverse String
# str = "Hello"
# a = ""
# for i in str:
#     a = i + a   

# print(a)


# 2. Count of Even No & Count of Odd Numbers
# list=[1,2,3,4,5,6,7,8,9,10]
# ec=0
# oc=0
# for i in list:
#     if(i%2==0):
#         ec+=1
#     else:
#         oc+=1
# print(ec,oc)


# 3. First Even No || First Odd No
# list = [3,5,7,1,2,3,4,2,2]

# for i in list:
#     if(i % 2==0):
#         print(i)
#         break    

# 4. Maximum Number
# list = [2,4,5,5,7,6]
# max = list[0]

# for i in list:
#     if(max < i):
#         max = i

# print(max)


a = [22,3,11,444,12,13,88882,3,4]
twoDigit = 0
threeDigit = 0
for i in a:
    aLen = len(str(i))
    if(aLen == 2):
        twoDigit += i
    elif(aLen == 3):
        threeDigit += i

print(twoDigit, threeDigit)
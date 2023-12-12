def createNode(data):
    return {
        "data": data,
        "next": None 
    }

def addAtHead(head, data):
    if(head == None): return createNode(data)
    newNode = createNode(data)
    newNode["next"] = head
    return newNode


def printLinkedList(head):
    temp = head
    while(temp != None):
        print(temp["data"], "", end="", sep=" => ")
        temp = temp["next"]
    print("end")

def addAtTail(head, data):
    if(head == None): return createNode(data)
    newNode = createNode(data)
    temp = head
    while(temp["next"] != None):
        temp = temp["next"]

    temp["next"] = newNode
    return head


def removeAtHead(head):
    if(head == None): return None
    temp = head
    temp = temp["next"]
    head["next"] = None

    return temp


def removeAtEnd(head):
    if(head["next"] == None): return None
    temp = head
    while(temp["next"]["next"] != None):
        temp = temp["next"]
    temp["next"] = None
    return head

h1 = None 
h2 = None
h3 = None

h1 = addAtHead(h1, 3)
h1 = addAtHead(h1, 2)
h1 = addAtHead(h1, 1)
h1 = addAtHead(h1, 5)
h1 = addAtHead(h1, 6)



h2 = addAtHead(h2, 1)
h2 = addAtHead(h2, 2)
h2 = addAtHead(h2, 3)

# printLinkedList(h1)
# printLinkedList(h2)

def sumLinkedList(h1, h2, h3):
    t1 = h1 
    t2 = h2

    while(t1 != None and t2 != None):
        h3 = addAtTail(h3, t1["data"] + t2["data"])

        t1 = t1["next"]
        t2 = t2["next"]
    
    return h3


def getLength(head):
    temp = head
    count = 0
    while(temp != None):
        count+=1
        temp = temp["next"]

    return count

def makeSameSizeList(h1, h2, h3):
    h1Len = getLength(h1)
    h2Len = getLength(h2)

    diff = abs(h1Len - h2Len)

    small = None
    if(h1Len < h2Len):
        small = h1
    else:
        small = h2

    while(diff > 0):
        small = addAtHead(small, 0)
        diff -= 1

    if(h1Len < h2Len):
        h1 = small
    else:
        h2 = small

    return sumLinkedList(h1, h2, h3)
    
h3 = makeSameSizeList(h1, h2, h3)
printLinkedList(h3)
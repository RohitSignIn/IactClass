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

head = None
head = addAtHead(head, 4)
head = addAtHead(head, 3)
head = addAtHead(head, 2)
head = addAtHead(head, 1)

head = addAtTail(head, 6)
head = addAtTail(head, 7)
head = removeAtHead(head)
head = removeAtHead(head)
head = removeAtHead(head)


head = removeAtEnd(head)
head = removeAtEnd(head)

head = removeAtEnd(head)


printLinkedList(head)
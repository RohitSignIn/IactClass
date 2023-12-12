# Remove Nth Node from End 


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

printLinkedList(head)


def removeNthNode(head, removal):
    prev = head 
    next = head 

    jump = removal 

    while(jump):
        next = next["next"]
        jump -= 1

    while(next["next"] != None):
        prev = prev["next"]
        next = next["next"]

    newConnect = prev["next"]["next"] 
    prev["next"]["next"] = None

    prev["next"] = newConnect

    return head

head = removeNthNode(head, 2)
printLinkedList(head)
def ListTraversal(head):
    temp = head
    while(temp != None):
        print(temp["data"], "", end="", sep=" => ")
        temp = temp["next"]
    
    print("end", end="", sep=" => ")

def createNode(data):
    return {
        "data": data,
        "next": None
    }

def addAtHead(Head, data):
    newNode = createNode(data)
    newNode["next"] = Head
    return newNode





Head = None
Head = addAtHead(Head, 1)
Head = addAtHead(Head, 2)
Head = addAtHead(Head, 3)
Head = addAtHead(Head, 4)
Head = addAtHead(Head, 5)

ListTraversal(Head)
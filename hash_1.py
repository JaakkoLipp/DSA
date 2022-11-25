import instructions

def hash(m, data):
    sum = 0
    for i in range(len(data)):
        sum += ord(data[i])
    return (sum % m)

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.tail = Node(None, None)
        self.head = Node(None, self.tail)
        self.len = 0

    def append(self, data):
        new=Node(data,None)
        current=self.head
        if self.head.next == self.tail:
            self.head.next=new
            new.next=self.tail
        else:
            while current.next is not self.tail:
                current=current.next
            current.next=new
            new.next=self.tail
        self.len=self.len+1
        return

    def print(self):
        current=self.head
        i=0
        while i<self.len-1:
            current=current.next
            print(current.data,"-> ",end="")
            i+=1
        
        current=current.next
        print(current.data)
        return

    def delete(self, index):
        if(index>=self.len):
            return
        prev=self.head
        current=self.head.next
        i=0
        while i<index:
            prev=prev.next
            current=current.next
            i+=1
        prev.next=current.next
        self.len=self.len-1
        return
    
    def insert(self, data, index):
        new=Node(data, None)
        prev=self.head
        i=0
        while i<index:
            prev=prev.next
            i+=1
        new.next=prev.next
        prev.next=new
        self.len=self.len+1
        return

    def index(self, data):
        cur=self.head
        for i in range(self.len):
            cur=cur.next
            if cur.data==data:
                return i
        return -1

class HashTable:
    def __init__(self, M):
        self.M = M
        self.T = [None] * M
    
    def hashAdd(self, data):
        i = hash(self.M, data)
        if self.T[i] == None:
            print("Creating new LL at:",i, "for:",data)
            L = LinkedList()
            L.append(data)
            self.T[i] = L
        elif(self.T[i] != None):
            print("Added at:",i,data)
            self.T[i].append(data)
        else:
            print("error inserting key")
            self.T[i].append(data)
    
    def remove(self, data):
        i = hash(self.M, data)
        if self.T[i] == data:
            self.T[i] = None
    
    def search(self, data):
        Lcounter=0
        for i in self.T:
            Lcounter+=1
            finder=i.index(data)
            if(finder!=-1):
                print("\nLocation of",data+":",finder, "in LL:",Lcounter)
                return
            else:
                print("L bozo")
        return
    
    def print(self):
        print("\nPrinting LL:")
        Lcounter=0
        for i in self.T:
            if (i is not None) and (i != "Del"):
                Lcounter+=1
                print("LL:",Lcounter)
                i.print()
        return

if __name__ == "__main__":
    print("--- Tests: ---")
    instructions.tests()
    print("\n--- Done! ---")

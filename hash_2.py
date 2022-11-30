def hash(m, data):
    data=str(data)
    sum = 0
    for i in range(len(data)):
        sum += ord(data[i])*(i+1)
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
            print("---Error inserting key---")
            self.T[i].append(data)
    
    def remove(self, data):
        i = hash(self.M, data)
        iL=self.T[i].index(data)
        if (iL!=-1):
            self.T[i].delete(iL)
            print("Removed:",data)
        else:
            print("---Removing Error---")
        return
    
    def search(self, data):
        datastr=str(data)
        i = hash(self.M, data)
        finder=self.T[i].index(data)
        if(finder!=-1):
            print("\nLocation of",datastr+": node",finder, "in LL:",i)
            return
        print(data,"Not Found")
        return
    
    def print(self):
        print("\nPrinting HT:")
        Lcounter=0
        for i in self.T:
            if (i is not None) and (i != "Del"):
                print("LL:",Lcounter)
                Lcounter+=1
                i.print()
        return

if __name__ == "__main__":
    print("--- Tests: ---")
    
    table = HashTable(3)
    table.hashAdd(12)
    table.hashAdd("hashtable")
    table.print()
    table.hashAdd(1234)
    table.print()
    table.hashAdd(4328989)
    table.print()
    table.hashAdd("BM40A1500")
    table.print()
    table.hashAdd(-12456)
    table.print()
    table.hashAdd("aaaabbbbcccc")
    table.print()

    table.search(-12456)
    table.search("hashtable")
    table.search("1235")
    table.remove("BM40A1500")
    table.remove(1234)
    table.remove("aaaabbbbcccc")
    table.print()
    table.search(12)

    print("\n--- Done! ---")

"""
TO-DO:
-m=3, 12, 'hashtable', 1234, 4328989, 'BM40A1500', -12456, 'aaaabbbbcccc' 

"""
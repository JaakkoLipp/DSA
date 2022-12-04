
def hash(m, data):
    data=str(data)
    sum = 0
    for i in range(len(data)):
        sum += ord(data[i])**(i+1)
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
        if (type(self.T[i]) is not LinkedList):
            return 0
        finder=self.T[i].index(data)
        if(finder!=-1):
            print("\nLocation of",datastr+": node",finder, "in LL:",i)
            return 1
        return 0
    
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
    
    table = HashTable(10000)
    f=open("words_alpha.txt")
    for line in f:
        line=line.rstrip('\n')
        table.hashAdd(line)
    f.close()

    counter=0
    f=open("kaikkisanat.txt")
    for line in f:
        line=line.rstrip('\n')
        if(table.search(line)!=1):
            table.hashAdd(line)
        else:
            counter+=1
    f.close()
    print(type(table.T[0]))
    #uncomment to print full table
    # table.print()
    #uncomment to print full table

    print("Same words:",counter)

    print("\n--- Done! ---")
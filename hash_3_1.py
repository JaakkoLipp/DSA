# hashing function
def hash(m, data):
    data=str(data)
    sum = 0
    # for every char in data, (unicode value)^i+1
    # position aware string folding, improves runtimes
    for i in range(len(data)):
        sum += ord(data[i])**(i+1)
    return (sum % m)
    # sum modulo tablearray size, return slot

# Linked list node, stores value and next node
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

# linked list
# stores head and tail node data, and length
class LinkedList:
    def __init__(self):
        self.tail = Node(None, None)
        self.head = Node(None, self.tail)
        self.len = 0

    #add to LL
    def append(self, data):
        new=Node(data,None)
        current=self.head
        #if no nodes in LL, add behind head node
        if self.head.next == self.tail:
            self.head.next=new
            new.next=self.tail
        else:
            #else iterate until tail, add before tail
            while current.next is not self.tail:
                current=current.next
            current.next=new
            new.next=self.tail
        self.len=self.len+1
        return

    # iterate whole LL, print data node values
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


    # node removing
    def delete(self, index):
        if(index>=self.len):
            return
        prev=self.head
        current=self.head.next
        i=0
        #find node at index and bypass it
        while i<index:
            prev=prev.next
            current=current.next
            i+=1
        prev.next=current.next
        self.len=self.len-1
        return
    
    # add node at index
    def insert(self, data, index):
        new=Node(data, None)
        prev=self.head
        i=0
        #iterate until index next
        while i<index:
            prev=prev.next
            i+=1
        # new is added after prev, prev.next moved to new.next
        new.next=prev.next
        prev.next=new
        self.len=self.len+1
        return

    # return index of node in LL
    def index(self, data):
        cur=self.head
        for i in range(self.len):
            cur=cur.next
            if cur.data==data:
                return i
        return -1

# Hashtable class
class HashTable:
    # M=table size, T = table sized M
    def __init__(self, M):
        self.M = M
        self.T = [None] * M
    
    # calulate has value then append to LL in position i of T[]
    def hashAdd(self, data):
        i = hash(self.M, data)
        # if T[i] doesnt have a LL yet, create one and append
        if self.T[i] == None:
            print("Creating new LL at:",i, "for:",data)
            L = LinkedList()
            L.append(data)
            self.T[i] = L
        # LL exists, append
        elif(self.T[i] != None):
            print("Added at:",i,data)
            self.T[i].append(data)
        else:
            print("---Error inserting key---")
            self.T[i].append(data)

    # removing from the hash table
    def remove(self, data):
        i = hash(self.M, data)
        iL=self.T[i].index(data)
        # call index for data for LL in slot, then call delete on index
        if (iL!=-1):
            self.T[i].delete(iL)
            print("Removed:",data)
        else:
            print("---Removing Error---")
        return
    
    # search if value is in hashtable
    def search(self, data):
        datastr=str(data)
        i = hash(self.M, data)
        # if slot is empty return not found
        if (type(self.T[i]) is not LinkedList):
            return 0
        # LL index is used to locate data from LL in slot
        finder=self.T[i].index(data)
        # return 1 if found, 0 if not found
        if(finder!=-1):
            print("\nLocation of",datastr+": node",finder, "in LL:",i)
            return 1
        return 0
    
    # print out whole data structure and data stored
    def print(self):
        print("\nPrinting HT:")
        Lcounter=0
        # call LL.print on every slot in T
        for i in self.T:
            if (i is not None):
                print("LL:",Lcounter)
                Lcounter+=1
                i.print()
        return


# task
if __name__ == "__main__":
    print("--- Tests: ---")
    
    # create new HT
    table = HashTable(10000)

    # handle EN words
    f=open("words_alpha.txt")
    for line in f:
        line=line.rstrip('\n')
        table.hashAdd(line)
    f.close()

    # same word counter
    counter=0
    # handle FI words
    f=open("kaikkisanat.txt")
    for line in f:
        line=line.rstrip('\n')
        if(table.search(line)!=1):
            table.hashAdd(line)
        else:
            counter+=1
    f.close()

    #uncomment to print full table
    #table.print()
    #uncomment to print full table

    print("Same words:",counter)

    print("\n--- Done! ---")
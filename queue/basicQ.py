class Queue:
    
    def __init__(self): 
        self.items = [] 
    
    def isEmpty(self): 
        return self.items == [] 

    def enqueue(self, item):  
        self.items.insert(0,item)

    def dequeue(self): 
        return self.items.pop() 

    def size(self):
        return len(self.items) 

    def __str__(self):
        return str(self.items)
    
    def peek(self):
        return self.items[0]
    
    def index(self) :
        return len(self.items)-1
    
    def re(self) :
        self.items.reverse()
        return str(self.items)
        
    
q = Queue()


s = input("Enter Input : ").split(",") 
r = []
i = int(0)
while  i < len(s):
  mode = s[i].split()[0]
  
  if mode == 'E' :
      value = s[i].split()[1]
      q.enqueue(value)
      print("Add",q.peek(),"index is",q.index())
  elif mode == 'D' and not q.isEmpty():
      
      print("Pop",q.dequeue(),"size in queue is",q.size())
  else :
      print("-1")
  i+=1
  
if q.isEmpty() :
    print("Empty")

else :
    print("Number in Queue is : ",q.re())
      
class Node(object):
  
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def get_data(self):
        return self.val
      
    def set_data(self, val):
        self.val = val
 
    def get_next(self):
        return self.next
 
    def set_next(self, next):
        self.next = next
      
 
class LinkedList(object):
  
    def __init__(self, head = None):
        self.head = head
        self.count = 0
        
    def insert(self, data):
        
        new_node = Node(data)
        
        new_node.set_next(self.head)
        
        self.head = new_node
        
        self.count += 1
        
    def find(self, val):
        
        item = self.head
        
        while item != None:
           
           
           if item.get_data() == val:
               return item
           
           
           else:
                item = item.get_next()
              
        return None
  
    def remove(self, item):
        
        current = self.head
        
        previous = None
       
        while current is not None:
            
            if current.data == item:
                break
            
            previous = current
            current = current.get_next()
            
        if current is None:
            raise ValueError(f"{item} is not in the list")
        
        if previous is None:
            self.head = current.next
            self.count -= 1
       
        else:
             previous.set_next(current.get_next())
             self.count -= 1
              
    def get_count(self):
        
        return self.count
      
    def is_empty(self):
        
        return self.head == None
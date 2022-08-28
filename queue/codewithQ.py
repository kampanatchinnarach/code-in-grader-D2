class Queue:
  def __init__(self,L=None):
    if L == None:
      self.list = []
    else:
      self.list = L

  def enQueue(self,data):
    self.list.append(data)
    
  def deQueue(self):
    return self.list.pop(0)

  def isEmpty(self):
    return self.list == []

  def size(self):
    return len(self.list)

  def __str__(self):
    return str(self.list)

s  = input('Enter code,hint : ').split(',')
code = []
code.extend(s[0])
h = s[1]
decode =ord(h) - ord(code[0]) 
q = Queue()
for i in range(len(code)):
  q.enQueue(chr(ord(code[i]) + decode))
  print(q)
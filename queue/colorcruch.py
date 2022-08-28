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

  def insert(self,item):
    return self.list.insert(2,item)
    
  def front(self):
    return self.list[0]

  def rear(self):
    return self.list[-1]
  
  def isEmpty(self):
    return self.list == []

  def size(self):
    return len(self.list)

  def reverse(self):
    self.list = self.list[::-1]
    
  def __str__(self):
    return str(self.list)

class Stack:
  def __init__(self,L=None):
    if L == None:
      self.list = []
    else:
      self.list = L

  def push(self,data):
    self.list.append(data)

  def pop(self):
    return self.list.pop()

  def peek(self):
    return self.list[-1] 

  def isEmpty(self):
    return self.list == []

  def size(self):
    return len(self.list)

  def reverse(self):
    self.list = self.list[::-1]
    
  def __str__(self):
    return str(self.list)

def reverseString(s = ''):
  return s[::-1]


p = input('Enter Input (Normal, Mirror) : ').split()
norm = []
norm.extend(p[0])
mirr = []
mirr.extend(p[1])

mirr.reverse()
mirr = Queue(mirr)
norm = Queue(norm)



item  = Queue()
left_color1 = Stack()
box = mirr.deQueue()
c = 1
mirr_ep = 0
while not mirr.isEmpty():
  if mirr.front() == box:
    c += 1
    mirr.deQueue()
    
    if norm.isEmpty():
      for i in range(c):
        left_color1.push(box)
  else:
    for i in range(c):
      left_color1.push(box)
    box = mirr.deQueue()
    c = 1
    
    if mirr.isEmpty():
      left_color1.push(box)

  if c == 3:
    mirr_ep += 1
    item.enQueue(box)
    '''when push item push color in left_color back to mirr for check explosive case again'''
    mirr.reverse()
    while not left_color1.isEmpty():
      
      mirr.enQueue(left_color1.pop())
    else:
      mirr.reverse()
    if not mirr.isEmpty():
      box = mirr.deQueue()
      c = 1
      if mirr.isEmpty():
        left_color1.push(box)
  

left_color2 = Stack()
box = norm.deQueue()
c2 = 1
norm_explo = 0
c_fail = 0
while not norm.isEmpty():
  if norm.front() == box:
    c2 += 1
    norm.deQueue()
    
    if norm.isEmpty() and c2 != 3:
      for i in range(c2):
        left_color2.push(box)
  else:
    for i in range(c2):
      left_color2.push(box)
    box = norm.deQueue()
    c2 = 1
    
    if norm.isEmpty():
      left_color2.push(box)
      
  if c2 == 3 :
    if item.isEmpty():
      norm_explo += 1
      norm.reverse()
      '''when push item push color in left_color back to mirr for check explosive case again'''
      while not left_color2.isEmpty():
        
        if norm.isEmpty(): 
          left_color2.pop()
        else:
          norm.enQueue(left_color2.pop())
      else:
        norm.reverse()
      if not norm.isEmpty():
        box = norm.deQueue()
        c2 = 1
        if norm.isEmpty():
          left_color2.push(box)
    else:
      norm.reverse()
      for i in range(c2):
        norm.enQueue(box)
      norm.reverse()
      norm.insert(item.deQueue())
      
      box = norm.deQueue()
      tmp = Stack()
      tmp.push(box)
      itr_fail = False
      for i in range(2):
        if norm.front() == box:
          itr_fail = True
          tmp.push(norm.deQueue())
        else:
          tmp.push(norm.deQueue())
          itr_fail = False
          break
      if itr_fail:
        c_fail += 1
        while not tmp.isEmpty():
          tmp.pop()
      else:
        norm.reverse()
        while not tmp.isEmpty():
          norm.enQueue(tmp.pop())
        norm.reverse()
      box = norm.deQueue()
      c2 = 1


left_color2.reverse()
mirr_left = ''.join(left_color1.list)
norm_left = ''.join(left_color2.list)
if mirr_left == '':
  mirr_left = 'Empty'
  
if norm_left == '':
  norm_left = 'Empty'

print('NORMAL :')
print(left_color2.size())
print(norm_left)
print(f'{norm_explo} Explosive(s) ! ! ! (NORMAL)')
if c_fail > 0:
  print(f'Failed Interrupted {c_fail} Bomb(s)')
else:
  pass
print('------------MIRROR------------')
print(': RORRIM')
print(reverseString(str(left_color1.size())))
print(reverseString(mirr_left))
print(f'(RORRIM) ! ! ! (s)evisolpxE {mirr_ep}')
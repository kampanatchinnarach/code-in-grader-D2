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

people = input('Enter people and time : ')
list = []

list.extend(people.split()[0])
num = int(people.split()[1])
main_q = Queue(list)
cash_1 = Queue()
cash_2 = Queue()
count_1 = 0
count_2 = 0

for i in range(1,num+1):
  
  if cash_1.size() < 5 and not main_q.isEmpty():
    tmp_1 = main_q.deQueue()
    cash_1.enQueue(tmp_1)
    count_1 += 1
    if not cash_2.isEmpty():
      count_2 += 1
    elif  main_q.isEmpty():
      count_2 +=1
  elif cash_1.size() >= 5 :
    count_1 += 1
    if cash_2.size() < 5 and not main_q.isEmpty():
      tmp_2 = main_q.deQueue()
      cash_2.enQueue(tmp_2)
      count_2 +=1
    elif cash_2.size() >= 5:
      count_2 += 1
    elif not cash_2.isEmpty() and main_q.isEmpty():
      count_2 += 1
  elif cash_1.size() < 5 and main_q.isEmpty() and not cash_2.isEmpty() :
      count_2 += 1
  print(i,main_q,cash_1,cash_2)
  
  if count_1 == 3 and not cash_1.isEmpty():
    cash_1.deQueue()
    count_1 = 0
    
  if count_2 % 2 == 0 and not cash_2.isEmpty():
    cash_2.deQueue()
    
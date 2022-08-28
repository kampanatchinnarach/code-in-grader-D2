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


def changeToString(q = Queue()):
    
  actdict = {
  '0' : 'Eat',
  '1' : 'Game',
  '2' : 'Learn', 
  '3' : 'Movie'
  }

  placedict = {
    '0' : 'Res.',
    '1' : 'ClassR.',
    '2' : 'SuperM.', 
    '3' : 'Home'
  }
  
  
  for data in q.list[:]:
    temp = q.deQueue().split(':')
    temp[0] = actdict[temp[0]]
    temp[1] = placedict[temp[1]]
    s = temp[0] + ':' + temp[1]
    q.enQueue(s)
  return q.list


def scoreCal(me = Queue(),her = Queue()):
  score = 0
  for i in range(me.size()):
    temp = me.list[i].split(':')
    act_me = temp[0]
    place_me = temp[1]
    temp = her.list[i].split(':')
    act_her = temp[0]
    place_her = temp[1]
    if act_me == act_her and place_me == place_her:
      score += 4
    elif act_me == act_her and place_me != place_her:
      score += 1
    elif act_me != act_her and place_me == place_her:
      score += 2
    else:
      score -= 5
  else:
    if score >= 7:
      status = "Yes! You're my love! : Score is {s}.".format(s = score)
    elif score < 7 and score > 0:
      status = "Umm.. It's complicated relationship! : Score is {s}.".format(s = score)
    else:
      status = "No! We're just friends. : Score is {s}.".format(s = score)
      
  return status


p = input('Enter Input : ').split(',')
me = Queue()
you = Queue()
for data in p:
  box_1 = data.split()
  me.enQueue(box_1[0])
  you.enQueue(box_1[1])
print('My   Queue = ',end = '') 
print(*me.list,sep = ', ')
print('Your Queue = ',end = '') 
print(*you.list,sep = ', ')
print('My   Activity:Location = ' ,end='')
print(*changeToString(me), sep = ', ')
print('Your Activity:Location = ', end = '') 
print(*changeToString(you), sep = ', ')
print(scoreCal(me,you))
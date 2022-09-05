class Stack:
     def __init__(self): #// สร้าง constructor ให้ class
         self.items = [] #// สร้าง list ที่ชื่อ items (ในที่นี้ก็คือ stack เดี๋ยว list ค่อยว่ากันอีกที)

     def isEmpty(self): #// สร้าง method isEmpty() เพื่อเช็ค stack ว่าว่างมั๊ย
         return self.items == [] #// ใช้ตรวจสอบ stack

     def push(self, item): #// สร้าง method push() เพื่อเพิ่มข้อมูลลง stack
         self.items.append(item) #// ใช้ method append() ของ list เพื่อเพิ่มข้อมูล

     def pop(self): #// สร้าง method pop() เพื่อ remove ค่าใน stack
         return self.items.pop() #// นำค่าออกจาก stack ด้วย method pop() ของ list

     def peek(self): #// สร้าง method สำหรับ fetch ค่า top จาก stack
         return self.items[len(self.items)-1] # ครับ มันเป็นเทคนิค n-1 ของ array นั้นแหละ เพื่อดึงค่าตรง top ออกมา

     def size(self): #// สร้าง method size() เพื่อดูขนาดของ stack
         return len(self.items) #// ครับ ใช้ len() คงไม่ต้องอธิบายหรอกน่ะ
     def value(self):
         pass
     
stack = Stack()

s = input("Enter Input : ").split(",") 

i = int(0)
while  i < len(s):
  mode = s[i].split()[0]
  
  #stack.push(s[i])
  if mode =='A' :
      value = s[i].split()[1]
      stack.push(value)
      print("Add =",stack.peek(),"and Size =",stack.size())
  else :
      if stack.size()==0:
          print("-1")
      else :
          print("Pop =",stack.pop(),"and Index =",stack.size())
      
  i +=1
if stack.size() == 0:
    print("Value in Stack = Empty")
else :
    print("Value in Stack = ",end = "")
    for i in range(len(stack.items)):
             print(f"{stack.items[i]} ",end = "")
   # print("Value in Stack = " ,stack.value())
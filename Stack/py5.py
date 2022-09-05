class Stack:

    """class Stack
        default : empty stack / Stack([...])
    """
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, s):
            self.items.append(s)

    def pop(self):
            return self.items.pop()

    def peak(self):
            return self.items[-1]
    
    def isEmpty(self):
            return self.items == []

    def size(self):
            return len(self.items)
    
    def hight_A(self):
        if self.size() > 0:
            return self.peak()
        else:
            return 0
    def __str__(self):
        s = ''
        for i in self.items :
            s += str(i)
        return s

    

    

print(" ***Decimal to Binary use Stack***")

def decimalToBinary(ip_val):
    if ip_val >= 1:
    
        decimalToBinary(ip_val // 2)
        s.push(ip_val%2)
 
# Driver Code
if __name__ == '__main__':
    s = Stack()
    ip_val = int(input("Enter decimal number : "))
    decimalToBinary(ip_val)
    print("Binary number :",s)

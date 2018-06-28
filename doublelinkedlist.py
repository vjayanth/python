import sys
def main():
    class node:
        def __init__(self,data=None,prev=None,next=None):
            self.data = data
            self.prev = prev
            self.next = next
    class doublelinkedlist:
        def __init__(self):
            self.head = None

        def insertFirst(self,ele):
            print(self.head)
            if self.head is None:
                self.head = node(data=ele)
            else:
                curr = node(data=ele)
                print(self.head.prev)
                self.head.prev = curr
                curr.next = self.head
                self.head = curr
        def insertLast(self,ele):
            if self.head is None:
                self.head = node(data=ele)
            else:
                curr = self.head
                while curr.next:
                    curr = curr.next
                temp = node(data=ele)
                curr.next = temp
                temp.prev = curr               
        def print(self):
            curr = self.head
            while curr:
                print(curr.data + '->',end = '')
                curr = curr.next
        def search(self,ele):
            i = 0
            curr = self.head
            while curr:
                if curr.data == ele:
                    print('element found at' , i)
                    return
                else:
                    i = i+1
                    curr = curr.next
            print('element cannot found')
        def delete(self,ele):
            curr = self.head
            while curr:  
                if curr.data == ele:
                    temp = curr.prev
                    temp.next = curr.next
                    print("element deleted " , ele)
                    return
                else:
                    curr = curr.next
    a = doublelinkedlist()    
    while True:
        print('press 1 to insert last')
        print('press 2 to insert first')
        print('press 3 to search element')
        print('press 4 to delete element')
        print('press 5 to print')
        print('Type exit to exit')
        res = input()
        if res == 'exit':
            sys.exit() 
        elif res == '1':
            ele = input('enter element to enter ')
            a.insertLast(ele)
        elif res == '2':
            ele = input('enter element to enter ')
            a.insertFirst(ele)    
        elif res == '3':
            ele = input('search element ')
            a.search(ele)
        elif res == '4':
            ele = input('delete element ')
            a.delete(ele)         
        elif res == '5':
            a.print()

if __name__ == '__main__':
    main()
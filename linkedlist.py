import sys

def main():
    class node:
        def __init__(self,data=None,next=None):
            self.data = data
            self.next = next

    class linkedlist:
        def __init__(self):
            self.head = None

        def insert(self,data):
            if not self.head: 
                self.head = node(data=data)
            else:
                curr = self.head
                while curr.next is not None:
                    curr = curr.next
                curr.next = node(data=data)    

        def print(self):
            while self.head:
                print(self.head.data + ' -> ')
                self.head = self.head.next

    a = linkedlist()    
    while True:
        print('Type exit to exit')
        res = input()
        if res == 'exit':
            sys.exit() 
        elif res == '1':
            ele = input('enter element to enter')
            a.insert(ele)
        elif res == '2':
            a.print()          


if __name__ == '__main__':
    main()
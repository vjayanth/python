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
            ele = input('search element')
            a.search(ele)
        elif res == '4':
            ele = input('delete element')
            a.delete(ele)         
        elif res == '5':
            a.print()

if __name__ == '__main__':
    main()
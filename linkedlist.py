import sys


def main():
    class node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

    class linkedlist:
        def __init__(self):
            self.head = None

        def insertLast(self, data):
            if not self.head:
                self.head = node(data=data)
            else:
                curr = self.head
                while curr.next is not None:
                    curr = curr.next
                curr.next = node(data=data)

        def print(self):
            curr = self.head
            while curr:
                print(curr.data + ' -> ', end='')
                curr = curr.next

        def insertFirst(self, data):
            curr = node(data=data)
            curr.next = self.head
            self.head = curr
            print('head is ' + self.head.data)

        def search(self, ele):
            curr = self.head
            i = 0
            while curr:
                if curr.data == ele:
                    print('Element found at ', i)
                    return
                else:
                    i = i+1
                    curr = curr.next
            print("Element not found")
            return

        def delete(self, ele):
            curr = self.head
            i = 0
            while curr:
                if curr.next.data == ele:
                    curr.next = curr.next.next
                    print('Element deleted ', ele)
                    return
                else:
                    i = i+1
                    curr = curr.next
            print("Element not found")
            return

    a = linkedlist()
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

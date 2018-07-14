import sys


def main():
    class node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    class binarytree:
        def __init__(self):
            self.head = None

        def insert(self, ele):
            if self.head is None:
                self.head = node(data=ele)
            else:
                temp = node(data=ele)
                curr = self.head
                while True:
                    print('in')
                    if curr.data == ele:
                        print("Element alerady exists")
                        return
                    elif curr.data > ele:
                        if curr.left:
                            curr = curr.left
                        else:
                            curr.left = temp
                            return

                    elif curr.data < ele:
                        if curr.right:
                            curr = curr.right
                        else:
                            curr.right = temp
                            return

        def printEle(self):
            curr = self.head
            if curr.data:
                print(' ', curr.data)
                self.printData(curr)

        def printData(self, node):
            print(' ')
            if node.right:
                print('right ele:', node.right.data, 'parent:', node.data)
                self.printData(node.right)
            if node.left:
                print('left ele:', node.left.data, 'parent:', node.data)
                self.printData(node.left)

        def search(self):
            print('in search')

    a = binarytree()
    while True:
        print("Enter 1 to insert")
        print('Enter 2 to search element')
        print('Enter 3 to print')
        print('Type exit to exit')
        res = input()
        if res == 'exit':
            sys.exit()
        elif res == '1':
            ele = input('enter element to enter ')
            a.insert(ele)
        elif res == '2':
            ele = input('enter element to search ')
            a.search(ele)
        elif res == '3':
            a.printEle()


if __name__ == '__main__':
    main()

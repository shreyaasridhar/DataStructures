from binarysearchtree import BinarySearchTree

def testtree():
    T=BinarySearchTree()
    n=int(raw_input())
    for i in range(n):
        T.insertElement(int(raw_input("Enter element "+str(i+1)+" : ")))
    l=int(raw_input("Enter Lower Value: "))
    h=int(raw_input("Enter Higher Value: "))
    print T.SumofValues(T.root,l,h)
    print "The tree is:" 
    T.inorderTraverse(T.root)


def main():
    testtree()
        
    
if __name__ == '__main__':
    main()
        

    
